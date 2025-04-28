from tables import *
from subMenus import *




def Menu():

    MenuOptions = 1
    while MenuOptions == 1:

        print("Insert 1 if you want to add a new record")
        print("Insert 2 if you want to edit an existing record")
        print("Insert 3 if you want to delete a record")
        print("Insert 4 if you want to view or search record\n")
        UserInput = int(input("Choose an option: "))



        
        
        if UserInput == 1:

            print("hello")
            addOptions()
        
        if UserInput == 2:

            print("hello")
            editOptions()
        
        if UserInput == 3:

            print("hello")
            deleteOptions()
        
        if UserInput == 4:

            print("hello")
            viewOptions()
        
        
        if UserInput == 0:
            print("Bye")
            MenuOptions = 0
        
        
        if UserInput == 5:
            CreateTables()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''if UserInput == 2:
            addDonators()



        if UserInput == 3:
            DeleteDonators()

        if UserInput == 4:
            addDonations()

        if UserInput == 5:
            addEvents()

        if UserInput == 6:
            addEventsHistory()
        if UserInput == 7:
            deleteEventHistory()
        if UserInput == 8:
            editDonators()

        if UserInput == 9:
            editDonations()

        if UserInput == 10:
            viewDonations()
        if UserInput == 11:
            viewDonators()
        if UserInput == 12:
            viewEvents()
        if UserInput == 13:
            searchDonations()
        if UserInput == 14:
            deleteDonorDonation()
        if UserInput == 15:
            deleteEvent()
        if UserInput == 16:
            addVolunteers()
        if UserInput == 17:
            editVolunteers()
        if UserInput == 18:
            deleteVolunteers()
        if UserInput == 19:
            editEventsInstances()
        #sqltest = """insert into donators VALUES ('{}','{}','{}','{}','{}','{}','{}',1)""".format(k_id,k_name,k_address,k_housenumber,k_postcode,k_phone,k_email)
        #cursor.execute(sqltest)'''



