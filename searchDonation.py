import sqlite3 as db
from tabulate import tabulate

def searchDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    print("Insert 1 to search a donation coming from a donor")
    print("Insert 2 to search a donation coming from a volunteer")
    print("Insert 3 to search a donation coming from an event")

    UserChoice = int(input("Choose an option: "))
    if UserChoice == 1:
        IDs = []
        insertIDs = 1
        while insertIDs == 1:
            searchPrompt = int(input("Insert the ID of the donators: "))
            IDs.append(searchPrompt)
            print(IDs)
            stop = input("Do you want to insert more IDs to search?: ")
            if stop.upper() == "N":
                insertIDs = 0
        print(IDs)
        results = []
        headers = ["Donator ID","Amount","Date"]
        
        for items in IDs:
            cursor.execute("""SELECT * from donations WHERE DonatorID='{}'""".format(items))
            results = results + cursor.fetchall()
        print(tabulate(results))
        
    if UserChoice == 2:
        IDs = []
        results = []
        headers = ["Volunteer ID","Amount","Date"]
        insertIDs = 1
        while insertIDs == 1:
            searchPrompt = int(input("Insert the name of the ID of the volunteer: "))
            IDs.append(searchPrompt) 
            print(IDs)
            stop = input("Do you want add more IDs to search? y/n")
            if stop.upper() == "N":
                insertIDs = 0
        
        for items in IDs:
            cursor.execute("""SELECT * from donations where VolunteerID ='{}'""".format(items))

            results = results + cursor.fetchall()
        print(tabulate(results,headers=headers))    
    if UserChoice == 3:
        Events = []
        results = []
        headers = ["Event Name","Amount","Date"]
        insertEvents = 1
        while insertEvents == 1:
            searchPrompt = input("Insert the name of the event where donations came from: ")
            Events.append(searchPrompt) 
            print(Events)
            stop = input("Do you want add more events to search? y/n")
            if stop.upper() == "N":
                insertEvents = 0
        
        for items in Events:
            cursor.execute("""SELECT * from events_history where EventName ='{}'""".format(items))

            results = results + cursor.fetchall()
        print(tabulate(results,headers=headers))    
        
