import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OtpManComponent } from './otp-man.component';

describe('OtpManComponent', () => {
  let component: OtpManComponent;
  let fixture: ComponentFixture<OtpManComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OtpManComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OtpManComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
