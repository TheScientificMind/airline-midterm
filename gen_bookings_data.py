import random
from faker import Faker
from datetime import datetime, timedelta, date
import base64
import secrets
import string
import sqlib
import numpy as np

con = sqlib.create_db_connection("127.0.0.1", "dheadley", "dheadley1", "airline")
fake = Faker()

class Gen_data:
        return_code = None
        return_checked_in = None

        first_name = None
        last_name = None
        email = None
        phone = None
        password = None
        ffmiles = None

        flight_id = None
        purchase_date = None
        ticket_amount = None
        return_flights = None
        confirmation_code = None
        aircraft_type = None
        checked_in = None

        ntr = 10000
        
        # initializes fake values for tables
        def __init__(self):
                self.return_code = str(random.randint(1000000, 9999999))
                self.return_checked_in = np.random.choice(['yes', 'no'], p=[.98, .02])
                
                self.first_name = fake.first_name()
                self.last_name = fake.last_name()

                self.email = fake.unique.free_email()
                self.phone = random.randint(1000000000, 9999999999)
                self.password = fake.password()
                self.ffmiles = random.randint(100, 10000)

                self.flight_id = random.randint(1, 22000)
                self.purchase_date = fake.date_time_between(date.fromisoformat('2022-01-01'), datetime.now() - timedelta(days = 14))
                self.ticket_amount = random.randint(1, 8)
                self.return_flights = random.randint(1, self.ticket_amount)
                self.confirmation_code = str(random.randint(1000000, 9999999))
                self.aircraft_type = sqlib.read_query(con, "SELECT aircraft FROM capacity;")[random.randint(0, 4)][0]
                self.checked_in = np.random.choice(['yes', 'no'], p=[.95, .05])

        # prints the bookings and ffaccounts when the object is printed
        def __str__(self):
                select_bookings = """
                SELECT * FROM bookings;
                """

                select_ff = """
                SELECT * FROM ffaccounts;
                """
                
                # gets all the data from the tables
                query_results = sqlib.read_query(con, select_bookings)
                query_results = sqlib.read_query(con, select_ff)

                return str(query_results)
                
        # inserts ntr rows of data into the tables
        def insert_vals(self):
                for i in range(self.ntr):
                        insert_ffaccounts = f"""
                        INSERT INTO ffaccounts (email, fname, lname, phone, password, ffmiles) 
                        VALUES ('{self.email}', '{self.first_name}', '{self.last_name}', 
                        '{self.phone}', '{self.password}', '{self.ffmiles}');
                        """
                        
                        insert_bookings = f"""
                        INSERT INTO bookings (email, flight_id, purchase_date, ticket_amount, 
                        return_flights, confirmation_code, aircraft_type)
                        VALUES ('{self.email}', '{self.flight_id}', '{self.purchase_date}', '{self.ticket_amount}',
                        '{self.return_flights}', '{self.confirmation_code}', '{self.aircraft_type}');
                        """

                        update_flights = f"UPDATE flights SET seats_booked = seats_booked + {self.ticket_amount + self.return_flights} WHERE id = {i + 1};"

                        run_ins_ff = sqlib.execute_query(con, insert_ffaccounts)
                        run_ins_bookings = sqlib.execute_query(con, insert_bookings)
                        run_update = sqlib.execute_query(con, update_flights)

                        if self.return_flights > 0:
                                insert_return = f"INSERT INTO return_flights (booking_id, return_code, return_checked_in) VALUES ('{i + i}', '{self.return_code}', '{self.return_checked_in}')"
                                run_return = sqlib.execute_query(con, insert_return)

                        self.__init__()

if __name__ == "__main__":
    Gen_data().insert_vals()