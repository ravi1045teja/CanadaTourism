import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewTouristDestinationComponent } from './view-tourist-destination.component';

describe('ViewTouristDestinationComponent', () => {
  let component: ViewTouristDestinationComponent;
  let fixture: ComponentFixture<ViewTouristDestinationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewTouristDestinationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewTouristDestinationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
