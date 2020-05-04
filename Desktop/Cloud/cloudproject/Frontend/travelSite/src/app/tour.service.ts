import { TouristItem } from './models/touristplace.model';
import { tours } from './models/touritstItems';
import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, map ,filter, switchMap,tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class TourService {
  destination:any;
  endpoint: string='http://52.90.211.209:81/';
  constructor(private http: HttpClient,
    ) { }

  getTouristDestinations(): Observable<TouristItem[]>{
   return this.http.get<TouristItem[]>('http://52.90.211.209:81/location/').pipe(
     map(data=>{return data['data']})
   );
    }

    getDestination(id){
      return this.http.get('http://52.90.211.209:81/location/'+id);
      
    }
  

  
}
