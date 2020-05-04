import { Component, OnInit } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../authentication.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  registrationForm:FormGroup;
  onInit;
  constructor(private route: Router,private authService:AuthService) { }
  password: String;
  ngOnInit() {
    this.onInit = false;
    this.registrationForm = new FormGroup({
      'firstName': new FormControl('', { validators: [Validators.required, Validators.minLength(2), Validators.maxLength(30)] }),
      'lastName': new FormControl('', { validators: [Validators.required, , Validators.minLength(2), Validators.maxLength(30)] }),
      'email': new FormControl('', { validators: [Validators.required] }),
      'password': new FormControl('', { validators: [Validators.required, Validators.minLength(6), Validators.maxLength(20)] }),
      'phoneNo': new FormControl('', { validators: [Validators.required] }),
      'gender': new FormControl('', { validators: [Validators.required] }),
    })
  }

  onSubmit() {
   
  }

  register() {
    if(this.registrationForm.invalid){
      this.onInit = true;
    }else{    
      // let body ={
      //   'email':this.registrationForm.get('username').value,
      //   'password':this.registrationForm.get('password').value
      // }
      //this.registrationForm.value
      this.authService.register(this.registrationForm.value).subscribe(data=>{
        console.log(data)
        this.route.navigate(["", "login"]);
        //sessionStorage.setItem('jwt',data.Authorization)

      })
      //this.route.navigate(["", "homepage"]);
  }
  }


}
