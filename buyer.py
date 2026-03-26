# Buyer.py

from datetime import datetime
import sys
while True:
  # read the number of available tickets
  tickets = open("/mnt/shared-data/Tickets.db", "r")
  available_tickets = tickets.read()
  num_tickets = int(available_tickets)
  tickets.close()
  if (num_tickets > 0):
    # update the number of available tickets
    tickets = open("/mnt/shared-data/Tickets.db", "w")
    new_num_tickets = num_tickets - 1
    tickets.write(str(new_num_tickets))
    tickets.close()
    # record the sales time
    sales = open("/mnt/shared-data/Sales.log", "a")
    ticket_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sales.write(ticket_time + "\n")
    sales.close
    print(new_num_tickets,"tickets available!")
  else:
    print("no more tickets are available!")
    sys.exit(0)