import { TouristItem } from './models/touristplace.model';
import { Pipe, PipeTransform } from '@angular/core';
import {tours} from './models/touritstItems'
const { isArray } = Array;

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(tours: TouristItem[], find: string): TouristItem[] {
    if(!tours) return [];
    if(!find) return tours;
    find = find.toLowerCase();
    return search( tours, find);
   }
}
function search(entries: any[], search: string) {

  search = search.toLowerCase();

  return entries.filter(function (obj) {
    const keys: string[] = Object.keys(obj);
    return keys.some(function (key) {
      const value = obj[key];
      if (isArray(value)) {
        return value.some(v => {
          return v.toLowerCase().includes(search);
        });
      }
      else if (!isArray(value)) {
        return value.toLowerCase().includes(search);
      }
    })
  });

}
