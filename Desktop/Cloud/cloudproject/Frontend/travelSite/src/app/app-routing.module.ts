import { ViewTicketComponent } from './view-ticket/view-ticket.component';
import { BookTicketComponent } from './book-ticket/book-ticket.component';
import { AuthGuard } from './auth.guard';
import { ViewTouristDestinationComponent } from './view-tourist-destination/view-tourist-destination.component';
import { HomePageComponent } from './home-page/home-page.component';
import { TouristComponent } from './tourist/tourist.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { OtpManComponent } from './otp-man/otp-man.component';








const routes: Routes = [{ path: '', component: HomePageComponent, pathMatch: 'full'},
{path: 'homepage', component: HomePageComponent, pathMatch: 'full'},
{path:'viewDestination/:tour.id',component:ViewTouristDestinationComponent},
{path:'login',component:LoginComponent},
{path:'register',component:RegistrationComponent},
{path:'otp/:id',component:OtpManComponent},
{path:'book-ticket/:destination',component:BookTicketComponent,canActivate:[AuthGuard]},
{path:'viewicket/:userId',component:ViewTicketComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
