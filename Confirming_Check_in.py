import sqlib
import datetime
from datetime import date, time

con = sqlib.create_db_connection("127.0.0.1", "dheadley", "dheadley1", "airline")

# checks a person in
def confirm_check_in():
    try:
        email = input("What is your email?: ")
        password = input("What is your password?: ")
        confirm_code = int(input("What is your flight confirmation code? "))

        is_return = input("Is this a return flight (yes/no)? ").strip().lower()

        origin = input("What is the location of your airport (ex: DEL)?: ")

        if is_return == "no":
            # gets a person's booking info
            sq = f"""
            SELECT bookings.email, ffaccounts.password, bookings.confirmation_code,
            flights.gate, flights.origin, DAY(flights.datetime) AS 'flight_day'
            FROM bookings
            INNER JOIN flights
            ON bookings.flight_id = flights.id
            INNER JOIN ffaccounts
            ON ffaccounts.email = bookings.email
            WHERE bookings.email = '{email}';
            """

            query_results = sqlib.read_query(con, sq)

            # verifies the identity of the person checking in, makes sure they are in the right place, and lets the airline know they arrived
            if [email, password, confirm_code, origin, datetime.date.today()] == [query_results[0][0], query_results[0][1], query_results[0][2], query_results[0][4], query_results[0][5]]:
                uq = f"""
                UPDATE bookings SET checked_in = "yes" WHERE email = '{email}';
                """

                query_results = sqlib.execute_query(con, sq)

                print("You are checked in for your flight.")
            else:
                print("You entered an invalid information. Please try again.")
        elif is_return == "yes":
            # finds the information on a customer taking a return flight (not as important, bonus feature)
            sjq = f"""
            SELECT bookings.email, ffaccounts.password, return_flights.return_code, flights.destination, DAY(flights.datetime)
            FROM bookings INNER JOIN return_flights ON bookings.booking_id = return_flights.booking_id
            INNER JOIN flights ON bookings.flight_id = flights.id
            INNER JOIN ffaccounts ON bookings.email = ffaccounts.email
            WHERE bookings.email = '{email}';
            """

            qr = sqlib.read_query(con, sjq)

            # verifies a person checking in for a return flight is who they claim to be and lets the airline know they arrived
            if ([email, password, confirm_code, origin, datetime.date.today()] == [qr[0][0], qr[0][1], qr[0][2], qr[0][3]], qr[0][4]):
                uq = f"""
                UPDATE return_flights INNER JOIN bookings ON return_flights.booking_id = bookings.booking_id SET return_checked_in = "yes" WHERE bookings.email = '{email}';
                """

                query_results = sqlib.execute_query(con, uq)

                print("You are checked in for your return flight.")
            else:
                print("You entered invalid info. Please try again. ")
        else:
            print("You entered an invalid input. Please try again.")

    except Exception as err:
        print(f"Your input caused an error. \n{err}")

if __name__ == "__main__":
    confirm_check_in()
