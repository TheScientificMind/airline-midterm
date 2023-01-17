import sqlib

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
         Airport_Code = None
         Date = None
         Price = None
         Time =  None
         Confirmation_Code = None
         def __init__(self, Airport_Code, Datetime, Price, Confirmation_Code):
            self.Airport_Code = Airport_Code
            self.Date = Datetime
            self.Price = Price
            self.Confirmation_Code = Confirmation_Code
def Buy_Ticket (X):
   booking_entry1 = booking_entry(input("First name:"),input("Last name:", input("Phone number:",input("Email:"))))
   print (booking_entry1)
   y = input("Is this the correct booking entry:")
   if y == "yes":
      Airport1 = input("please enter origin airport:")
      Airport2 = input("please enter destination airport:")
      squery = """SELECT * FROM flights WHERE origin='{Origin}' and destination='{Destination}'""".format(Origin=Airport1, Destination=Airport2)
      flight_list = sqlib.read_query(con,squery)
      print(flight_list)
      ID = input(int("Enter Id of Flight you wish to purchase tickets for:")
      uquery = """SELECT * FROM flights WHERE origin='{Origin}' and destination='{Destination}'""".format(Origin=Airport1, Destination=Airport2)
      
   elif y =="no":
       booking_entry1 = booking_entry(input("Enter First name:"),input("EnterLast name:", input("Enter Phone number:",input("Enter Email:"))))
Buy_Ticket(input(int("How many tickets do you want to buy:")))



    