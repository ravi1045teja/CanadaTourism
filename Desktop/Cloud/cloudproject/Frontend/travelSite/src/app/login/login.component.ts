import { Component, OnInit } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../authentication.service';
import { MatSnackBar } from '@angular/material';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  onInit;
  loginForm: FormGroup;
  constructor(private route: Router,private authService:AuthService,private _snackBar: MatSnackBar) {
    this.loginForm = new FormGroup({
      username: new FormControl('', { validators: [Validators.required,Validators.maxLength(30)] }),
      password: new FormControl('', { validators: [Validators.required, Validators.minLength(6), Validators.maxLength(20)] })
    })
   }

  ngOnInit() {
    this.onInit = false;
   
  }
  onSubmit() {

  }

  onRegister() {
    this.route.navigate(["", "register"]);

  }

  onLogin() {
    if (this.loginForm.invalid) {
      this.onInit = true;

    }
    else {

      let body ={
        'email':this.loginForm.get('username').value,
        'password':this.loginForm.get('password').value
      }

      this.authService.login(body).subscribe(data=>{
        console.log(data)
        if(data.status == "success"){
          //added to check if the user logged in for auth guard purpose
          this.authService.isLoggedin=true;
          this.route.navigate(["/otp",this.loginForm.get('username').value]);
        }else{
          this._snackBar.open(data.message, "Please retry", {
            duration: 1500,
            
          });
          this.authService.isLoggedin=false;
        }
        //sessionStorage.setItem('jwt',data.Authorization)

      })

      if (this.loginForm.get('username').value == 'admin@gmail.com') {
       // this.route.navigate(["", "adminHome"]);

      }
      else {
        //this.route.navigate(["", "homepage"]);
      }

    }
  }
}
