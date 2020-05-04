import { FilterPipe } from './filter.pipe';
import { MaterialModule } from './material/material.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule,HttpClient } from '@angular/common/http';

import { FormsModule,ReactiveFormsModule } from '@angular/forms';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavigationBarComponent } from './navigation-bar/navigation-bar.component';
import { HomePageComponent } from './home-page/home-page.component';
import { TouristItemComponent } from './tourist-item/tourist-item.component';
import { TouristSectionComponent } from './tourist-section/tourist-section.component';
import { TouristComponent } from './tourist/tourist.component';
import { ViewTouristDestinationComponent } from './view-tourist-destination/view-tourist-destination.component';
import { BookTicketComponent } from './book-ticket/book-ticket.component';
import { LoginComponent } from './login/login.component';
import { AuthService } from './authentication.service';
import { RegistrationComponent } from './registration/registration.component';
import { OtpManComponent } from './otp-man/otp-man.component';
import { MyBookingsComponent } from './my-bookings/my-bookings.component';
import { ViewTicketComponent } from './view-ticket/view-ticket.component';

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    HomePageComponent,
    TouristItemComponent,
    TouristSectionComponent,
    TouristComponent,
    FilterPipe,
    ViewTouristDestinationComponent,
    BookTicketComponent,
    LoginComponent,
    RegistrationComponent,
    OtpManComponent,
    MyBookingsComponent,
    ViewTicketComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
