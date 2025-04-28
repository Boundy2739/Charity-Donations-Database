from addRecords import *
from editRecords import *
from deleteRecords import *
from viewRecords import *



def addOptions():
    sub_options = 1
    while sub_options == 1:
        print("adding")
        print("Which record do you want to add?\n")
        print("Insert 1 to add a new donor")
        print("Insert 2 to add a new volunteer")
        print("Insert 3 to add a new event")
        print("Insert 4 to add a new event instance")
        print("Insert 5 to add new donation coming from a donor or a volunteer")
        print("Insert 0 to go back\n")
        
        UserInput = int(input("Choose an option: "))
        if UserInput == 0:
            sub_options = 0
            print("Going back to main menu")
        
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


def editOptions():
    sub_options = 1
    while sub_options == 1:
        print("editing")
        print("Which record do you want to edit?\n")
        print("Insert 1 to edit an existing donor")
        print("Insert 2 to edit an existing volunteer")
        print("Insert 3 to edit an existing event")
        print("Insert 4 to edit an existing instance")
        print("Insert 5 to edit an existing donation coming from a donor or a volunteer")
        print("Insert 0 to go back\n")

        UserInput = int(input("Choose an option: "))
        if UserInput == 0:
            sub_options = 0
            print("Going back to main menu")
        
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



def deleteOptions():
    sub_options = 1
    while sub_options == 1:
        print("deleting")
        print("Which record do you want to delete?\n")
        print("Insert 1 to delete a donor")
        print("Insert 2 to delete a volunteer")
        print("Insert 3 to delete an event")
        print("Insert 4 to delete an event instance")
        print("Insert 5 to delete a donation coming from a donor or a volunteer")
        print("Insert 0 to go back\n")


        UserInput = int(input("Choose an option: "))
        if UserInput == 0:
            sub_options = 0
            print("Going back to main menu")
        
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

def viewOptions():
    print("viewing")