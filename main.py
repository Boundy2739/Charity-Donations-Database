from tables import *
from addDonators import *
from deleteDonators import *
from addDonations import *
from deleteDonations import *
from addEvent import *
from deleteEvent import *
from modifyDonators import *
from modifyDonations import *


UserInput = int(input("Choose an option"))



if UserInput == 1:
    CreateTables()

if UserInput == 2:
    addRecords()


if UserInput == 3:
    UserID = int(input("Insert the user ID to delete: "))
    DeleteRecords(UserID)

if UserInput == 4:
    addDonations()

if UserInput == 5:
    addEvents()

if UserInput == 6:
    event = str(input("Insert the name of the event delete: "))
    deletebyEvent(event)
if UserInput == 7:
    deleteEvent()
if UserInput == 8:
    editDonators()

if UserInput == 9:
    editDonations()
#sqltest = """insert into donators VALUES ('{}','{}','{}','{}','{}','{}','{}',1)""".format(k_id,k_name,k_address,k_housenumber,k_postcode,k_phone,k_email)
#cursor.execute(sqltest)



