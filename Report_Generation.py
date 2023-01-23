from matplotlib import pyplot as plt
import sqlib
import random
from faker import Faker
import random
from datetime import datetime, timedelta, date
import base64
import secrets
import string

con = sqlib.create_db_connection("127.0.0.1", "dheadley", "dheadley1", "airline")
fake = Faker()

class Report_gen:
        bars = []
        height = []
        x = []
        y = []
        pop_data = None

        def __init__(self):
                sq = """
                SELECT destination, CAST(ROUND(COUNT(destination) * AVG(ticket_amount)) AS INT)
                AS 'value_occurrence'
                FROM flights INNER JOIN bookings
                ON flights.id = bookings.flight_id
                GROUP BY destination 
                ORDER BY count(destination) DESC 
                LIMIT 5;
                """

                self.pop_data = sqlib.read_query(con, sq)

                for i in self.pop_data:
                        self.bars.append(i[0])
                        self.height.append(i[1])

        # tells the user helpful info when the print the object
        def __str__(self):
                return """
                This class' primary purpose is to generate reports as charts and text. 
                You can run pop_destinations to see a chart of the most popular destinations.
                """

        # makes a graph or prints the information of the most popular destinations
        def pop_destinations(self):
                try:        
                        print_console = input("Would you like the info printed to the console? ").lower().strip()

                        if print_console == "yes":
                                print(f'\n{self.pop_data}\n')
                        elif print_console == "no":
                                print ("The info won't be printed to the console.")
                        else:
                                print("Your input was not understood. The info won't be printed to the console.")
                        
                        save_graph = input("Would you like the info saved as a graph? ").lower().strip()
                        if  save_graph == "yes":
                                plt.bar(self.bars, 
                                self.height,
                                color = "orange")

                                plt.xlabel('Destination')
                                plt.ylabel('# of Bookings')
                                plt.suptitle('Most Popular Destinations')
                                file_name = input("Enter file name: ")
                                if '.' in file_name:
                                        print("There was a period in your file name. Please run the program once more to try again.")
                                else:
                                        plt.savefig(f'{file_name}.png')
                                        plt.show()
                                        print(f"The graph has been saved as {file_name}")
                        elif save_graph == "no":
                                print("The graph will not be saved.")
                        else:
                                print("Your input was not understood. The graph won't be saved.")

                except Exception as err:
                        print(f"You entered an invalid input. It produced the error:\n\n{err}\n\nYou may run the program to try again.")

class Gen_data:
        first_name = None
        last_name = None
        email = None
        phone = None
        booking_price = None
        purchase_date = None
        flight_date = None
        ticket_amount = None
        return_flights = None
        confirmation_code = None
        aircraft_type = None
        password = None
        ffmiles = None
        ntr = 10000
        
        # initializes fake values for tables
        def __init__(self):
                self.first_name = fake.first_name()
                self.last_name = fake.last_name()
                self.email = f"{self.first_name}.{self.last_name}@{fake.domain_name()}"
                self.phone = fake.phone_number()
                self.flight_id = random.randint(1, 22000)
                self.booking_price = str(round(random.uniform(100, 1000), 2))
                self.purchase_date = fake.date_time_between(date.fromisoformat('2022-01-01'), datetime.now() - timedelta(days = 14))
                self.ticket_amount = random.randint(1, 8)
                self.return_flights = random.randint(1, self.ticket_amount)
                self.confirmation_code = str(random.randint(1000000, 9999999))
                self.aircraft_type = sqlib.read_query(con, "SELECT aircraft FROM capacity;")[random.randint(0, 4)][0]
                self.password =  base64.b64encode(''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(random.randint(7, 20))).encode("utf-8"))
                self.ffmiles = random.randint(100, 10000)

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
                uery_results = sqlib.read_query(con, select_ff)

                return str(query_results)
                
        # inserts ntr rows of data into the tables
        def insert_vals(self):
                for i in range(self.ntr):
                        insert_bookings = f"""
                        INSERT INTO bookings (fname, lname, email, phone, flight_id, booking_price, 
                        purchase_date, ticket_amount, return_flights, confirmation_code, aircraft_type)
                        VALUES ('{self.first_name}', '{self.last_name}', '{self.email}', '{self.phone}',
                        '{self.flight_id}', '{self.booking_price}', '{self.purchase_date}', '{self.ticket_amount}', 
                        '{self.return_flights}', '{self.confirmation_code}', '{self.aircraft_type}');
                        """

                        insert_ffaccounts = f"""
                        INSERT INTO ffaccounts (email, password, ffmiles) 
                        VALUES ("{self.email}", "{self.password}", "{self.ffmiles}");
                        """

                        update_flights = f"UPDATE flights SET seats_booked = seats_booked + 1 WHERE id = {i + 1};"

                        run_ins_bookings = sqlib.execute_query(con, insert_bookings)
                        run_ins_ff = sqlib.execute_query(con, insert_ffaccounts)
                        run_update = sqlib.execute_query(con, update_flights)

                        self.__init__()
                print(Gen_data())

Report_gen().pop_destinations()
