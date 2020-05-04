import { Component, OnInit ,Input} from '@angular/core';
import { TouristItem } from './../models/touristplace.model';

@Component({
  selector: 'app-tourist-item',
  templateUrl: './tourist-item.component.html',
  styleUrls: ['./tourist-item.component.css']
})
export class TouristItemComponent implements OnInit {
  @Input()
  recipePageItem: TouristItem;
  constructor() { }

  ngOnInit() {
  }

}
