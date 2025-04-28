import sqlite3 as db
from tables import *

def addDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            k_id= int(input("Insert the ID, the ID cannot contain letters: "))
            cursor.execute("""SELECT ID from donators WHERE ID ='{}'""".format(k_id))
            IDcheck = cursor.fetchall()
            if IDcheck:
                print("This ID is already in the database, insert an unique ID")
            else:
                k_name = str(input("put your name: "))
                k_address = str(input("put your adress: "))
                k_housenumber = str(input("put your housenum: "))
                k_postcode = str(input("put your postcode: "))
                k_phone = str(input("put your phone: "))
                k_email = str((input("put email: ")))
                cursor.execute("""insert into donators VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(k_id,k_name,k_address,k_housenumber,k_postcode,k_phone,k_email))
                connection.commit()
                confirmation = input("Do you want to add another record? y/n: ")
                if confirmation.lower() == "n":
                    connection.close()
                    break
                else:
                    print("ok")
        except ValueError:
            print("Please dont use letter when asked for numeric values only")

        

def addVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            k_ID = int(input("Insert the ID: "))
            k_name = input("Insert the name and surname of the Volunteer: ")
            k_address = input("Insert the name of the street where they live: ")
            k_housenumber = int(input("Insert the house number"))
            k_postcode = input("Insert the postcode: ")
            k_phonenumber = int(input("Insert their phone number: "))
            k_email = input("Insert the email: ")
            cursor.execute("""INSERT into volunteers VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(k_ID,k_name,k_address,k_housenumber,k_postcode,k_phonenumber,k_email))
            connection.commit()

            confirmation = input("Do you want to add another record? y/n: ")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
        except ValueError:
            print("Please dont use letter when asked for numeric values only")
    


def addDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            k_id= int(input("Insert the donator's ID: "))
            k_amount = float(input("Insert the amount donated: "))
            k_date = str(input("Insert the date of the donation: "))
            k_role = input("Is the donator a volunteer? y/n: ")
            if k_role.lower() == "y":
                cursor.execute("""Select ID FROM volunteers WHERE ID = '{}'""".format(k_id))
                checkIDs = cursor.fetchall()
                try:
                    if checkIDs[0][0]== k_id:
                        cursor.execute("""insert into volunteers_donations (VolunteerID,Amount,Date) VALUES ('{}','{}','{}')""".format(k_id,k_amount,k_date))
                except IndexError:
                    print("The ID you inserted does not exist in the database")
            else:
                cursor.execute("""Select ID FROM donators WHERE ID = '{}'""".format(k_id))
                checkIDs = cursor.fetchall()
                try:
                    if checkIDs[0][0]== k_id:
                        cursor.execute("""insert into donor_donations (DonatorID,Amount,Date) VALUES ('{}','{}','{}')""".format(k_id,k_amount,k_date))
                except IndexError:
                    print("The ID you inserted does not exist in the database\n")
                    print("You need to add the donor's ID into the donators table before linking a donation to it")
            connection.commit()

            confirmation = input("Do you want to add another record? y/n: ")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
        except ValueError:
            print("Please dont use letters when asked to add numbers only!")


def addEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
            cursor.execute("PRAGMA foreign_keys=1")
            k_eventName = input("Please insert the name of the event you want to add: ")
            cursor.execute("""INSERT INTO events (EventName) VALUES('{}')""".format(k_eventName))
            connection.commit()
            confirmation = input("Do you want to add another record? y/n: ")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")



def addEventsHistory():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            k_eventName = input("Insert the name of the event:")
            k_date = input("Insert the date of the event: ")
            k_room = input("In which room is the event going to take place: ")
            k_participants = int(input("Insert the number of participants that will be there: "))
            k_price = float(input("Insert the price of the ticket: "))
            k_total = k_price * k_participants

            cursor.execute("""SELECT EventID from events WHERE EventName ='{}' """.format(k_eventName))
            k_eventID = cursor.fetchall()
            cursor.execute("""insert into events_history(EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations,EventID) VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(k_eventName,k_date,k_room,k_participants,k_price,k_total,k_eventID[0][0]))
            
            connection.commit()
            confirmation = input("Do you want to add another record? y/n: ")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
        except:
            print("Dont insert letters!")
    



