import sqlib
import math
from_db = []
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","airline")

def ticket_checking(flight_id):
    qt = """select * from flights where id='{flight_id}';""".format(flight_id = flight_id)
    query_results = sqlib.read_query(con,qt)
    for x in query_results:
        x = list(x)
        from_db.append(x)
    flight_id = from_db[0][0]
    aircraft = from_db[0][5]

    tt = """select id,seats_booked from flights where id='{id}';""".format(id = flight_id)

    ticket_checker = sqlib.read_query(con,tt)
    tt_db = []
    for y in ticket_checker:
        y = list(y)
        tt_db.append(y)
    tickets = tt_db[0][1]

    if aircraft == "737":
        seats = 25
    elif aircraft == "747":
        seats = 100
    elif aircraft == "767":
        seats = 50
    elif aircraft == "777":
        seats = 75
    elif aircraft == "A320":
        seats = 25
    else:
        print("error")

    if tickets > seats:
        if input("I'm sorry but your requested flight is full. Press 1 if you would like to book another flight. Press 2 if you would like to end.") == "1":
            print("do booking stuff")
        else:
            print("goodbye")
    else:
        print("Your ticket has been booked.")

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
            print("Understood")

## 22000 Total
# 679 DEL origins
# 691 DEL destinations
# 646 SFO origins
# 557 SFO destinations
# 644 MEX origins
# 628 MEX destinations
# 647 LAX origins
# 644 LAX destinations
# 617 CTU origins
# 671 CTU destinations
# 647 EWR origins
# 637 EWR destinations
# 1300 SEA origins
# 1327 SEA destinations
# 656 IAH origins
# 628 IAH destinations
# 646 CAN origins
# 638 CAN destinations
# 698 FRA origins
# 631 FRA destinations
# 670 IST origins
# 640 IST destinations
# 618 CJU origins
# 609 CJU destinations
# 647 CKG origins
# 603 CKG destinations
# 693 DEN origins
# 663 DEN destinations
# BOS origins
# BOS destinations
# ORD origins
# ORD destinations
# ATL origins
# ATL destinations
# HND origins
# HND destinations
# KMG origins
# KMG destinations
# SVO origins
# SVO destinations
# JFK origins
# JFK destinations
# DXB origins
# DXB destinations
# SZX origins
# SZX destinations