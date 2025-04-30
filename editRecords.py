import sqlite3 as db
from tabulate import tabulate as tb
from datetime import datetime
import time
def editDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    
    k_id = int(input("Insert the ID of the donator whose details you want to edit: \n"))
    while True:
           try: 
                
            while True:
            #this selects the ID that matches the user input, and the fecth the result and store them in IDcheck
               
                cursor.execute("""SELECT ID from donators WHERE ID = '{}'""".format(k_id))
                
                
                #if the ID inserted by the user is not present in the database, this if statement runs
                try:
                    IDcheck = cursor.fetchall()[0][0]
                    if k_id != IDcheck:
                            print("There is no volunteer with the ID:",k_id )
                            break
                    else:
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
                            try:
                                k_housenumber = int(input("Insert the new house number: "))
                                cursor.execute( """UPDATE donators
                                            SET HouseNumber ='{}'
                                            WHERE ID = '{}'""".format(k_housenumber,k_id))
                            except ValueError:
                                 print("Insert only whole numbers")
                        if UserChoice == 4:
                            try:
                                k_phone = int(input("Insert the new phone number: "))
                                cursor.execute( """UPDATE donators
                                            SET PhoneNumber ='{}'
                                            WHERE ID = '{}'
                                            """.format(k_phone,k_id))
                            except:
                                 print("Insert only whole numbers")
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
                            return
                except IndexError:
                    print("There is no volunteer with the ID:",k_id )
                    time.sleep(1.5)
                    return
                    
                
           except ValueError:
               ("Please dont use letters!\n")
               time.sleep(1.5)

        

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
                    break
            
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
                            try:
                                k_housenumber = int(input("Insert the new house number: "))
                                cursor.execute( """UPDATE volunteers
                                            SET HouseNumber ='{}'
                                            WHERE ID = '{}'
                                            """.format(k_housenumber,k_id))
                            except ValueError:
                                 print("Insert only whole numbers")
                        
                        if UserChoice == 4:
                            try:
                                k_phone = int(input("Insert the new phone number: "))
                                cursor.execute( """UPDATE volunteers
                                            SET PhoneNumber ='{}'
                                            WHERE ID = '{}'
                                            """.format(k_phone,k_id))
                            except ValueError:
                                print("Insert only whole numbers")
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
                                return
                        if UserChoice > 6 or UserChoice < 0:
                            print("Choose one of the options listed above!")
                    except ValueError:
                        print("Dont use letters!")
        
    except IndexError:
        print("This ID does not exists in the database, make sure to spell correctly")
              

