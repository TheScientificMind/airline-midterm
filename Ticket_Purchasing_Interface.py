import sqlib

con= sqlib.create_db_connection ("127.0.0.1", "credmond", "credmond1", "flights")



class booking_entry:
    Name = None
    Phone_number = None
    Email = None
    Confirmation_Code = None
    class Ticket:
        Airport_Code = None
        Date = None
        Price = None
        Time =  None
    


    