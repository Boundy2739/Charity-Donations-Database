import sqlite3 as db
from tabulate import tabulate as tb
from datetime import datetime
def editDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    
    k_id = int(input("Insert the ID of the donator whose details you want to edit: \n"))
    while True:
           try: 

            
                print("Insert 1 if you want to edit the name of the donator")
                print("Insert 2 if you want to edit the address of the donator")
                print("Insert 3 if you want to edit the house number of the donator")
                print("Insert 4 if you want to edit the phone number of the donator")
                print("Insert 5 if you want to edit the email of the donator")
                print("Insert 6 if you want to edit the postcode of the donator")
                print("Insert 0 if you have finished editing or you want to go back\n")
                
                UserChoice = int(input("Choose one of details you want to edit: "))

                if UserChoice == 1:
                    k_name = str(input("put your name: "))
                    cursor.execute( """UPDATE donators
                                SET Name ='{}'
                                WHERE ID = '{}'
                                """.format(k_name,k_id))
                
                if UserChoice == 2:
                    k_address = str(input("Insert the new address: "))
                    cursor.execute( """UPDATE donators
                            SET Address ='{}'
                            WHERE ID = '{}'
                            """.format(k_address,k_id))
                
                if UserChoice == 3:
                    k_housenumber = str(input("Insert the new house number: "))
                    cursor.execute( """UPDATE donators
                                SET HouseNumber ='{}'
                                WHERE ID = '{}'
                                """.format(k_housenumber,k_id))
                
                if UserChoice == 4:
                    k_phone = str(input("Insert the new phone number: "))
                    cursor.execute( """UPDATE donators
                                SET PhoneNumber ='{}'
                                WHERE ID = '{}'
                                """.format(k_phone,k_id))
                if UserChoice == 5:
                    k_email = str((input("Insert the new email: ")))
                    cursor.execute( """UPDATE donators
                                SET Email ='{}'
                                WHERE ID = '{}'
                                """.format(k_email,k_id))
                if UserChoice == 6:
                    k_postcode = (input("Insert the new postcode: "))
                    cursor.execute( """UPDATE donators
                                SET Postcode ='{}'
                                WHERE ID = '{}'
                                """.format(k_postcode,k_id))
                connection.commit()
                
                if UserChoice == 0:
                    print("Finished editing")
                    connection.close()
                    
                    break
           except ValueError:
               ("Please dont use letters!")
        

        #k_address = str(input("put your adress: "))
        #k_housenumber = str(input("put your housenum: "))
        #k_postcode = str(input("put your postcode: "))
        #k_phone = str(input("put your phone: "))
        #k_email = str((input("put email: ")))
        
        



def editVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    try:
        k_id = int(input("Insert the ID of volunteer whose details you want to edit: "))
        while True:
            #this selects the ID that matches the user input, and the fecth the result and store them in IDcheck
            cursor.execute("SELECT ID from volunteers WHERE ID = '{}'".format(k_id))
            IDcheck = cursor.fetchall()
            
            #if the ID inserted by the user is not present in the database, this if statement runs
            if k_id != IDcheck[0][0]:
                    print("There is no volunteer with such ID")
                    return
            
            #if the ID is present, the user can than access the edit options
            else: 
                    print("Insert 1 to edit the name of the volunteer")
                    print("Insert 2 to edit the address of the volunteer")
                    print("Insert 3 to edit the house number of the volunteer")
                    print("Insert 4 to edit the phone number of the volunteer")
                    print("Insert 5 to edit the email of the volunteer")
                    print("Insert 6 to edit the postcode of the volunteer")
                    print("Insert 0 if you have finished editing or if you want to go back\n")
                    try:
                        UserChoice = int(input("Choose an option: "))
                        if UserChoice == 1:
                            k_name = str(input("put your name: "))
                            cursor.execute("""UPDATE volunteers
                                        SET Name ='{}'
                                        WHERE ID = '{}'
                                        """.format(k_name,k_id))
                    
                        if UserChoice == 2:
                            k_address = str(input("Insert the new address: "))
                            cursor.execute( """UPDATE volunteers
                                    SET Address ='{}'
                                    WHERE ID = '{}'
                                    """.format(k_address,k_id))
                        
                        if UserChoice == 3:
                            k_housenumber = str(input("Insert the new house number: "))
                            cursor.execute( """UPDATE volunteers
                                        SET HouseNumber ='{}'
                                        WHERE ID = '{}'
                                        """.format(k_housenumber,k_id))
                        
                        if UserChoice == 4:
                            k_phone = str(input("Insert the new phone number: "))
                            cursor.execute( """UPDATE volunteers
                                        SET PhoneNumber ='{}'
                                        WHERE ID = '{}'
                                        """.format(k_phone,k_id))
                        if UserChoice == 5:
                            k_email = str((input("Insert the new email: ")))
                            cursor.execute( """UPDATE volunteers
                                        SET Email ='{}'
                                        WHERE ID = '{}'
                                        """.format(k_email,k_id))
                        if UserChoice == 6:
                            k_postcode = (input("Insert the new postcode: "))
                            cursor.execute( """UPDATE volunteers
                                        SET Postcode ='{}'
                                        WHERE ID = '{}'
                                        """.format(k_postcode,k_id))
                        connection.commit()
                        if UserChoice == 0:
                                print("Finished editing")
                                connection.close()
                                break
                        if UserChoice > 6 or UserChoice < 0:
                            print("Choose one of the options listed above!")
                    except ValueError:
                        print("Dont use letters!")
        
    except IndexError:
        print("This ID does not exists in the database, make sure to spell correctly")
              

def editDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try:    
            k_id = int(input("Insert the id of the donator: "))  
            while True:#forces the user to use the yyyy-mm-dd format
                k_date = input("Insert the date when the donation happened (yyyy-mm-dd): ")
                try:
                    datetime.strptime(k_date, "%Y-%m-%d")
                    break 
                except ValueError:
                    print("Invalid date format. Please use yyyy-mm-dd.")
            k_amount = float(input("Insert the amount that was donated: "))

            #selects the ID that matches the user input
            cursor.execute("""select DonatorID from donor_donations where DonatorID='{}'
                               UNION
                               select VolunteerID from volunteers_donations where VolunteerID ='{}'""".format(k_id,k_id))
            #fetch the results and store them
            idcheck = cursor.fetchall()
            
            #if the result is empty this runs
            if not idcheck:
                    print("There is no such donation in the database")
            
            if idcheck:
                    #this unites the volunteers and donor donations table, then selects rows where the data matches the user input
                    cursor.execute("""select Date,Amount, 'Donor' as Role  from donor_donations where Date ='{}'
                                   AND Amount = '{}'
                                   UNION
                                   select Date,Amount, 'Volunteer' as Role from volunteers_donations where Date ='{}'
                                   AND Amount ='{}'""".format(k_date,k_amount,k_date,k_amount))
                    CheckDetails = cursor.fetchall()
                    
                    if CheckDetails:
                        if CheckDetails[0][2] == 'Donor': # If found, check if the donation came from a 'Donor'
                            while True:
                                choice = int(input("Insert 1 to change the date, insert 2 to change the amount that was donated: "))
                                if choice == 2:
                                    new_amount = float(input("Insert the new amount of money"))
                                    cursor.execute("""UPDATE donor_donations
                                        SET Amount = '{}' 
                                        WHERE DonatorID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(new_amount,k_id,k_date,k_amount))
                                    break
                                if choice == 1:
                                    new_date = input("Insert the new date in the format yyyy-mm-dd")
                                    try:
                                        datetime.strptime(k_date, "%Y-%m-%d")
                                        break 
                                    except ValueError:
                                        print("Invalid date format. Please use yyyy-mm-dd.")
                                    cursor.execute("""UPDATE donor_donations
                                        SET Date = '{}' 
                                        WHERE DonatorID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(new_date,k_id,k_date,k_amount))
                                    break
                        if CheckDetails[0][2] == 'Volunteer': # If found, check if the donation came from a 'Volunteer'
                            while True:
                                choice = int(input("Insert 1 to change the date, insert 2 to change the amount that was donated: "))
                                if choice == 2:
                                    new_amount = float(input("Insert the new amount of money"))
                                    cursor.execute("""UPDATE volunteers_donations
                                        SET Amount = '{}' 
                                        WHERE VolunteerID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(new_amount,k_id,k_date,k_amount))
                                    break
                                if choice == 1:
                                    new_amount = input("Insert the new date in the format yyyy-mm-dd")
                                    cursor.execute("""UPDATE volunteers_donations
                                        SET Date = '{}' 
                                        WHERE VolunteerID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(new_amount,k_id,k_date,k_amount))
                                    break


                                
                    if not CheckDetails:
                        print("There is no donations in database with the details you have given!")
                    
            connection.commit()
            confirmation = input("Do you want to edit something else? y/n:")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
        except ValueError:
            print("Dont use letters when insert an ID or a monetray value!")
            break   


def editEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        cursor.execute("PRAGMA foreign_keys=1")
        k_eventName = input("Please insert the name of the event you want to edit: ")
        cursor.execute("""SELECT EventName FROM events WHERE EventName = '{}'""".format(k_eventName))
        #fetch the result select statement and store it in checkName
        checkName = cursor.fetchall()
        if not checkName:#runs if nothing was found
            print("There is no such event in the database!")
        else:#runs if there is a result
            new_eventName = input("Insert the new name of the event: ")
            cursor.execute("""UPDATE events SET EventName = '{}'
                           WHERE EventName = '{}'""".format(new_eventName,k_eventName))
            cursor.execute("""UPDATE events_history SET EventName = '{}'
                           WHERE EventName = '{}'""".format(new_eventName,k_eventName))
        connection.commit()
        confirmation = input("Do you want to edit another record? y/n: ")
        if confirmation.lower() == "n":
            connection.close()
            break
        else:
            print("ok")
    


