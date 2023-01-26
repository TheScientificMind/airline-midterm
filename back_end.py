import sqlib
import math
from_db = []
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","airline")

# This function adds FF miles and creates new FF accounts for users that don't have one (user's email needs to be in bookings for a FF account to be created)
def ffmiles(email):
    try:
        query = """select * from ffaccounts where email ='{email}';""".format(email = email)
        priceq = """select booking_price from bookings where email ='{email}';""".format(email = email)
        price_checker = sqlib.read_query(con,priceq)
        price = price_checker[0][0]
        ff = round(price/10)
        ffaccount = sqlib.read_query(con,query)
        new_ff = ff + ffaccount[0][2]
        print(f"You have gained {ff} frequent flier miles for a new total of {new_ff} miles.")
        add_ff = """update ffaccounts set ffmiles =('{new_ff}') where ffmiles =('{ffaccount}') and email =('{email}');""".format(new_ff = new_ff, ffaccount = ffaccount[0][2], email = email)
        sqlib.execute_query(con,add_ff)
    except:
        if int(input("Would you like to create a frequent flier account? 1 for yes, 0 for no: ")) > 0:
            password = str(input("Please enter a password for your frequent flier account: "))
            createrq = """insert into ffaccounts (email,password,ffmiles) values ('{email}','{password}','0');""".format(email = email, password = password)
            sqlib.execute_query(con,createrq)
            priceq = """select booking_price from bookings where email ='{email}';""".format(email = email)
            price_checker = sqlib.read_query(con,priceq)
            price = price_checker[0][0]
            ff = round(price/10)
            new_ff = ff
            print(f"You now have {new_ff} frequent flier miles!")
            add_ff = """update ffaccounts set ffmiles =('{new_ff}') where ffmiles =('0') and email =('{email}');""".format(new_ff = new_ff, ffaccount = 0, email = email)
            sqlib.execute_query(con,add_ff)
        else:
            print("Understood, enjoy your flight!")