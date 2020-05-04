import { AuthService } from './../authentication.service';
import { Component, OnInit,Input } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-navigation-bar',
  templateUrl: './navigation-bar.component.html',
  styleUrls: ['./navigation-bar.component.css']
})
export class NavigationBarComponent implements OnInit {
  @Input()  logged: string;
  loginShow = true;
  constructor(private route:Router,
    private authService:AuthService) {
    
   }
  
   onLogin(comp){
    if(comp.logged){
      comp.logged.subscribe(data=>{
        console.log("logged in")
        this.loginShow = false;
      });
      
    }
  }
  homepage(){
    this.loginShow = true;
    this.authService.isLoggedin=false;
    this.route.navigate(["/","homepage"]);

  }
  myBooking(){
    
  }

  

  ngOnInit() {
    this.route.navigate(["/","homepage"]);
  }

  login(){
    this.route.navigate(["/","login"]);
  }
  navigate(){
    this.route.navigate(["/","homepage"]);
  }
}
