from matplotlib import pyplot as plt
import sqlib

con = sqlib.create_db_connection("127.0.0.1", "dheadley", "dheadley1", "airline")

# generates reports on the status of the airline
class Report_gen:
        bars = []
        height = []
        pop_data = []
        x = []
        y1 = []
        y2 = []
        book_rev_data = []
        print_console = None
        save_graph = None

        # initializes the values for report generation
        def __init__(self):
                # query to get the most pop dests by month
                pop_query = """
                SELECT destination, SUM(ticket_amount)
                AS 'value_occurrence'
                FROM flights INNER JOIN bookings
                ON flights.id = bookings.flight_id
                GROUP BY destination 
                ORDER BY count(destination) DESC 
                LIMIT 5;
                """

                self.pop_data = sqlib.read_query(con, pop_query)
                
                # fills the pop dest axis values with their data
                for i in self.pop_data:
                        self.bars.append(i[0])
                        self.height.append(i[1])
                
                #query to get the booking and revenue information of the airline
                book_rev_query = """
                SELECT MONTH(purchase_date) AS 'month',
                (SUM(ticket_amount) + SUM(return_flights)) * price AS 'monthly_sales',
                CAST(SUM(ticket_amount) + SUM(return_flights) AS INT) AS 'tickets_sold'
                FROM bookings INNER JOIN flights
                ON bookings.flight_id = flights.id
                WHERE YEAR(purchase_date) = '2022'
                GROUP BY MONTH(purchase_date);
                """

                self.book_rev_data = sqlib.read_query(con, book_rev_query)

                # fills the book_rev axis values with their data
                for i in self.book_rev_data:
                        if len(self.x) < 12:
                                self.x.append(i[0])
                                self.y1.append(round(i[1]/1000))
                                self.y2.append(i[2])

                self.print_console = input("Would you like the info printed to the console? ").lower().strip()
                self.save_graph = input("Would you like the info saved as a graph? ").lower().strip()

        # tells the user helpful info when the print the object
        def __str__(self):
                return """
                This class' primary purpose is to generate reports as charts and text.
                You can run pop_destinations to see a chart of the most popular destinations 
                or bookings_rev to see the monthly bookings and revenue.
                """

        # gets the booking and revenue data of the airline in text or graph form
        def bookings_rev(self):
                try:        
                        if self.print_console == "yes":
                                print("\nColumn 1 = Month\nColumn 2 = Sales\nColumn 3 = Tickets Sold")
                                print(f'{self.book_rev_data}\n')
                        elif self.print_console == "no":
                                print ("The info won't be printed to the console.")
                        else:
                                print("Your print console input was not understood. The info won't be printed to the console.")
                        
                        if self.save_graph == "yes":
                                plt.close()
                                # first plot with X and Y data
                                plt.plot(self.x, self.y1, color = 'black')
                        
                                # second plot with x1 and y1 data
                                plt.plot(self.x, self.y2, color = 'orange')
                        
                                plt.xlabel("Month")
                                plt.ylabel("Revenue in Thousands (Black Line) and Bookings (Orange Line)")
                                plt.suptitle('Monthly Booking Revenue')

                                file_name = input("Enter file name: ")
                                if '.' or ' ' in file_name:
                                        print("There was a period in your file name. Please run the program once more to try again.")
                                else:
                                        plt.savefig(f'{file_name}.png')
                                        plt.show()
                                        print(f"The graph has been saved as {file_name}.png")
                        elif self.save_graph == "no":
                                print("The graph will not be saved.")
                        else:
                                print("Your save graph input was not understood. The graph won't be saved.")
                except Exception as err:
                        print(f"You entered an invalid input. It produced the error:\n\n{err}\n\nYou may run the program to try again.")

        # makes a graph or prints the information of the most popular destinations
        def pop_destinations(self):
                try:        
                        if self.print_console == "yes":
                                print("\nColumn 1 = Destination\nColumn 2 = Visitors")
                                print(f'{self.pop_data}\n')
                        elif self.print_console == "no":
                                print ("The info won't be printed to the console.")
                        else:
                                print("Your print console input was not understood. The info won't be printed to the console.")                        
                        if self.save_graph == "yes":
                                plt.close()
                                plt.bar(self.bars, 
                                self.height,
                                color = "orange")

                                plt.xlabel('Destination')
                                plt.ylabel('# of Bookings')
                                plt.suptitle('Most Popular Destinations')
                                file_name = input("Enter file name: ")
                                if '.' or ' ' in file_name:
                                        print("There was a period or space in your file name. Please run the program once more to try again.")
                                else:
                                        plt.savefig(f'{file_name}.png')
                                        plt.show()
                                        print(f"The graph has been saved as {file_name}.png")
                        elif self.save_graph == "no":
                                print("The graph will not be saved.")
                        else:
                                print("Your input was not understood. The graph won't be saved.")
                except Exception as err:
                        print(f"You entered an invalid input. It produced the error:\n\n{err}\n\nYou may run the program to try again.")

# manages which reports are ran
def run_report_gen():
        run_pop = input("Would you like to run the popular destinations code? ").strip().lower()
        if run_pop == "yes":
                Report_gen().pop_destinations()
        elif run_pop == "no":      
                print("Pop_destinations won't be run.") 
        else:
                print("You entered an input other than yes or no. Pop_destinations won't be run.")

        run_rev = input("Would you like to run the bookings and revenue code? ").strip().lower()

        if run_rev == "yes":
                Report_gen().bookings_rev()
        elif run_rev == "no":      
                print("Bookings_rev won't be run.") 
        else:
                print("You entered an input other than yes or no. Bookings_rev won't be run.")

if __name__ == "__main__":
        run_report_gen()