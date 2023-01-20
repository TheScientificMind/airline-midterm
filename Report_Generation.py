from matplotlib import pyplot as plt
import sqlib
import random
from faker import Faker
import random
from datetime import datetime, timedelta
import base64
import secrets
import string
import pprint

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
                SELECT origin, count(origin) as 'value_occurrence' FROM flights
                GROUP BY origin 
                ORDER BY count(origin) 
                DESC LIMIT 5;
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
                        print_console = input("Would you like the info printed to the console? ").lower()
                        if print_console == "yes":
                                print(f'\n{self.pop_data}\n')
                        elif print_console == "no":
                                print ("The info won't be printed to the console.")
                        else:
                                print("Your input was not understood. The info won't be printed to the console.")
                        
                        save_graph = input("Would you like the info saved as a graph? ").lower()
                        if  save_graph == "yes":
                                plt.bar(self.bars, 
                                self.height,
                                color = "orange")

                                plt.xlabel('Destination')
                                plt.ylabel('# of Bookings')
                                plt.suptitle('Most Popular Destinations')
                                file_name = f'{input("Enter file name: ")}.png'
                                if '.' not in file_name:
                                        plt.savefig()
                                        plt.show()
                                        print(f"The graph has been saved as {file_name}")
                                else:
                                        print("There was a period in your file name. Please run the program once more to try again.")
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
        ntr = 1000
        
        # initializes fake values for tables
        def __init__(self):
                self.first_name = fake.first_name()
                self.last_name = fake.last_name()
                self.email = f"{self.first_name}.{self.last_name}@{fake.domain_name()}"
                self.phone = fake.phone_number()
                self.flight_id = random.randint(1, 22000)
                self.booking_price = str(round(random.uniform(100, 1000), 2))
                self.purchase_date = fake.date_time_this_month() - timedelta(days = 30)
                self.ticket_amount = random.randint(1, 8)
                self.return_flights = random.randint(1, self.ticket_amount)
                self.confirmation_code = str(random.randint(1000000, 9999999))
                self.aircraft_type = sqlib.read_query(con, "SELECT aircraft FROM capacity;")[random.randint(0, 4)][0]
                self.password =  base64.b64encode(''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(random.randint(7, 20))).encode("utf-8"))
                self.ffmiles = random.randint(100, 10000)

        # prints the bookings and ffaccounts when the object is printed
        def __str__(self):
                squery = """
                SELECT * FROM bookings;
                SELECT * FROM ffaccounts;
                """
                
                # gets all the data from bookings
                query_results = sqlib.read_query(con, squery)

                return str(query_results)
                
        # inserts __ntr rows of data into the tables
        def insert_vals(self):
                for i in range(self.ntr):
                        insert_query = f"""
                        INSERT INTO bookings (fname, lname, email, phone, flight_id, booking_price, 
                        purchase_date, ticket_amount, return_flights, confirmation_code, aircraft_type)
                        VALUES ('{self.first_name}', '{self.last_name}', '{self.email}', '{self.phone}',
                        '{self.flight_id}', '{self.booking_price}', '{self.purchase_date}', '{self.ticket_amount}', 
                        '{self.return_flights}', '{self.confirmation_code}', '{self.aircraft_type}');
                        
                        INSERT INTO ffaccounts (email, password, ffmiles) 
                        VALUES ("{self.email}", "{self.password}", "{self.ffmiles}");
                        """

                        run_insert = sqlib.execute_query(con, insert_query)
                        
                        self.__init__()
                        print(Report_gen())

        # empties the tables
        def empty_tables(self):
                dquery = """
                DELETE FROM bookings;
                DELETE FROM ffaccounts;
                """

                dquery_results = sqlib.execute_query(con, dquery)

                print(Report_gen())

Report_gen().pop_destinations()
