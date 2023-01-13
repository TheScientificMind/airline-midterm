import sqlib

con= sqlib.create_db_connection ("127.0.0.1", "credmond", "credmond1", "flights")

def Buy_ticket (Z):
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
            def __init__(self, Airport_Code, Date, Price, Time, Confirmation_Code):
                self.Airport_Code = Airport_Code
                self.Date = Date
                self.Price = Price
                self.Time = Time
                self.Confirmation_Code = Confirmation_Code
Buy_ticket(input(int("How many tickets do you want to buy:")))



    