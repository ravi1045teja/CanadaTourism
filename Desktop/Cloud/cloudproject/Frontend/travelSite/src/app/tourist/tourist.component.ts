import { TourService } from './../tour.service';
import { TouristItem } from './../models/touristplace.model';
import { Component, OnInit ,Input} from '@angular/core';




@Component({
  selector: 'app-tourist',
  templateUrl: './tourist.component.html',
  styleUrls: ['./tourist.component.css']
})
export class TouristComponent implements OnInit {
  @Input()
  private tours:any=[]
  recipePageSections = [{
    recipes: [
        
        new TouristItem('../../assets/pleasent.png','1','point pleasent','halifx','nice breeze','parks'),
        new TouristItem('../../assets/pleasent.png','1','point pleasent','halifx','nice breeze','parks'),
        new TouristItem('../../assets/pleasent.png','1','point pleasent','halifx','nice breeze','parks'),
        new TouristItem('../../assets/pleasent.png','1','point pleasent','halifx','nice breeze','parks')
      ]
    }];
  constructor(private tourService:TourService) { }

  ngOnInit() {
  //this.tourService.getTouristDestinations().subscribe(
    //(data)=>{
      //this.tours=data;
    //}
  //);
  //console.log(this.tours);
  }
  
  

}
