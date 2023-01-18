import sqlib
import random
con= sqlib.create_db_connection ("127.0.0.1", "credmond", "credmond1", "flights")

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
   Date = None
   Price = None
   Time =  None
   Confirmation_Code = None
   def __init__(self, Airport_Code1,Airport_Code2, Datetime, Price, Confirmation_Code):
      self.Departure_Airport = Airport_Code1
      self.Arrival_Airport = Airport_Code2
      self.Date = Datetime
      self.Price = Price
      self.Confirmation_Code = Confirmation_Code
def Buy_Ticket (X):
   booking_entry1 = booking_entry(input("First name:"),input("Last name:", input("Phone number:",input("Email:"))))
   print (booking_entry1)
   y = input("Is this the correct booking entry:")
   if y == "yes":
      theflight = []
      flight_list = []
      Airport1 = input("please enter origin airport:")
      Airport2 = input("please enter destination airport:")
      squery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}'""".format(Origin=Airport1, Destination=Airport2)
      qresults = sqlib.read_query(con,squery)
      for x in qresults:
         x = list(x)
         flight_list.append(x)
      print (flight_list)
      iD = input(int("Enter Id of Flight you wish to purchase tickets for:"))
      uquery = """SELECT * FROM flights WHERE origin='{Origin}' AND destination='{Destination}' ID ='{ID}' AND""".format(Origin=Airport1, Destination=Airport2, ID=iD)
      flight = sqlib.read_query(con,uquery)
      for x in flight:
         x = list(x)
         theflight.append(x)
      for u in range(X):
         R = random.randint(10000000, 99999999)
         Create_Ticket(theflight [0][2], theflight [0][3], theflight [0][4], theflight [0][5], R)
   elif y =="no":
       booking_entry1 = booking_entry(input("Enter First name:"),input("Enter Last name:", input("Enter Phone number:",input("Enter Email:"))))
Buy_Ticket(input(int("How many tickets do you want to buy:")))
def Create_Ticket (x, y, c, a, g):
   Theticket = []
   ticket_holder = Ticket(x, y, c, a ,g )
   print(ticket_holder)
   for x in ticket_holder:
      x = list (x)
      Theticket.append(x)
   
      
   



    