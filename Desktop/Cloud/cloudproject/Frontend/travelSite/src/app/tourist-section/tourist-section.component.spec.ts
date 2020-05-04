import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TouristSectionComponent } from './tourist-section.component';

describe('TouristSectionComponent', () => {
  let component: TouristSectionComponent;
  let fixture: ComponentFixture<TouristSectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TouristSectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TouristSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
