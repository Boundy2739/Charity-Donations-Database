import sqlite3 as db
from tabulate import tabulate
from datetime import datetime


#this function deletes a donor from the table
def DeleteDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            cursor.execute("PRAGMA foreign_keys=1")
            ID = int(input("Insert the ID of the donor you want to delete: "))
            cursor.execute("""SELECT * from donators WHERE ID = '{}'""".format(ID))
            IDCheck = cursor.fetchall()   #stores results of SELECT statement
            try:
                print(tabulate(IDCheck))#prints the results so the user can check if they are deleting the right person
                if ID == IDCheck[0][0]: #this statement checks if the ID inserted by the user is present in the donators table
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
                break
            else:
                print("ok")
        except ValueError:
            print("Use only numbers!")

        



def deleteDonorDonation(k_ID = None, k_Amount = None, formatted_date = None):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            cursor.execute("PRAGMA foreign_keys=1")
            if k_ID == None:
                k_ID = int(input("Insert the ID of the donator whose donation you want to remove: "))
            if formatted_date == None:
                while True: #this loop forces the user to respect the yyyy-mm-dd format
                    k_Date = input("Insert the date when the donation happened (yyyy-mm-dd): ")
                    try:
                        formatted_date = datetime.strptime(k_Date, "%Y-%m-%d").strftime("%Y-%m-%d")
                        break 
                    except ValueError:
                        print("Invalid date format. Please use yyyy-mm-dd.")
            if k_Amount == None:
                k_Amount = float(input("Insert the amount that was donated: "))
            
            #This unites the donor and volunteers donation tables into one table with a new Role column, 
            #and checks if the ID of the user is present
            cursor.execute("""select DonatorID, Date,Amount, 'Donor' as Role from donor_donations where DonatorID='{}'
                                AND Date ='{}'
                                AND Amount = '{}'
                                UNION
                                select VolunteerID, Date,Amount, 'Volunteer' as Role from volunteers_donations where VolunteerID ='{}'
                                AND Date ='{}'
                                AND Amount = '{}'""".format(k_ID,formatted_date,k_Amount,k_ID,formatted_date,k_Amount))
                
            # Fetch the query result and store it in CheckDetails    
            CheckDetails = cursor.fetchall()

            # Check if any matching donation was found           
            if CheckDetails:
                if CheckDetails[0][3] == 'Donor':  # If found, check if the donation came from a 'Donor'
                    headers = ["ID","Amount","Date","Role"]
                    print(tabulate(CheckDetails, headers = headers, tablefmt="grid"))
                    confirmation = input("Is this the donation you want to delete? y/n: ")
                    if confirmation.lower() == ("y"):
                                        
                        cursor.execute("""DELETE from donor_donations 
                                        WHERE DonatorID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(k_ID,formatted_date,k_Amount))

                    
                                    
                if CheckDetails[0][3] == 'Volunteer':  # If found, check if the donation came from a 'Volunteer'
                    headers = ["ID","Amount","Date","Role"]
                    print(tabulate(CheckDetails, headers = headers, tablefmt="grid"))
                    confirmation = input("Is this the donation you want to delete? y/n: ")
                    if confirmation.lower() == ("y"):
                        
                        cursor.execute("""DELETE from volunteers_donations 
                                        WHERE VolunteerID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(k_ID,formatted_date,k_Amount))
        


                                    
            if not CheckDetails:
                print("There is no donations in database with the details you have given!")

            connection.commit()
            
            confirmation = input("Do you want to remove more donations? y/n: ")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
                k_ID = None
                k_Amount = None
                formatted_date = None
        except ValueError:
            print("Please dont use letters!")                
            


def deleteVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            cursor.execute("PRAGMA foreign_keys=1")
            k_id = int(input("Insert the ID of volunteer you want to remove from the database: "))
            cursor.execute("""SELECT * from volunteers WHERE ID ='{}'""".format(k_id))
            
            #Fetch the results and store them
            IDcheck = cursor.fetchall()
            try:
                if k_id == IDcheck[0][0]: #Checks if the results are the same as inputs the user has given
                    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
                    
                    #Shows the record the user is going to delete if they accept the confirmation
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
                break
            else:
                print("ok")
        except ValueError:
            print("Dont use letters when inserting the ID")



