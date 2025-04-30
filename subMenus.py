from addRecords import *
from editRecords import *
from deleteRecords import *
from viewRecords import *



def addOptions():
    
    while True:
        print("Which record do you want to add?\n")
        print("Insert 1 to add a new donor")
        print("Insert 2 to add a new volunteer")
        print("Insert 3 to add a new event")
        print("Insert 4 to add a new event instance")
        print("Insert 5 to add new donation coming from a donor or a volunteer")
        print("Insert 0 to go back\n")
        
        try:
            UserInput = int(input("Choose an option: "))
            if UserInput == 0:
                print("Going back to main menu")
                break
            
            if UserInput == 1:
                addDonators()
            
            if UserInput == 2:
                addVolunteers()
            
            if UserInput == 3:
                addEvents()
            
            if UserInput == 4:
                addEventsHistory()
            
            if UserInput == 5:
                addDonations()
            if UserInput > 5 or UserInput < 0:
                print("Invalid input, please choose one of the options listed")
        except ValueError:
            print("Your input is invalid please use only numbers")


def editOptions():
    
    while True:
        print("editing")
        print("Which record do you want to edit?\n")
        print("Insert 1 to edit an existing donor")
        print("Insert 2 to edit an existing volunteer")
        print("Insert 3 to edit an existing event")
        print("Insert 4 to edit an existing instance")
        print("Insert 5 to edit an existing donation coming from a donor or a volunteer")
        print("Insert 0 to go back\n")
        

        try:
            UserInput = int(input("Choose an option: "))
            if UserInput == 0:
                print("Going back to main menu")
                break
            
            if UserInput == 1:
                editDonators()
            
            if UserInput == 2:
                editVolunteers()
            
            if UserInput == 3:
                editEvents()
            
            if UserInput == 4:
                editEventsInstances()
            
            if UserInput == 5:
                editDonations()

            if UserInput > 5 or UserInput < 0:
                print("Invalid input, please choose one of the options listed")
        except ValueError:
            print("Your input is invalid, dont use letters!")



def deleteOptions():
    while True:
        print("deleting")
        print("Which record do you want to delete?\n")
        print("Insert 1 to delete a donor")
        print("Insert 2 to delete a volunteer")
        print("Insert 3 to delete an event")
        print("Insert 4 to delete an event instance")
        print("Insert 5 to delete a donation coming from a donor or a volunteer")
        print("Insert 0 to go back\n")

        try:
            UserInput = int(input("Choose an option: "))
            if UserInput == 0:
                print("Going back to main menu")
                break
            
            if UserInput == 1:
                DeleteDonators()
            
            if UserInput == 2:
                deleteVolunteers()
            
            if UserInput == 3:
                deleteEvent()
            
            if UserInput == 4:
                deleteEventHistory()
            
            if UserInput == 5:
                deleteDonorDonation()
            
            if UserInput > 5 or UserInput < 0:
                print("Invalid input, please choose one of the options listed")
        
        except ValueError:
            print("Your input is invalid, dont use letters!")



def viewOptions():
    
    while True:
        print("viewing")
        print("Which record do you want to view?\n")
        print("Insert 1 to view the donor's table")
        print("Insert 2 to view a volunteer's table")
        print("Insert 3 to see the events history")
        print("Insert 4 to view a donation coming from a donor or a volunteer")
        print("Insert 5 to search a record")
        print("Insert 0 to go back\n")

        try:
            UserInput = int(input("Choose an option: "))
            if UserInput == 0:
                print("Going back to main menu")
                break
            
            if UserInput == 1:
                viewDonators()
            
            if UserInput == 2:
                viewVolunteers()
            
            if UserInput == 3:
                viewEvents()
            
            if UserInput == 4:
                viewDonations()
            
            if UserInput == 5:
                searchOptions()
            
            if UserInput > 5 or UserInput < 0:
                    print("Invalid input, please choose one of the options listed")
        
        except ValueError:
            print("Your input is invalid, dont use letters!")
        
