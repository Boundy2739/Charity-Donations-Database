from tables import *
from subMenus import *
import time




def Menu():

    while True:

        print("Insert 1 to add a new record")
        print("Insert 2 to edit an existing record")
        print("Insert 3 to delete a record")
        print("Insert 4 to view or search record")
        print("Insert 5 to create the tables if you dont have them")
        print("Insert 0 to close the program")



        
        try:
            UserInput = int(input("Choose an option: "))
            if UserInput == 1:

                
                addOptions()
            
            if UserInput == 2:

                
                editOptions()
            
            if UserInput == 3:

                
                deleteOptions()
            
            if UserInput == 4:

                viewOptions()
            
            
            if UserInput == 0:
                print("Bye")
                break
                
            
            
            if UserInput == 5:
                CreateTables()
            if UserInput > 5 or UserInput < 0:
                print("The input is invalid, please choose one of the options listed!\n")
                time.sleep(1.5)
        except ValueError:
            print("This input is invalid, please use only numeric values!\n")
            time.sleep(1.5)
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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