def editEventsInstances():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    try:
        k_eventname = input("Insert the name of the event you want to edit: ")
        while True:#this ensures that the user uses yyyy-mm-dd format
                k_date = input("Insert the date when the event happened (yyyy-mm-dd): ")
                try:
                    datetime.strptime(k_date, "%Y-%m-%d")
                    break 
                except ValueError:
                    print("Invalid date format. Please use yyyy-mm-dd.")
        k_room = input("Insert the number of the room where the event was hosted: ")
        k_participants = int(input("How many participants were at the event?: "))
        k_price = float(input("How much did the ticket for the event cost?: "))
        k_total = k_participants * k_price
        #selects rows based on the user input
        cursor.execute("""SELECT * from events_history where EventName = '{}'
                    AND Date ='{}'
                    AND RoomInfo = '{}'
                    AND Participants ='{}'
                    AND TicketPrice ='{}'
                    AND TotalDonations ='{}'""".format(k_eventname,k_date,k_room,k_participants,k_price,k_total))
            
        #these are the names of the headers that will be shown when printing the results using tabulate
        headers = ["Event name","Date","Room info","Participants","Ticket price","Total donations","EventID"]
        #fetch results and store them
        eventToEdit = cursor.fetchall()
        if not eventToEdit:
            print("This is empty!!")
        else:
            #prints the results in eventsToEdit and ask the user if this the row they want to edit
            print(tb(eventToEdit,headers=headers,tablefmt="grid"))
            confirmation = input("Is this the event history you want to edit? y/n: ")
            if confirmation.lower() == "y":
                print("ok")
                while True:
                    print("Insert 1 if you want to edit the name of the event\n")
                    print("Insert 2 if you want to edit the date of the event\n")
                    print("Insert 3 if you want to edit the room number of the event\n")
                    print("Insert 4 if you want to edit the number of participants\n")
                    print("Insert 5 if you want to edit the price of the ticket\n")
                    print("Insert 6 if you want to edit the ID of the event\n")
                    print("Insert 0 if you want to go back")
                    UserChoice = int(input("Choose one of details you want to edit: "))
                    try:
                        if UserChoice == 1:
                            new_eventName = input("Insert the new name of the event: ")
                            #Updates the row selected with a new event name
                            cursor.execute( """UPDATE events_history
                                        SET EventName ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                        """.format(new_eventName,k_eventname,k_date,k_room,k_participants,k_price,k_total))
                    
                        if UserChoice == 2:
                            while True:
                                new_date = input("Insert the date when the event happened (yyyy-mm-dd): ")
                                try:
                                    datetime.strptime(new_date, "%Y-%m-%d")
                                    #Updates the row selected with a new date
                                    cursor.execute( """UPDATE events_history
                                        SET Date ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                    """.format(new_date,k_eventname,k_date,k_room,k_participants,k_price,k_total))
                                    break 
                                except ValueError:
                                    print("Invalid date format. Please use yyyy-mm-dd.")
                                
                        
                        if UserChoice == 3:
                            new_roomnumber = str(input("Insert the new room number: "))
                            #Updates the row selected with a room number
                            cursor.execute( """UPDATE events_history
                                        SET RoomInfo ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                        """.format(new_roomnumber,k_eventname,k_date,k_room,k_participants,k_price,k_total))
                        
                        if UserChoice == 4:
                            new_participants = int(input("Insert the new number of participants: "))
                            #This will calculate the new amount of total donations, 
                            #by multiplying the new number of participants with current ticket price
                            new_total = new_participants * k_price
                            #Updates the row selected with a new number of participants
                            cursor.execute( """UPDATE events_history
                                        SET Participants ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                        """.format(new_participants,k_eventname,k_date,k_room,k_participants,k_price,k_total))
                            #Updates the row selected with the new amount of total donations
                            cursor.execute("""UPDATE events_history 
                                        SET TotalDonations = '{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'""".format(new_total,k_eventname,k_date,k_room,new_participants,k_price,k_total))
                            k_participants = new_participants
                        if UserChoice == 5:
                            new_price = float((input("Insert the new ticket price: ")))
                            #This will calculate the new amount of total donations, 
                            #by multiplying the new ticket cost with current number of participants
                            new_total = k_participants * new_price
                            #Updates the row selected with the new ticket cost
                            cursor.execute( """UPDATE events_history
                                        SET TicketPrice ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                        """.format(new_price,k_eventname,k_date,k_room,k_participants,k_price,k_total))
                            #Updates the row selected with a new amount of total donations
                            cursor.execute( """UPDATE events_history
                                        SET TotalDonations ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                        """.format(new_total,k_eventname,k_date,k_room,k_participants,new_price,k_total))
                            k_price = new_price
                        if UserChoice == 6:
                            new_ID = (input("Insert the ID for the event: "))
                            cursor.execute( """UPDATE events_history
                                        SET EventID ='{}'
                                        WHERE EventName = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                    """.format(new_ID,k_eventname,k_date,k_room,k_participants,k_price,k_total))

                        connection.commit()
                        if UserChoice == 0:
                            connection.close()
                            break
                        if UserChoice > 6 or UserChoice < 0:
                            print("Please select one of the options listed")
                    except ValueError:
                        ("Dont use letters!")
    except ValueError:
        print("Dont use letters")