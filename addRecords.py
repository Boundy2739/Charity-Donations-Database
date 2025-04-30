import sqlite3 as db
from tables import *
from datetime import datetime

def addDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            k_id= int(input("Insert the ID, the ID cannot contain letters: "))
            cursor.execute("""SELECT ID from donators WHERE ID ='{}'""".format(k_id))
            IDcheck = cursor.fetchall()
            #after fetching and storing the result in IDcheck, this will check if the ID inserted is already in the donor table
            if IDcheck: 
                print("This ID is already in the database, insert an unique ID")
            #if the ID is unique the user will be asked to add the other personal details
            else:
                k_name = input("put your name: ")
                k_address = input("put the name of the street where they live: ")
                while True:#checks if the user input is an integer
                     try:
                        k_housenumber = int(input("put the house number: "))
                        break
                     except ValueError:
                         print("Dont use letters or decimals, only whole numbers")
                k_postcode = input("put your postcode: ")
                while True:#checks if the user input is an integer
                     try:
                        k_phone = int(input("put the phone number: "))
                        break
                     except ValueError:
                         print("Dont use letters or decimals, only whole numbers")
                k_email = input("put the email: ")
                #this inserts the values from the user inputs into the table
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
            cursor.execute("""SELECT ID from volunteers WHERE ID ='{}'""".format(k_ID))
            IDcheck = cursor.fetchall()
            #after fetching and storing the result in IDcheck, this will check if the ID inserted is already in volunteer table
            if IDcheck: 
                print("This ID is already in the database, insert an unique ID")
            #if the ID is unique the user will be prmpted to add more personal details                
            else:
                k_name = input("Insert the name and surname of the Volunteer: ")
                k_address = input("Insert the name of the street where they live: ")
                while True:#checks if the user input is an integer
                        try:
                            k_housenumber = int(input("put the house number: "))
                            break
                        except ValueError:
                            print("Dont use letters or decimals, only whole numbers")
                    
                k_postcode = input("Insert the postcode: ")
                while True:#checks if the user input is an integer
                        try:
                            k_phonenumber = int(input("put the phone number: "))
                            break
                        except ValueError:
                            print("Dont use letters or decimals, only whole numbers")
                k_email = input("Insert the email: ")
                #this inserts the values from the user inputs into the table
                cursor.execute("""INSERT into volunteers VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(k_ID,k_name,k_address,k_housenumber,k_postcode,k_phonenumber,k_email))
                connection.commit()

                confirmation = input("Do you want to add another record? y/n: ")
                if confirmation.lower() == "n":
                    connection.close()
                    break
                else:
                    print("ok")
        except ValueError:
            print("Please dont use letter when asked for numeric values only, and dont use decimals unless asked for a monetary value\n")
    


def addDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            k_id= int(input("Insert the donator's ID: "))
            k_amount = float(input("Insert the amount donated: "))
            while True:#forces the user to use the yyyy-mm-dd format
                k_date = input("Insert the date (yyyy-mm-dd): ")
                try:
                    formatted_date = datetime.strptime(k_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                    break 
                except ValueError:
                    print("Invalid date format. Please use yyyy-mm-dd.")
            #this asks the user, wether the donation comes from a regular donor or a volunteer
            k_role = input("Is the donator a volunteer? y/n: ")
            if k_role.lower() == "y": #this runs if the donator is a volunteer
                cursor.execute("""Select ID FROM volunteers WHERE ID = '{}'""".format(k_id))
                
                #this fetches the result of the SELECT statement, it checks if the ID given by the user exists in the table
                checkIDs = cursor.fetchall() 
                try:
                    if checkIDs[0][0]== k_id: #this runs if the ID given is present in the volunteers table
                        cursor.execute("""insert into volunteers_donations (VolunteerID,Amount,Date) 
                                       VALUES ('{}','{}','{}')""".format(k_id,k_amount,formatted_date))
                    else:
                        print("The ID you have given does not exist, you have to add the ID in the volunteers table along with the person's details")
                except IndexError:
                    print("The ID you inserted does not exist in the database")
            elif k_role.lower() == "n": #this runs if the donator is not a volunteer
                cursor.execute("""Select ID FROM donators WHERE ID = '{}'""".format(k_id))
                #this fetches the result of the SELECT statement, it checks if the ID given by the user exists in the table
                checkIDs = cursor.fetchall()
                try:
                    if checkIDs[0][0]== k_id: #this runs if the ID given is present in the donors table
                        cursor.execute("""insert into donor_donations (DonatorID,Amount,Date) 
                                       VALUES ('{}','{}','{}')""".format(k_id,k_amount,formatted_date))
                except IndexError:
                    print("The ID you inserted does not exist in the database\n")
                    print("You need to add the donor's ID into the donators table before linking a donation to it")
            
            else:
                print("Reply with y or n")
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
            while True:#forces the user to use the yyyy-mm-dd format
                k_date = input("Insert the date when the event took place (yyyy-mm-dd): ")
                try:
                    formatted_date = datetime.strptime(k_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                    break 
                except ValueError:
                    print("Invalid date format. Please use yyyy-mm-dd.")
            k_room = input("In which room is the event going to take place: ")
            k_participants = int(input("Insert the number of participants that will be there: "))
            k_price = float(input("Insert the price of the ticket: "))
            k_total = k_price * k_participants
            
            try:
                cursor.execute("""SELECT EventID from events WHERE EventName ='{}' """.format(k_eventName))
                k_eventID = cursor.fetchall()[0][0]
                cursor.execute("""insert into events_history (EventID,Date,RoomInfo,Participants,TicketPrice,TotalDonations) VALUES ('{}','{}','{}','{}','{}','{}')""".format(k_eventID,formatted_date,k_room,k_participants,k_price,k_total))
                
                connection.commit()
                confirmation = input("Do you want to add another record? y/n: ")
                if confirmation.lower() == "n":
                    connection.close()
                    break
                else:
                    print("ok")
            except IndexError:
                print("The event does not exists in the event list")
        except ValueError:
            print("Dont insert letters!")
    


