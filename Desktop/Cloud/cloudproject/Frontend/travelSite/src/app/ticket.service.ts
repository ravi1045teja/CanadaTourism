import { Injectable } from '@angular/core';
import {Package} from './models/package';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, map ,filter, switchMap,tap } from 'rxjs/operators';
import {Ticket} from './TicketItem';

@Injectable({
  providedIn: 'root'
})
export class TicketService {
  email:any;
  constructor(private http: HttpClient,
    ) { }


    getPackages(destination){
      return this.http.get('http://52.90.211.209:81/package/'+destination);
     
 
    }
    bookTicket(data): Observable<any>{
      const jwt=sessionStorage.getItem('jwt');

      return this.http.post('http://52.90.211.209:81/ticket/',data,
      { headers: new HttpHeaders({'Authorization': 'jwt '+ jwt})
      });
    }
    payment(data):Observable<any>{
      const jwt=sessionStorage.getItem('jwt');

      return this.http.post('http://52.90.211.209:81/payment/',data,
      
      { headers: new HttpHeaders({'Authorization': 'jwt '+ jwt})
      });
    }
    getTickets(userId):Observable<Ticket[]>{
      return this.http.get<Ticket[]>('http://52.90.211.209:81/ticket/'+userId);

    }

}
