import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, map ,filter, switchMap,tap } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isLoggedin: boolean;
  isFromBookTicket:boolean;
  
    endpoint: string='http://100.26.195.40:82';
  //endpoint: string='http://54.162.179.234:5001';
  constructor(private http: HttpClient,
    ) { }
    
  login(data): Observable<any>{
   return this.http.post(this.endpoint+'/auth/login',data)
}
    register(data): Observable<any>{
    return this.http.post(this.endpoint+'/user/',data)
 }

 loginSecond(data): Observable<any>{
    return this.http.post(this.endpoint+'/auth/loginSecond',data)
 }

 
 validate():Observable<any>{
   
  const jwt=sessionStorage.getItem('jwt');
  console.log(jwt);
   return this.http.get(this.endpoint+'/auth/validate',{ headers: new HttpHeaders({'Authorization': 'jwt '+ jwt})
  });
 }
  
}
