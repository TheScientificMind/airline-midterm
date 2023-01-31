import sqlib
import random
<<<<<<< HEAD
import datetime
from datetime import date, time
from back_end import ffmiles
import sys
import send_email
=======
from datetime import time, date, datetime
from annie_back_end import ffmiles
con = sqlib.create_db_connection ("127.0.0.1", "credmond", "credmond1", "airline")
>>>>>>> ba709d4a72b7fbf56e1f373edc44f07ae35bcbf2

con = sqlib.create_db_connection("127.0.0.1", "credmond", "credmond1", "airline")

# overall function to buy tickets
def Buy_Ticket():
   try:   
      # gets customer information

      email = input("What is your email? ")
      already = input("Do you have an account (yes/no)? ").strip().lower()

<<<<<<< HEAD
      if already == "no":
         fname = input("What is your first name? ")
         lname = input("What is your last name? ")
         phone = input("What is your phone number? ")
         password = input("What would you like your password to be? ")
      elif already == "yes":
         password = input("What is your password? ")
         ffq = "SELECT fname, lname, phone, password FROM ffaccounts;"
         read_ff = sqlib.read_query(con, ffq)
         fname = read_ff[0][0]
         lname = read_ff[0][1]
         phone = read_ff[0][2]
         password = read_ff[0][3]
      else:
         sys.exit("You entered an input other than yes/no. Please run the program once more to try again.")
      
      origin = input("What is the code of the airport you would like to fly from (ex: DEL)? ")
      dest = input("What is the code of the airport you would like to fly to (ex: CTU)? ")
      date = input("What day would you like your flight to be on (ex: 2023-01-30)? ")
      ticket_amount = input("How many tickets would you like to buy? ")
      return_tickets = input("How many return tickets would you like to purchase? ")

      select = f"SELECT * FROM flights WHERE origin = '{origin}' AND destination = '{dest}' AND DATE(datetime) = '{date}';"
      read_select = sqlib.read_query(con, select)

      # checks if no flights matched your specifications
      if len(read_select) > 0:
         print(read_select)
      else:
         print("There were no flights that matched your specifications. Please run the program once more to try again.")
         sys.exit()

      flight_id = input("What is the id of the flight you would like to take? ")
      id_select = f"SELECT * FROM flights WHERE id = '{flight_id}'"
      read_id_select = sqlib.read_query(con, select)
      print(read_id_select)

      correct_booking = input("Is this the flight you would like to book (yes/no)? ").strip().lower()

      capacity_query = f"SELECT seats FROM capacity WHERE aircraft = '{read_id_select[0][5]}';"
      capacity = sqlib.read_query(con, capacity_query)[0][0]

      seatfill_query = f"""
      SELECT seats_booked FROM flights WHERE flights.id = '{flight_id}';
      """
      seatfill = sqlib.read_query(con, seatfill_query)[0][0]

      # checks if you have the correct booking and that you haven't exceed flight capacity
      if correct_booking == "yes" and (seatfill + int(ticket_amount)) < capacity:
         price_query = f"SELECT price FROM flights WHERE flights.id = '{flight_id}';"

         price = sqlib.read_query(con, price_query)[0][0]
         ffmiles = ((int(ticket_amount) + int(return_tickets)) * price)/10

         # inserts values into the tables based on the customers previous answers
      
         if already == "no":   
            insert_ff = f"""
            INSERT INTO ffaccounts (email, fname, lname, phone, password, ffmiles) 
            VALUES ('{email}', '{fname}', '{lname}', '{phone}', '{password}', '{ffmiles}')
            """
            print("Created your ffaccount.")

            ff = sqlib.execute_query(con, insert_ff)
         elif already == "yes":
            update_ff = f"UPDATE ffaccounts SET ffmiles = ffmiles + {ffmiles} WHERE email = '{email}';"

            up = sqlib.execute_query(con, update_ff)
         
         code = str(random.randint(1000000, 9999999))
         today = datetime.date.today()

         insert_books = f"""
         INSERT INTO bookings (email, flight_id, purchase_date, ticket_amount, 
         return_flights, confirmation_code, aircraft_type)
         VALUES ('{email}', '{flight_id}', '{today}', '{ticket_amount}', 
         '{return_tickets}', '{code}', '{read_id_select[0][5]}');
         """

         books = sqlib.execute_query(con, insert_books)

         # updates the database so it accurately reflects the number of seats taken
         update_seats = f"""
         UPDATE flights INNER JOIN bookings ON flights.id = bookings.flight_id 
         SET seats_booked = seats_booked + {ticket_amount} WHERE bookings.email = '{email}';
         """

         us = sqlib.execute_query(con, update_seats)

         # acts if you are going to take any return flights
         if int(return_tickets) > 0:
            return_code = str(random.randint(1000000, 9999999))

            count_query = """
            SELECT COUNT(booking_id) FROM bookings;
            """
            booking_id = sqlib.read_query(con, count_query)[0][0]

            insert_return = f"""
            INSERT INTO return_flights (booking_id, return_code, return_checked_in)
            VALUES ('{booking_id}', '{return_code}', 'no')
            """

            return_ins = sqlib.execute_query(con, insert_return)
      
         # sends an email to the specified email adress with given data
         send_email.sendEmail(email, code, origin, dest, str(read_id_select[0][3].date()), str(read_id_select[0][3].time()), read_id_select[0][5], capacity, fname + " " + lname, str((int(ticket_amount) + int(return_tickets)) * price))

      elif correct_booking == "no":
         print("Please rerun the program and choose the correct booking.")
      else:
         print("You entered an invalid input. Please rerun the program to try again.")

   except Exception as err:
      print(f"You entered an invalid input that produced this error:\n\n{err}\n\nPlease rerun the program to try again.")

