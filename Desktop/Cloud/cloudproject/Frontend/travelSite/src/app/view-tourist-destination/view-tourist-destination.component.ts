import { AuthService } from './../authentication.service';
import { TourService } from './../tour.service';
import { Component, OnInit } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { ActivatedRoute, ParamMap ,Router} from '@angular/router';



@Component({
  selector: 'app-view-tourist-destination',
  templateUrl: './view-tourist-destination.component.html',
  styleUrls: ['./view-tourist-destination.component.css']
})
export class ViewTouristDestinationComponent implements OnInit {

  id:any;
  tour:any;
  constructor(private route:ActivatedRoute,
    private  tourService:TourService,
    private router:Router,
    private authService:AuthService
    ) { }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      console.log(params.get('tour.id'));
      this.id = params.get('tour.id');
      this.tourService.getDestination(this.id).subscribe(data=>{
        this.tour=data;
        console.log(data);
      })
    });
  }
  book(){
    this.authService.isFromBookTicket=true;
    let destination=this.tour.location;
    console.log(destination);
    this.tourService.destination=this.tour.location;
    this.router.navigate(['/book-ticket',destination]);
  }

}