def deleteEventHistory(eventID = None,formatted_date = None, eventRoom = None,eventParticipants = None, eventTicketPrice = None):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:
            cursor.execute("PRAGMA foreign_keys=1")
            if eventID == None:
                eventName = input("Insert the name of the event you want to delete: ")
            if formatted_date == None:
                while True: #this forces the user to stick to the format yyyy-mm-dd
                    eventDate = input("Insert the date when the donation happened (yyyy-mm-dd): ")
                    try:
                        formatted_date = datetime.strptime(eventDate, "%Y-%m-%d").strftime("%Y-%m-%d")
                        break 
                    except ValueError:
                        print("Invalid date format. Please use yyyy-mm-dd.")
            if eventRoom == None:
                eventRoom = input("Which room did the event took place: ")
            if eventParticipants == None:
                eventParticipants = int(input("How many people did partake: "))
            if eventTicketPrice == None:
                eventTicketPrice = float(input("Insert the price of the ticket: "))
            if eventID == None:
                cursor.execute("""SELECT EventID from events WHERE EventName = '{}'""".format(eventName))
                eventID = cursor.fetchall()[0][0]
            #selects the rows that match the user input
            cursor.execute("""SELECT events.EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history
                              JOIN events ON events_history.EventID = events.EventID 
                              WHERE events_history.EventID = '{}'
                              AND Date = '{}'
                              AND RoomInfo = '{}'
                              AND Participants = '{}'
                              AND TicketPrice = '{}'""".format(eventID,formatted_date,eventRoom,eventParticipants,eventTicketPrice))
            #fetch the results and store them
            try:
                eventDetails = cursor.fetchall()
                print(eventDetails)
            except IndexError:
                print("The event you are trying to delete does not exist in the event list ")
                connection.close()
                break
            try:
                headers = ("Event name","Date","Room info","Participants","Ticket price","Total donations")
                #stores the user inputs in an array that will be used to compare the results of the select statement
                fields_to_check = [eventID, formatted_date, eventRoom, eventParticipants, eventTicketPrice]
                
                # checks if all the results in eventDetails match the values in field_to_check all at once
                if all(eventDetails [0][i] == fields_to_check[i] for i in range (0-5)):

                    #prints the record that is going to be deleted and asks for a confirmation from the user before proceeding
                    print(tabulate(eventDetails,headers=headers))
                    while True:
                        confirmation = input("Is this the record you want to delete? y/n:")
                        if confirmation.lower() == "y":
                            cursor.execute ( """delete from events_history
                                where EventID  = '{}' 
                                and Date = '{}'
                                and RoomInfo ='{}'
                                and Participants ='{}'
                                and TicketPrice = '{}' """.format(eventID,formatted_date,eventRoom,eventParticipants,eventTicketPrice))
                            break
                        elif confirmation.lower() == "n" :
                            print("Ok")
                            break
                        else:
                            print("Reply with y or n")
                else:
                    print("Cant find any event instance with the details given, make sure write correctly the details")

            except IndexError:
                print("Cant find any event instance with the details given, make sure write correctly the details")


            
            connection.commit()
            confirmation =  input("Do you want to remove another volunteer? y/n: ")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
        except ValueError:
            print("Dont insert letters")

#this removes an event from the event list table
def deleteEvent():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        cursor.execute("PRAGMA foreign_keys=1")
        k_eventName = input("Insert the name of the event you want to delete: ")
        try: #Tries to delete the event from the database
            cursor.execute("""DELETE from events WHERE EventName = '{}'""".format(k_eventName))
            connection.commit()
            confirmation =  input("Do you want to remove another event? y/n: ")
            if confirmation.lower() == "n":
                    connection.close()
                    break
            else:
                    print("ok")
        except db.IntegrityError: #this exception run if the event has an instance in the event history table
            ("You cannot remove this event, you need to remove all the instances of this event from the events history table")
            break