import { Router } from '@angular/router';
import { TourService } from './../tour.service';
import { TouristItem } from './../models/touristplace.model';
import { Component, OnInit } from '@angular/core';
import {tours} from '../models/touritstItems';


@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {
  tours:Array<TouristItem>;
  constructor(private tourservice:TourService,
    private router:Router
    ) { }

  ngOnInit() {
    //this.tourservice.getTouristDestinations();
    //this.tours=this.tourservice.getTours();
    this.retrieveTours();
  }

  retrieveTours(){
    this.tourservice.getTouristDestinations().subscribe(data=>{
      this.tours=data;
      console.log(data);
    },
    error=>{
      console.log(error);
      
    }
    );
  }

  /* navigate(){
    this.router.navigate(['/viewDestination',])
  } */

}
