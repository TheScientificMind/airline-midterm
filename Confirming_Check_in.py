import base64
import sqlib

con = sqlib.create_db_connection("127.0.0.1", "dheadley", "dheadley1", "airline")

def confirm_check_in():
    email = input("What is your email?: ")
    password = input("What is your password?: ")
    confirm_code = input("What is your flight confirmation code?")
    origin = input("What is the location of your airport (ex: DEL)?: ")
    gate = input("What gate are you at?: ")

    sq = f"""
    SELECT bookings.email, bookings.password, bookings.confirmation_code,
    flights.gate, flights.origin, DAY(flights.datetime) AS 'flight_day'
    FROM bookings
    INNER JOIN flights
    ON bookings.flight_id = flights.id
    WHERE email = '{email}';
    """

    query_results = sqlib.read_query(con, sq)

    if [email, password, confirm_code, gate, origin] == [query_results[0][0], base64.b64encode(query_results[1][0]), query_results[2][0], query_results[3][0], query_results[4][0]]:
        uq = f"""
        UPDATE bookings SET checked_in = "yes" WHERE email = '{email}';
        """

        query_results = sqlib.execute_query(con, sq)
    else:
        print("You entered an invalid issue. Please try again.")

if __name__ == "__main__":
    confirm_check_in()
