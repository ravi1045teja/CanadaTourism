import { AuthService } from './../authentication.service';
import { TicketService } from './../ticket.service';
import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { ActivatedRoute, ParamMap ,Router} from '@angular/router';
import {Package} from '../models/package';
import { MatDatepickerInputEvent } from '@angular/material';




@Component({
  selector: 'app-book-ticket',
  templateUrl: './book-ticket.component.html',
  styleUrls: ['./book-ticket.component.css']
})
export class BookTicketComponent implements OnInit {
destination:any;
packages:any;
selectedSource:any;
selectedPackage:any;
selectedAdults:any;
selectedChildren:any;
departingDt:Date;
returnDt:Date;
adults:any;
children:any;
creditCard:number;
returning:Date;
user_id:any;
transaction_id:any;
ticketPrice:any;
dateMinArrival = new Date();
@Output() 
dateChange:EventEmitter< MatDatepickerInputEvent< any>>;

email:any;
selectedDestination:any;
  constructor(private route:ActivatedRoute,
    private ticketService:TicketService,
    private authService:AuthService,
    private router:Router
    ) { }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      console.log(params.get('destination'));
      this.destination = params.get('destination');
      this.retrievePackages(this.destination);
      this.email=this.ticketService.email;

      this.authService.validate().subscribe(data=>{
        console.log(data);
        console.log(data.data.public_id);
        this.user_id=data.data.public_id;
      })
    });   
  }
  retrievePackages(dest){
    this.ticketService.getPackages(dest).subscribe(data=>{
      this.packages=data;
      //this.p=JSON.stringify(this.packages);
      console.log(data);
      //console.log(typeof(data));
    },
    error=>{
      console.log(error);
      
    }
    );
  }
  
  selectedSrc(){
    console.log(this.selectedSource.source);
    console.log(this.selectedSource.price);
    console.log(this.email);
  }
  selectedDest(){
    console.log(this.selectedDestination.destination);
   
  }

  changeEvent(event){
    this.departingDt=event.value;
    console.log(event.value);
    console.log(this.departingDt);
  }
  changeEvent2(event){
    this.returnDt=event.value;
    console.log(event.value);
    console.log(this.returnDt);
  }
  pay(value:number){
    console.log(this.selectedSource.source);
    console.log(this.selectedDestination.destination);
    console.log(this.selectedDestination.price);
    this.ticketPrice=this.selectedDestination.price;
    console.log(this.departingDt);
    console.log(this.returnDt);


    this.creditCard=value;
    console.log(this.creditCard);

    const transaction={'paymentMethod':'creditcata','public_id':this.user_id,'cardDetails':this.creditCard};
    this.ticketService.payment(transaction).subscribe(data=>{

      this.transaction_id=data.transactionId;
      console.log(this.transaction_id);
      window.alert("Payment Done succesfully");
      console.log(this.ticketPrice);
      const booked_ticket={'ticketPrice':this.ticketPrice,'departing':this.selectedSource.source,'returning':this.selectedDestination.destination,
      'email':this.email,
      'packageId':this.selectedDestination.packageId,
      'bookingUserId':this.user_id,
      'transactionId':this.transaction_id
    
    }
    this.ticketService.bookTicket(booked_ticket).subscribe(data=>{
      if(data!=null){

      this.router.navigate(['viewicket',data.ticketId]);
      }
      else{
        window.alert('Please book again!!')
      }
  
    });
     
    });


  
  }
  






}
