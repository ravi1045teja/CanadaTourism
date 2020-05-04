import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TouristItemComponent } from './tourist-item.component';

describe('TouristItemComponent', () => {
  let component: TouristItemComponent;
  let fixture: ComponentFixture<TouristItemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TouristItemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TouristItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
