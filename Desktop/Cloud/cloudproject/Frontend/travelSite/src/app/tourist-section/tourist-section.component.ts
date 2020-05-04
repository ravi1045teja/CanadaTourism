import { Component, OnInit,Input } from '@angular/core';
import { TouristItem } from './../models/touristplace.model';

@Component({
  selector: 'app-tourist-section',
  templateUrl: './tourist-section.component.html',
  styleUrls: ['./tourist-section.component.css']
})
export class TouristSectionComponent implements OnInit {
  @Input()
  recipePageSection: {
    
    recipes: TouristItem[]
  };
  constructor() { }

  ngOnInit() {
  }

}
