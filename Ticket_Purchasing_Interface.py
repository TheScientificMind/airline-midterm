import sqlib
import random
from datetime import time, date, datetime
con = sqlib.create_db_connection ("127.0.0.1", "credmond", "credmond1", "airline")

class booking_entry:
      fName = None
      lname = None
      Phone_number = None
      Email = None
   
      def __init__ (self, fname, lname, Phone_Number, Email):
         self.fname = fname
         self.lname = lname
         self.Phone_Number = Phone_Number
         self.Email = Email 

class Ticket:
   flightid = None
   Departure_Airport = None
   Arrival_Airport = None
   Datetime = None
   Price = None
   Aircraft = None
   Confirmation_Code = None

   def __init__(self, FlightID, Airport_Code1,Airport_Code2, Datetime, Price, Aircraft, Confirmation_Code):
      self.flightid = FlightID
      self.Departure_Airport = Airport_Code1
      self.Arrival_Airport = Airport_Code2
      self.Datetime = Datetime
      self.Price = Price
      self.Aircraft= Aircraft
      self.Confirmation_Code = Confirmation_Code

def Buy_Ticket (tickets_purchased, returns): #overall function to buy tickets
   bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))

   print (bookingentry.fname, bookingentry.lname, bookingentry.Phone_Number, bookingentry.Email)

   bookingcheck = input("Is this the correct booking entry:")

   #creates booking entry object and asks if this information entered is correct
   for x in range (int(returns)+1):
      def Purchase(Airport1, Airport2): #function all code is in to make things easier
          theflight = []
          sflights =[]
          squery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}' """.format(Origin=Airport1, Destination=Airport2)
          flights = (sqlib.read_query(con,squery))

          for x in flights:
             x = list(x)
             sflights.append(x)
          i = (len(sflights))

          for w in range ((0), (i)):
             sflights[w][3] = datetime.strftime(sflights[w][3], "%y-%m-%d %H:%M:%S")
             print (sflights[w])

          #finds flights between two airports purchased, and lists them to the purchaser
          ID = input("Enter Id of Flight you wish to purchase tickets for:")
          uquery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}' AND ID='{ID}' """.format(Origin=Airport1, Destination=Airport2, ID=ID)
          flight = sqlib.read_query(con,uquery)

          for x in flight:
             x = list(x)
             theflight.append(x)

          #finds flight from db that purchaser chose (by inputing the ID from the list)

          # This function checks if there is space avalible for the tickets the user is trying to buy (annie created this code)
   
          def ticket_checking(flight_id):
                  from_db=[]
                  qt = """select * from flights where id='{flight_id}';""".format(flight_id = flight_id)
                  query_results = sqlib.read_query(con,qt)
                  for x in query_results:
                     x = list(x)
                     from_db.append(x)
                  aircraft = from_db[0][5]
                  tickets = (int(from_db[0][6]) + int(tickets_purchased))

                  aircraft_search = """select * from capacity where aircraft ='{aircraft}';""".format(aircraft=aircraft)
                  search_results = sqlib.read_query(con,aircraft_search)
                  seats = (search_results[0][1])

                  if tickets > seats:
                     if  input("I'm sorry but your requested flight is full. Press 1 if you would like to book another flight. Press 2 if you would like to end.") == "1":
                        Purchase(input("please enter origin airport:"), input("please enter destination airport:"))
                     
                     else:
                        print("Goodbye!")
                  else:
                     #creates ticket function which will create a ticket object and print the ticket info out to the purchaser
                     def Create_Ticket (j, x, y, c, a, f, g):
                        ticket = Ticket(j, x, y, c, a , f, g)
                        print(ticket.flightid,ticket.Departure_Airport,ticket.Arrival_Airport, ticket.Datetime, ticket.Price, ticket.Aircraft, ticket.Confirmation_Code)
                        cquery = """INSERT INTO bookings (fname, lname, email, phone, flight_id,booking_price, purchase_date, ticket_amount, return_flights, confirmation_code, aircraft_type) 
                        VALUES ('{fnam}','{lnam}','{theemail}','{phonen}','{idflight}','{pricen}','{thedated}','{amountn}','{returned}','{coded}','{typeofplane}') 
                        """.format(fnam=bookingentry.fname, lnam=bookingentry.lname,theemail=bookingentry.Email, phonen=bookingentry.Phone_Number,idflight=ticket.flightid,
                        pricen=ticket.Price,thedated=ticket.Datetime, amountn=tickets_purchased, returned=int(returns), coded=ticket.Confirmation_Code, typeofplane=ticket.Aircraft )
                        #inputs data into bookings table, /return flights
                        g= sqlib.execute_query(con,cquery)

                     R = str(random.randint(10000000, 99999999)) #creates random confirmation code
                     
                     #creates ticket using info about flight form db
                     Create_Ticket(str(theflight[0][0]),str(theflight [0][1]), str(theflight [0][2]), str(theflight [0][3]), str(theflight [0][4]), str(theflight [0][5]), R)
         
                     tt = """select ID,seats_booked from flights where ID='{id}';""".format(id=ID)
                     ticket_checker = sqlib.read_query(con,tt)
                     tt_db = []

                     for y in ticket_checker:
                        y = list(y)
                     tt_db.append(y)
                     tickets = tt_db[0][1]

                     total = int(tickets_purchased) + tickets
                     iquery = "UPDATE flights SET seats_booked='{x}' WHERE  ID='{ID}' ".format(x=total, ID=ID)
      
                     #changes seats_booked column in db to the current amount of tickets after purchase
                     c = sqlib.execute_query(con,iquery)
          ticket_checking(ID)
         
      if bookingcheck == "yes": 
         Purchase(input("please enter origin airport:"), input("please enter destination airport:"))
      elif bookingcheck =="no":
         bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))
         Purchase(input("please enter origin airport:"), input("please enter destination airport:"))
      else:
         print ("please enter yes or no, rerun command")
     

Buy_Ticket(input("How many tickets do you want to buy:"), input("how many return flights will this have:"))