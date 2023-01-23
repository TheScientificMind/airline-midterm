import sqlib
import random
from datetime import time, date, datetime
from tabulate import tabulate
con= sqlib.create_db_connection ("127.0.0.1", "credmond", "credmond1", "airline")

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
   flightid=  None
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
def Buy_Ticket (tickets_purchased):
   bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))
   print (bookingentry.fname, bookingentry.lname, bookingentry.Phone_Number, bookingentry.Email)
   y = input("Is this the correct booking entry:")
   def thing_a_majig(Airport1, Airport2):
         theflight = []
         sflights =[]
         amountofbookings =[]
         squery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}'""".format(Origin=Airport1, Destination=Airport2)
         flights = (sqlib.read_query(con,squery))
         for x in flights:
            x = list(x)
            sflights.append(x)
         i = (len(sflights))
         for w in range ((0), (i)):
            sflights[w][3] = datetime.strftime(sflights[w][3], "%y-%m-%d %H:%M:%S")
            print (sflights[w])
         
         ID = input("Enter Id of Flight you wish to purchase tickets for:")
         uquery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}' AND ID ='{ID}'""".format(Origin=Airport1, Destination=Airport2, ID=ID)
         flight = sqlib.read_query(con,uquery)
         for x in flight:
            x = list(x)
            theflight.append(x)
         def Create_Ticket (j,x, y, c, a, f, g):
            ticket = Ticket(j,x, y, c, "$"+ a ,f, g )
            print(ticket.flightid,ticket.Departure_Airport,ticket.Arrival_Airport, ticket.Datetime, ticket.Price, ticket.Aircraft, ticket.Confirmation_Code)
            bquery = "SELECT * FROM Bookings"
            v = sqlib.read_query(con, bquery)
            for x in v:
               x =list(x)
               amountofbookings.append(x)
            A = (len(amountofbookings))
            cquery = """INSERT INTO Bookings (booking_id, fname, lname , email, phone, flight_id,booking_price, purchase_date, ticket_amount, return_flights, confirmation_code, aircraft_type) 
            VALUES ({bID},{fnam},{lnam},{theemail},{phonen},{idflight},{pricen},{thedated},{amountn},{returned},{coded},{typeofplane}) 
            """.format(bID=A, fnam=bookingentry.fname, lnam=bookingentry.lname,theemail=bookingentry.Email, phonen=bookingentry.Phone_Number,idflight=ticket.flightid,
             pricen=ticket.Price,thedated=ticket.Datetime, amountn=tickets_purchased, returned=Z, coded=ticket.Confirmation_Code, typeofplane=ticket.Aircraft )
            #inputs data into bookings table, /return flights
            #g= sqlib.execute_query(con,cquery)
         for u in range(int(tickets_purchased)):
            R = str(random.randint(10000000, 99999999))
            Create_Ticket(str(theflight[0][0]),str(theflight [0][1]), str(theflight [0][2]), str(theflight [0][3]), str(theflight [0][4]), str(theflight [0][5]), R)
         iquery = "INSERT INTO flights (seats_booked) VALUES ('{x}') WHERE  ID ='{ID} ".format(x=tickets_purchased, ID=ID)
         c = sqlib.execute_query(con,iquery)
         #adds seats_booked to ticket
        
   if y == "yes": 
      thing_a_majig(input("please enter origin airport:"), input("please enter destination airport:"))
   elif y =="no":
      bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))
      thing_a_majig(input("please enter origin airport:"), input("please enter destination airport:"))
Buy_Ticket(input("How many tickets do you want to buy:"))

   
   
      
   



    