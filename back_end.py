import sqlib
from_db = []
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","airline")

# uinput = list(map(int,input("Input Flight ID: ").strip().split()))
# # Need to get the ID (for real)

# tickets = 0
# # Need to get real ticket information + add the tickets being bought to this because if person is buying 3 tickets but there is only one more seat avalible that bad

# qt = """select flights.id,capacity.aircraft from flights 
# join capacity on flights.aircraft = capacity.aircraft;""".format(id=uinput[0])

# query_results = sqlib.read_query(con,qt)
# for x in query_results:
#         x = list(x)
#         from_db.append(x)

uinput = int(input("Input Booking ID: "))

qt = """select * from bookings where booking_id='{uinput}';""".format(uinput = uinput)
query_results = sqlib.read_query(con,qt)
for x in query_results:
        x = list(x)
        from_db.append(x)
flight_id = from_db[0][5]

ticket_checker = """select * from bookings where flight_id ='{flight_id}';""".format(flight_id = flight_id)

# if aircraft == "737":
#     seats = 25
# elif aircraft == "747":
#     seats = 100
# elif aircraft == "767":
#     seats = 50
# elif aircraft == "777":
#     seats = 75
# elif aircraft == "A320":
#     seats = 25
# else:
#     print("error")

# if tickets > seats:
#     if input("I'm sorry but your requested flight is full. Press 1 if you would like to book another flight. Press 2 if you would like to end.") == "1":
#         print("do booking stuff")
#     else:
#         print("goodbye")
# else:
#     print("Your ticket has been booked.")

# email = "placeholder@test.edu"
# try:
#     query = """select * from ffaccounts where email ='{email}';""".format(email = email)
#     # calculate the number of FF the user would get
#     # give user said FF
# except:
#     if int(input("Would you like to create a frequent flier account? 1 for yes, 0 for no: ")) > 0:
#         password = str(input("Please enter a password for your frequent flier account: "))
#         creater = """inset into ffaccounts (email,password,ffmiles) values ('{email}','{password}','0');""".format(email = email, password = password)
#         # calculate the number of FF the user would get
#         # give user said FF

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