if __name__ == "__main__":
   Buy_Ticket()
=======
def Buy_Ticket (tickets_purchased, returns): #overall function to buy tickets
  for x in range (int(returns)+1):
      already = input("do you already have a bookingentry account:")
      if already == "yes":
         bookingen = []
         bookingemail = input("input your bookings email:")
         vquery = "Select fname, lname, email, phone From Bookings Where ID={email}".format(email=bookingemail)
         d = sqlib.read_query(con, vquery)
         for x in d:
            x = list(x)
            bookingen.append(x)
            bookingentry =booking_entry(bookingen[0][1], bookingen[0][2], bookingen[0][3], bookingen [0][4], bookingen [0][5])
      
      if already == "no":
         bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))

      print (bookingentry.fname, bookingentry.lname, bookingentry.Phone_Number, bookingentry.Email)

      bookingcheck = input("Is this the correct booking entry account:")

   #creates booking entry object and asks if this information entered is correct
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
                        VALUES ('{fnam}','{lnam}','{theemail}','{phonen}','{idflight}','{thedated}','{amountn}','{returned}','{coded}','{typeofplane}') 
                        """.format(fnam=bookingentry.fname, lnam=bookingentry.lname,theemail=bookingentry.Email, phonen=bookingentry.Phone_Number,idflight=ticket.flightid,
                       thedated=ticket.Datetime, amountn=tickets_purchased, returned=int(returns), coded=ticket.Confirmation_Code, typeofplane=ticket.Aircraft )
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
          ffmiles(bookingentry.Email)
         
      if bookingcheck == "yes": 
         Purchase(input("please enter origin airport:"), input("please enter destination airport:"))
      elif bookingcheck =="no":
         bookingentry = booking_entry(input("First name:"),input("Last name:"), input("Phone number:"),input("Email:"))
         Purchase(input("please enter origin airport:"), input("please enter destination airport:"))
      else:
         print ("please enter yes or no, rerun command")
     
Buy_Ticket(input("How many tickets do you want to buy:"), input("how many return flights will this have:"))
>>>>>>> ba709d4a72b7fbf56e1f373edc44f07ae35bcbf2
