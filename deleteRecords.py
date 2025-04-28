import sqlite3 as db
from tabulate import tabulate
def DeleteDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    deletingRecords = 1
    while deletingRecords == 1:
        cursor.execute("PRAGMA foreign_keys=1")
        ID = int(input("Insert the ID of the donor you want to delete: "))
        cursor.execute("""SELECT * from donators WHERE ID = '{}'""".format(ID))
        IDCheck = cursor.fetchall()
        try:
            print(tabulate(IDCheck))
            if ID == IDCheck[0][0]:
                confirmation = input("Is this the donor you want to delete? y/n: ")
                if confirmation == "y":
                    try:
                        cursor.execute ( """delete from donators 
                    where ID = '{}' """.format(ID))
                    except db.IntegrityError:
                        print("You cant delete this donator until you have removed all the donations made by them from the database")
        except IndexError:
            print("This ID does not exist in the database, make sure to write it correctly")
        connection.commit()
        confirmation = input("DO you want to remove another donor? y/n" )
        if confirmation.lower() == "n":
            connection.close()
            deletingRecords = 0
        else:
            print("ok")

        



def deleteDonorDonation():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    deletingRecords = 1
    while deletingRecords == 1:
        cursor.execute("PRAGMA foreign_keys=1")
        k_ID = int(input("Insert the ID of the donator whose donation you want to remove: "))
        k_Date = input("Insert the date of the donation")
        k_Amount = float(input("Insert the amount that was donated: "))
        k_role = input("Is the donator a volunteer? y/n")
        if k_role.lower() == "y":
            cursor.execute("""SELECT VolunteerID,Amount,Date from volunteers_donations 
                        WHERE VolunteerID = '{}'
                        AND Date = '{}'
                        AND Amount = '{}'""".format(k_ID,k_Date,k_Amount))
            checkDetails = cursor.fetchall()
            try:
                headers = ["VolunteerID","Amount","Date"]
                if checkDetails[0][0] == k_ID and checkDetails[0][2] == k_Date and checkDetails[0][1] == k_Amount:
                    print(tabulate(checkDetails,headers=headers))
                    confirmation = input("Is this the donation you want to delete? y/n: ")
                    if confirmation == 'y':
                        cursor.execute("""DELETE from volunteers_donations WHERE VolunteerID ='{}' and Date = '{}'""".format(k_ID,k_Date))
            except:
                print("Cannot find a donation with the details give, check that the ID and the date are correct")
        else:
            cursor.execute("""SELECT DonatorID,Amount,Date from donor_donations 
                        WHERE DonatorID = '{}'
                        AND Date = '{}'
                        AND Amount = '{}'""".format(k_ID,k_Date,k_Amount))
            checkDetails = cursor.fetchall()
            
            try:
                headers = ["DonatorID","Amount","Date"]
                if checkDetails[0][0] == k_ID and checkDetails[0][1] == k_Amount and checkDetails[0][2] == k_Date:
                    print(tabulate(checkDetails,headers=headers))
                    confirmation = input("Is this the donation you want to delete? y/n: ")
                    if confirmation.lower() == ("y"):
                        cursor.execute("""DELETE from donor_donations WHERE DonatorID ='{}' and Date = '{}'""".format(k_ID,k_Date))
            except:
                print("Cannot find a donation with the details give, check that the ID and the date are correct")

        connection.commit()
        
        confirmation = input("Do you want to remove more donations? y/n: ")
        if confirmation.lower() == "n":
            connection.close()
            deletingRecords =0
        else:
            print("ok")
            


def deleteVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    deletingRecords = 1
    while deletingRecords == 1:
        cursor.execute("PRAGMA foreign_keys=1")
        k_id = int(input("Insert the ID of volunteer you want to remove from the database: "))
        cursor.execute("""SELECT * from volunteers WHERE ID ='{}'""".format(k_id))
        IDcheck = cursor.fetchall()
        try:
            if k_id == IDcheck[0][0]:
                headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
                print(tabulate(IDcheck, headers=headers,tablefmt="grid"))
                confirmation = input("Is this the volunteer you want to delete? y/n: ")
                if confirmation == "y":
                    try:
                        cursor.execute ( """delete from volunteers
                    where ID = '{}' """.format(k_id))
                    except db.IntegrityError:
                        print("You cant delete this volunteer until you have removed all the donations made by them from the database")
        except IndexError:
            print("This ID does not exists in the database, make sure to spell correctly")
        connection.commit()
        confirmation =  input("Do you want to remove another volunteer? y/n: ")
        if confirmation.lower() == "n":
            connection.close()
            deletingRecords = 0
        else:
            print("ok")



def deleteEventHistory():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    deletingRecords =1
    while deletingRecords == 1:
        cursor.execute("PRAGMA foreign_keys=1")
        eventName = input("Insert the name of the event you want to delete: ")
        eventDate = input("Insert the date of the event you want to delete: ")
        eventRoom = input("Which room did the event took place: ")
        eventParticipants = int(input("How many people did partake: "))
        eventTicketPrice = float(input("Insert the price of the ticket: "))
        cursor.execute("""SELECT EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history WHERE EventName = '{}'
            AND Date = '{}'
            AND RoomInfo = '{}'
            AND Participants = '{}'
            AND TicketPrice = '{}'""".format(eventName,eventDate,eventRoom,eventParticipants,eventTicketPrice))
        eventDetails = cursor.fetchall()
        try:
            headers = ("Event name","Date","Room info","Participants","Ticket price","Total donations")
            if eventDetails [0][0] == eventName and eventDate == eventDetails[0][1] and eventDetails [0][2] == eventRoom and eventParticipants == eventDetails[0][3] and eventDetails[0][4] == eventTicketPrice:

                print(tabulate(eventDetails,headers=headers))
                confirmation = input("Is this the record you want to delete? y/n:")
                if confirmation.lower() == "y":
                    cursor.execute ( """delete from events_history
                        where EventName  = '{}' 
                        and Date = '{}'
                        and RoomInfo ='{}'
                        and Participants ='{}'
                        and TicketPrice = '{}' """.format(eventName,eventDate,eventRoom,eventParticipants,eventTicketPrice))
        except IndexError:
            print("Cant find any event instance with the details given, make sure write correctly the details")


        
        connection.commit()
        confirmation =  input("Do you want to remove another volunteer? y/n: ")
        if confirmation.lower() == "n":
            connection.close()
            deletingRecords = 0
        else:
            print("ok")
def deleteEvent():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    deletingRecords = 1
    while deletingRecords == 1:
        cursor.execute("PRAGMA foreign_keys=1")
        k_eventName = input("Insert the name of the event you want to delete: ")
        cursor.execute("""DELETE from events WHERE EventName = '{}'""".format(k_eventName))
        connection.commit()
        confirmation =  input("Do you want to remove another volunteer? y/n: ")
        if confirmation.lower() == "n":
                connection.close()
                deletingRecords = 0
        else:
                print("ok")