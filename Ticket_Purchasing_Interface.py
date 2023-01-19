import sqlib
import random
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
   Departure_Airport = None
   Arrival_Airport = None
   Datetime = None
   Price = None
   Aircraft = None
   Confirmation_Code = None
   def __init__(self, Airport_Code1,Airport_Code2, Datetime, Price, Aircraft, Confirmation_Code):
      self.Departure_Airport = Airport_Code1
      self.Arrival_Airport = Airport_Code2
      self.Datetime = Datetime
      self.Price = Price
      self.Aircraft= Aircraft
      self.Confirmation_Code = Confirmation_Code
def Buy_Ticket (X):
   bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))
   print (bookingentry.fname, bookingentry.lname, bookingentry.Phone_Number, bookingentry.Email)
   y = input("Is this the correct booking entry:")
   if y == "yes":
      theflight = []
      Airport1 = input("please enter origin airport:")
      Airport2 = input("please enter destination airport:")
      squery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}'""".format(Origin=Airport1, Destination=Airport2)
      q = sqlib.execute_query(con,squery)
      ID = input("Enter Id of Flight you wish to purchase tickets for:")
      uquery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}' ID ='{ID}' AND""".format(Origin=Airport1, Destination=Airport2, ID=ID)
      flight = sqlib.read_query(con,uquery)
      for x in flight:
         x = list(x)
         theflight.append(x)
      for u in range(X):
         R = random.randint(10000000, 99999999)
         Create_Ticket(theflight [0][2], theflight [0][3], theflight [0][4], theflight [0][5], theflight [0][6], R)
   elif y =="no":
       bookingholder = booking_entry(input("Enter First name:"),input("Enter Last name:", input("Enter Phone number:",input("Enter Email:"))))
       y == "yes"
Buy_Ticket(input("How many tickets do you want to buy:"))
def Create_Ticket (x, y, c, a, f, g):
   ticket = Ticket(x, y, c, "$"+ a ,f, g )
   print(ticket.Departure_Airport,ticket.Arrival_Airport, ticket.Datetime, ticket.Price, ticket.Aircraft, ticket.Confirmation_Code)
   
   
      
   




