import { TicketService } from './../ticket.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap ,Router} from '@angular/router';


@Component({
  selector: 'app-view-ticket',
  templateUrl: './view-ticket.component.html',
  styleUrls: ['./view-ticket.component.scss']
})
export class ViewTicketComponent implements OnInit {
  userId:any;
  ticket:any;
  constructor(private route:ActivatedRoute,
    private router:Router,
    private ticketService:TicketService

  ) { }

  ngOnInit() {
    this.route.paramMap.subscribe(params=>{
      console.log(params.get('userId'));
      this.userId=params.get('userId');

      this.ticketService.getTickets(this.userId).subscribe(data=>{
        console.log(data);
        this.ticket=data;
      })
    })
  }

}