def editDonations(k_id = None,k_amount = None,formatted_date = None):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    while True:
        try: 
            if k_id == None:   
                k_id = int(input("Insert the id of the donator: "))  
            if formatted_date == None:
                while True:#forces the user to use the yyyy-mm-dd format
                        k_date = input("Insert the date when the donation happened (yyyy-mm-dd): ")
                        try:
                            formatted_date = datetime.strptime(k_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                            break 
                        except ValueError:
                            print("Invalid date format. Please use yyyy-mm-dd.")
            if k_amount == None:
                k_amount = float(input("Insert the amount that was donated: "))
            

            #this unites the volunteers and donor donations table, then selects rows where there is data that matches the user values input
            cursor.execute("""select DonatorID,Date,Amount, 'Donor' as Role  from donor_donations 
                                   where DonatorID ='{}'
                                   and Date ='{}'
                                   AND Amount = '{}'
                                   UNION
                                   select VolunteerID,Date,Amount, 'Volunteer' as Role from volunteers_donations 
                                   where VolunteerID ='{}'
                                   and Date ='{}'
                                   AND Amount ='{}'""".format(k_id,formatted_date,k_amount,k_id,formatted_date,k_amount))
            FetchDetails = cursor.fetchall()

                    
            if FetchDetails:
                        if FetchDetails[0][3] == 'Donor': # If found, check if the donation came from a 'Donor'
                            while True:
                                choice = int(input("Insert 1 to change the date, insert 2 to change the amount that was donated: "))
                                if choice == 2:
                                    new_amount = float(input("Insert the new amount of money"))
                                    cursor.execute("""UPDATE donor_donations
                                        SET Amount = '{}' 
                                        WHERE DonatorID ='{}'
                                        AND Date = '{}'
                                        AND Amount ='{}'""".format(new_amount,k_id,formatted_date,k_amount))
                                    k_amount = new_amount
                                    break
                                if choice == 1:
                                    
                                        try:
                                            new_date = input("Insert the new date in the format yyyy-mm-dd")
                                        
                                            new_format = datetime.strptime(new_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                                            cursor.execute("""UPDATE donor_donations
                                            SET Date = '{}' 
                                            WHERE DonatorID ='{}'
                                            AND Date = '{}'
                                            AND Amount ='{}'""".format(new_format,k_id,formatted_date,k_amount))
                                            formatted_date = new_format
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please use yyyy-mm-dd.")
                                        
                        if FetchDetails[0][3] == 'Volunteer': # If found, check if the donation came from a 'Volunteer'
                            while True:
                                try:
                                    choice = int(input("Insert 1 to change the date, insert 2 to change the amount that was donated: "))
                                    if choice == 2:
                                        new_amount = float(input("Insert the new amount of money"))
                                        cursor.execute("""UPDATE volunteers_donations
                                            SET Amount = '{}' 
                                            WHERE VolunteerID ='{}'
                                            AND Date = '{}'
                                            AND Amount ='{}'""".format(new_amount,k_id,formatted_date,k_amount))
                                        k_amount = new_amount
                                        break
                                    if choice == 1:
                                            try:
                                                new_date = input("Insert the new date in the format yyyy-mm-dd")
                                        
                                                new_format = datetime.strptime(new_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                                                cursor.execute("""UPDATE volunteers_donations
                                                    SET Date = '{}' 
                                                    WHERE VolunteerID ='{}'
                                                    AND Date = '{}'
                                                    AND Amount ='{}'""".format(new_format,k_id,formatted_date,k_amount))
                                                formatted_date = new_format
                                                break
                                            except ValueError:
                                                print("Use the format yyyy-mm-dd")
                                except ValueError:
                                    print("Dont use letters, dont use decimals unless inserting monetary value")
                            

                                
            if not FetchDetails:
                        print("There is no donations in database with the details you have given!")
                    
            connection.commit()
            confirmation = input("Do you want to edit something else? y/n:")
            if confirmation.lower() == "n":
                connection.close()
                break
            else:
                print("ok")
                k_id = None
                k_amount= None
                formatted_date = None
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
        connection.commit()
        confirmation = input("Do you want to edit another record? y/n: ")
        if confirmation.lower() == "n":
            connection.close()
            break
        else:
            print("ok")
    


def editEventsInstances(k_eventID = None, formatted_date = None, k_room = None, k_participants = None, k_price = None,k_total = None):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    try:
        if k_eventID == None:
            k_eventname = input("Insert the name of the event you want to edit: ")
        if formatted_date == None:
            while True:#this ensures that the user uses yyyy-mm-dd format
                    k_date = input("Insert the date when the event happened (yyyy-mm-dd): ")
                    try:
                        formatted_date = datetime.strptime(k_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                        break 
                    except ValueError:
                        print("Invalid date format. Please use yyyy-mm-dd.")
        if k_room == None:
            k_room = input("Insert the number of the room where the event was hosted: ")
        if k_participants == None:
            k_participants = int(input("How many participants were at the event?: "))
        if k_price == None:
            k_price = float(input("How much did the ticket for the event cost?: "))
        if k_total == None:
            k_total = k_participants * k_price
        
        if k_eventID == None:
            cursor.execute("""SELECT EventID from events WHERE EventName = '{}'""".format(k_eventname))
            k_eventID = cursor.fetchall()[0][0]
        #selects rows based on the user input
        cursor.execute("""SELECT events.EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history 
                     JOIN events ON events_history.EventID = events.EventID
                    where events_history.EventID = '{}'
                    AND Date ='{}'
                    AND RoomInfo = '{}'
                    AND Participants ='{}'
                    AND TicketPrice ='{}'
                    AND TotalDonations ='{}'""".format(k_eventID,formatted_date,k_room,k_participants,k_price,k_total))
            
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
                    print("Insert 0 if you finished and want to go back")
                    UserChoice = int(input("Choose one of details you want to edit: "))
                    try:
                        if UserChoice == 1:
                            new_eventName = input("change the name of the event: ")
                            cursor.execute("""Select EventID from events WHERE EventName ='{}'""".format(new_eventName))
                            new_eventID = cursor.fetchall()[0][0]
                            if new_eventID:
                                #Updates the row selected with a new event name
                                cursor.execute( """UPDATE events_history
                                            SET EventID ='{}'
                                            WHERE EventID = '{}'
                                            AND Date ='{}'
                                            AND RoomInfo = '{}'
                                            AND Participants ='{}'
                                            AND TicketPrice ='{}'
                                            AND TotalDonations ='{}'
                                            """.format(new_eventID,k_eventID,formatted_date,k_room,k_participants,k_price,k_total))
                                k_eventID = new_eventID
                            else:
                                ("There is no event with that name, make sure the that it is in the event list")
                    
                        if UserChoice == 2:
                            while True:
                                new_date = input("Insert the date when the event happened (yyyy-mm-dd): ")
                                try:
                                    new_format = datetime.strptime(new_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                                    #Updates the row selected with a new date
                                    cursor.execute( """UPDATE events_history
                                        SET Date ='{}'
                                        WHERE EventID = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                    """.format(new_date,k_eventID,new_format,k_room,k_participants,k_price,k_total))
                                    formatted_date = new_format
                                    break 
                                except ValueError:
                                    print("Invalid date format. Please use yyyy-mm-dd.")
                                
                        
                        if UserChoice == 3:
                            new_roomnumber = input("Insert the new room number: ")
                            #Updates the row selected with a room number
                            cursor.execute( """UPDATE events_history
                                        SET RoomInfo ='{}'
                                        WHERE EventID = '{}'
                                        AND Date ='{}'
                                        AND RoomInfo = '{}'
                                        AND Participants ='{}'
                                        AND TicketPrice ='{}'
                                        AND TotalDonations ='{}'
                                        """.format(new_roomnumber,k_eventID,formatted_date,k_room,k_participants,k_price,k_total))
                            k_room = new_roomnumber
                        
                        if UserChoice == 4:
                            while True:
                                 try:
                                    new_participants = int(input("Insert the new number of participants: "))
                                    #This will calculate the new amount of total donations, 
                                    #by multiplying the new number of participants with current ticket price
                                    new_total = new_participants * k_price
                                    #Updates the row selected with a new number of participants
                                    cursor.execute( """UPDATE events_history
                                                SET Participants ='{}'
                                                WHERE EventID = '{}'
                                                AND Date ='{}'
                                                AND RoomInfo = '{}'
                                                AND Participants ='{}'
                                                AND TicketPrice ='{}'
                                                AND TotalDonations ='{}'
                                                """.format(new_participants,k_eventID,formatted_date,k_room,k_participants,k_price,k_total))
                                    #Updates the row selected with the new amount of total donations
                                    cursor.execute("""UPDATE events_history 
                                                SET TotalDonations = '{}'
                                                WHERE EventID = '{}'
                                                AND Date ='{}'
                                                AND RoomInfo = '{}'
                                                AND Participants ='{}'
                                                AND TicketPrice ='{}'
                                                AND TotalDonations ='{}'""".format(new_total,k_eventID,formatted_date,k_room,new_participants,k_price,k_total))
                                    k_participants = new_participants
                                    k_total = new_total
                                    break
                                 except ValueError:
                                     print("Dont use letters, use decimals only when inserting monetary values")
                        if UserChoice == 5:
                            while True:
                                 try:
                                    new_price = float((input("Insert the new ticket price: ")))
                                    #This will calculate the new amount of total donations, 
                                    #by multiplying the new ticket cost with current number of participants
                                    new_total = k_participants * new_price
                                    #Updates the row selected with the new ticket cost
                                    cursor.execute( """UPDATE events_history
                                                SET TicketPrice ='{}'
                                                WHERE EventID = '{}'
                                                AND Date ='{}'
                                                AND RoomInfo = '{}'
                                                AND Participants ='{}'
                                                AND TicketPrice ='{}'
                                                AND TotalDonations ='{}'
                                                """.format(new_price,k_eventID,formatted_date,k_room,k_participants,k_price,k_total))
                                    #Updates the row selected with a new amount of total donations
                                    cursor.execute( """UPDATE events_history
                                                SET TotalDonations ='{}'
                                                WHERE EventID = '{}'
                                                AND Date ='{}'
                                                AND RoomInfo = '{}'
                                                AND Participants ='{}'
                                                AND TicketPrice ='{}'
                                                AND TotalDonations ='{}'
                                                """.format(new_total,k_eventID,formatted_date,k_room,k_participants,new_price,k_total))
                                    k_price = new_price
                                    k_total = new_total
                                    break
                                 except ValueError:
                                     print("Dont use letters, use decimals only when inserting monetary values")
                        connection.commit()
                        if UserChoice == 0:
                            connection.close()
                            break
                        if UserChoice > 5 or UserChoice < 0:
                            print("Please select one of the options listed")
                    except ValueError:
                        ("Dont use letters!")
    except ValueError:
        print("Dont use letters")