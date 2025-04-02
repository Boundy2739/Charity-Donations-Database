from tables import *
from addRecords import *
from deleteRecords import *


UserInput = int(input("Choose an option"))



if UserInput == 1:
    CreateTables()

if UserInput == 2:
    addRecords()


if UserInput == 3:
    UserID = int(input("Insert the user ID to delete: "))
    DeleteRecords(UserID)

#sqltest = """insert into donators VALUES ('{}','{}','{}','{}','{}','{}','{}',1)""".format(k_id,k_name,k_address,k_housenumber,k_postcode,k_phone,k_email)
#cursor.execute(sqltest)



