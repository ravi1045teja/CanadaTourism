import { TicketService } from './../ticket.service';
import { TourService } from './../tour.service';
import { Component, OnInit,Output,EventEmitter } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../authentication.service';
import { MatSnackBar } from '@angular/material';
import {ActivatedRoute} from "@angular/router";



@Component({
  selector: 'app-otp-man',
  templateUrl: './otp-man.component.html',
  styleUrls: ['./otp-man.component.css']
})
export class OtpManComponent implements OnInit {

  @Output() logged: EventEmitter<any> = new EventEmitter();
  onInit;
  email;
  loginForm: FormGroup;
  constructor(private route: Router,private authService:AuthService,private router: ActivatedRoute,private _snackBar: MatSnackBar,private tourService:TourService,private ticketService:TicketService) {
    this.router.params.subscribe( params => {
      console.log(params)
      this.email=params.id} );
      
    this.loginForm = new FormGroup({
      otp: new FormControl('', { validators: [Validators.required,Validators.minLength(4)] }),
     })
   }

  ngOnInit() {
    this.onInit = false;
   
  }
  onSubmit() {

  }

  onRegister() {
    this.route.navigate(["","register"]);

  }

  onLogin() {
    if (this.loginForm.invalid) {
      this.onInit = true;

    }
    else {

      let body ={
        'email':this.email,
        'password':'',
        'otp':this.loginForm.get('otp').value
      }
      

      this.authService.loginSecond(body).subscribe(data=>{
        console.log(data)
        if(data.status == "success"){
        sessionStorage.setItem('jwt',data.Authorization)
        this.logged.emit("true");
        if(this.authService.isFromBookTicket!=true){
          this.route.navigate(["/", "homepage"]);
        }
        else{
          console.log(this.tourService.destination);
          this.ticketService.email=this.email;
        this.route.navigate(['book-ticket',this.tourService.destination]);
        }
        }else{
          this._snackBar.open(data.message, "Please retry", {
            duration: 1500,
          });
        }
     })

      

    }
  }
}
