import sqlib
from_db = []
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","airline")

uinput = list(map(int,input("Input Flight ID: ").strip().split()))

qt = """select flights.id,capacity.aircraft from flights 
join capacity on flights.aircraft = capacity.aircraft;""".format(id=uinput[0])

query_results = sqlib.read_query(con,qt)
for x in query_results:
        x = list(x)
        from_db.append(x)

uinput = uinput[0] - 1

print(from_db[uinput][1])

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