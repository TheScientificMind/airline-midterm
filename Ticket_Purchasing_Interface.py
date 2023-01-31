import sqlib
import random
import datetime
from datetime import date, time
from back_end import ffmiles
import sys
import send_email

con = sqlib.create_db_connection("127.0.0.1", "credmond", "credmond1", "airline")

# overall function to buy tickets
def Buy_Ticket():
   try:   
      # gets customer information

      email = input("What is your email? ")
      already = input("Do you have an account (yes/no)? ").strip().lower()

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