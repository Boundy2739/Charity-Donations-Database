import sqlite3 as db
from tabulate import tabulate
from editRecords import *
from deleteRecords import *
import time

#shows all the donators
def viewDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from donators""")
    data = cursor.fetchall()
    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()

#shows all the volunteers
def viewVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from volunteers""")
    data = cursor.fetchall()
    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()

#shows all the donations made
def viewDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT DonatorID,Amount,Date from donor_donations
                   UNION
                   SELECT VolunteerID,Amount,Date from volunteers_donations""")
    data = cursor.fetchall()
    headers = ["Donor ID","Amount donated","Date"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()

#shows all the past events
def viewEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    #joins table to display the name of the event instead of the ID
    cursor.execute("""SELECT events.EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history
                   JOIN events ON events_history.EventID = events.EventID""")
    data = cursor.fetchall()
    headers = ["Event name","Date","Room info","Participants","Ticket price","Total donations"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()


def searchOptions():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    print("Insert 1 to search a donation coming from a donor")
    print("Insert 2 to search a donation coming from a volunteer")
    print("Insert 3 to search a events in the event history")
    print("Insert 0 to go back")
    while True:
        try:
            UserChoice = int(input("Choose an option: "))
            if UserChoice == 1:
                #creates a list of IDs
                IDs = []
                insertIDs = 1
                while insertIDs == 1:
                    try:
                        searchPrompt = int(input("Insert the ID of the donators: "))
                        #adds IDs tp the list
                        IDs.append(searchPrompt)
                        print(IDs)
                        stop = input("Do you want to insert more IDs to search? y/n: ")
                        if stop.upper() == "N":
                            insertIDs = 0
                        elif stop.upper() == "Y":
                            print("ok")
                        else:
                            print("reply with y or n\n")
                        print(IDs)
                        
                    
                    except ValueError:
                        print("Use whole numbers")
                
                headers = ["RecordID","Donator ID","Amount","Date"]
                results = []
                try: #the for loop runs through the IDs list
                    for items in IDs:
                        cursor.execute("""SELECT * from donor_donations WHERE DonatorID='{}'""".format(items))
                        #returns every row found using the IDs
                        rows = cursor.fetchall()
                        #appends the rows in the results
                        results.extend(rows)
                except IndexError:
                    print("You inserted an ID that does not exists in the table")
                while True:
                    #prints the result so the user can see which records have been found
                    print(tabulate(results, headers=headers,tablefmt="grid"))
                    if len(results) == 0:
                        print("No events found")
                        connection.close()
                        return
                    
                    else:
                        print("Insert 1 to modify the entries")
                        print("Insert 2 to delete the entries")
                        print("Or 3 to go back\n")
                        try:
                            UserChoice2 = int(input("choose an option: "))
                            
                            if UserChoice2 == 1:
                                #asks the user for the Record ID of the record the need to edit
                                RecordID = int(input("Insert the record ID of the donation you want to edit: "))
                                cursor.execute("""SELECT DonatorID,Amount,Date from donor_donations WHERE ID = '{}'""".format(RecordID))
                                #this fetches the details of the donation as the results and store them
                                results = cursor.fetchall()[0]
                                #the function will take the results as parameters
                                editDonations(int(results[0]),float(results[1]),results[2])
                                return
                            if UserChoice2 == 2:
                                RecordID = int(input("Insert the record ID of the donation you want to edit: "))
                                cursor.execute("""SELECT DonatorID,Amount,Date from donor_donations WHERE ID = '{}'""".format(RecordID))
                                results = cursor.fetchall()[0]
                                print(results)
                                deleteDonorDonation(int(results[0]),float(results[1]),results[2])
                                return
                            if UserChoice2 == 3:
                                print("ok")
                                connection.close()
                                return
                            
                            if UserChoice2 > 3 or UserChoice2 < 0:
                                print("Please choose one of the options")
                        except:
                            print("Dont use letters or decimals")
                    

                
            if UserChoice == 2:
                IDs = []
                insertIDs = 1

                while insertIDs == 1:
                    try:
                        searchPrompt = int(input("Insert the ID of the volunteer: "))
                        IDs.append(searchPrompt) 
                        print(IDs)
                        stop = input("Do you want to add more IDs? y/n: ")
                        if stop.upper() == "N":
                            insertIDs = 0
                        elif stop.upper() == "Y":
                            print("ok")
                        else:
                            print("reply with y or n\n")
                        print(IDs)
                        
                    
                    except ValueError:
                        print("Use whole numbers")
                
                headers = ["RecordID","Volunteers ID","Amount","Date"]
                results = []
                try:
                    for items in IDs:
                        cursor.execute("""SELECT * from volunteers_donations WHERE VolunteerID='{}'""".format(items))
                        rows = cursor.fetchall()
                        results.extend(rows)
                except IndexError:
                    print("You inserted an ID that does not exists in the table")
                while True:
                    print(tabulate(results, headers=headers,tablefmt="grid"))
                    if len(results) == 0:
                        print("No events found")
                        connection.close()
                        return
                    print("Insert 1 to modify the entries")
                    print("Insert 2 to delete the entries")
                    print("Or 3 to go back\n")
                    UserChoice2 = int(input("choose an option: "))
                    try:
                        if UserChoice2 == 1:
                            RecordID = int(input("Insert the record ID of the donation you want to edit: "))
                            cursor.execute("""SELECT VolunteerID,Amount,Date from volunteers_donations WHERE ID = '{}'""".format(RecordID))
                            results = cursor.fetchall()[0]
                            print(results)
                            editDonations(int(results[0]),float(results[1]),results[2])
                            return
                        if UserChoice2 == 2:
                            RecordID = int(input("Insert the record ID of the donation you want to delete: "))
                            cursor.execute("""SELECT VolunteerID,Amount,Date from volunteers_donations WHERE ID = '{}'""".format(RecordID))
                            results = cursor.fetchall()[0]
                            print(results)
                            deleteDonorDonation(int(results[0]),float(results[1]),results[2])
                            return
                        if UserChoice2 == 3:
                            print("ok")
                            return
                        if UserChoice2 > 3 or UserChoice2 < 0:
                            print("Please choose one of the options")
                    except:
                        print("Dont use letters or decimals")
            if UserChoice == 3:
                Events = []
                results = []
                headers = ["Event Name","Amount","Date"]
                insertEvents = 1
                while insertEvents == 1:
                    searchPrompt = input("Insert the name of the event your looking for in the events history: ")
                    Events.append(searchPrompt) 
                    print(Events)
                    stop = input("Do you want add more events to search? y/n")
                    if stop.upper() == "N":
                        insertEvents = 0
                try:
                    for items in Events:
                        cursor.execute("""SELECT EventID from events WHERE EventName = '{}'""".format(items))
                        EventID = cursor.fetchall()[0][0]
                        cursor.execute("""SELECT ID,events.EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history 
                                JOIN events ON events_history.EventID = events.EventID
                                WHERE events_history.EventID = '{}'""".format(EventID))

                        rows = cursor.fetchall()
                        results.extend(rows)
                except IndexError:
                    print("Some of the events you looked for dont exist in the event list")
                    time.sleep(1.5)
                    
                headers = ["RecordID","EventName","Date","Room","Participants","Ticket Price","Total donations"]   
                while True:
                    print(tabulate(results, headers=headers,tablefmt="grid"))
                    if len(results) == 0:
                        print("No events found")
                        return
                    print("Insert 1 to modify the entries")
                    print("Insert 2 to delete the entries")
                    print("Or 3 to go back\n")
                    try:
                        UserChoice2 = int(input("choose an option: "))
                        
                        if UserChoice2 == 1:
                            RecordID = int(input("Insert the record ID of the donation you want to edit: "))
                            cursor.execute("""SELECT EventID,Date,RoomInfo,Participants,TicketPrice,TotalDonations 
                                        from events_history
                                        WHERE ID = '{}'""".format(RecordID))
                            results = cursor.fetchall()[0]
                            print(results)
                            editDonations(int(results[0]),results[1],results[2],int(results[3]),float(results[4]),float(results[5]))
                            return
                        if UserChoice2 == 2:
                            RecordID = int(input("Insert the record ID of the donation you want to delete: "))
                            cursor.execute("""SELECT EventID,Date,RoomInfo,Participants,TicketPrice,TotalDonations 
                                        from events_history
                                        WHERE ID = '{}'""".format(RecordID))
                            results = cursor.fetchall()[0]
                            print(results)
                            editDonations(int(results[0]),results[1],results[2],int(results[3]),float(results[4]),float(results[5]))
                            return
                        if UserChoice2 == 3:
                            print("ok")
                            return
                        if UserChoice2 > 3 or UserChoice2 < 0:
                            print("Please choose one of the options")
                    except ValueError:
                        print("Dont use letters or decimals!")
            if UserChoice == 0:
                print("Going back\n")
                return
            if UserChoice > 3 or UserChoice < 0:
                print("Select one of the options")   
        except ValueError:
            print("Dont use letters or decimals!")