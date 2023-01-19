import sqlib
from_db = []
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","airline")

uinput = list(map(int,input("Input Flight ID: ").strip().split()))
# Need to get the ID (for real)

tickets = 0
# Need to get real ticket information + add the tickets being bought to this because if person is buying 3 tickets but there is only one more seat avalible that bad

qt = """select flights.id,capacity.aircraft from flights 
join capacity on flights.aircraft = capacity.aircraft;""".format(id=uinput[0])

query_results = sqlib.read_query(con,qt)
for x in query_results:
        x = list(x)
        from_db.append(x)

uinput = uinput[0] - 1

aircraft = (from_db[uinput][1])

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


# table where flier info will be avalible is in the works
class flier:
    fname = None
    lname = None
    phone_num = None
    email = None
    ffmiles = None

    def __init__(self,fname,lname,phone_num,email):
        self.fname = fname
        self.lname = lname
        self.phone_num = phone_num
        self.email = email
    # all based upon email
        # self.ffmiles = 
    
    def addff(self,ffmiles):
        self.ffmiles =+ ffmiles