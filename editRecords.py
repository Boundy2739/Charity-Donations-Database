import sqlite3 as db
from tabulate import tabulate as tb
def editDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    editingRecords = 1
    k_id = int(input("Insert the ID of the donator whose details you want to edit: \n"))
    while editingRecords == 1:
        

        
        print("Insert 1 if you want to edit the name of the donator")
        print("Insert 2 if you want to edit the address of the donator")
        print("Insert 3 if you want to edit the house number of the donator")
        print("Insert 4 if you want to edit the phone number of the donator")
        print("Insert 5 if you want to edit the email of the donator")
        print("Insert 6 if you want to edit the postcode of the donator")
        print("Insert 7 if you have finished editing or you want to go back\n")
        
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
            
            editingRecords = 0
        
        

        #k_address = str(input("put your adress: "))
        #k_housenumber = str(input("put your housenum: "))
        #k_postcode = str(input("put your postcode: "))
        #k_phone = str(input("put your phone: "))
        #k_email = str((input("put email: ")))
        
        



def editVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    editingRecords = 1
    k_id = int(input("Insert the ID of volunteer whose details you want to edit: "))
    while editingRecords == 1:
        
        cursor.execute("SELECT ID from volunteers WHERE ID = '{}'".format(k_id))
        IDcheck = cursor.fetchall()
        try:
            if k_id != IDcheck[0][0]:
                print("There is no volunteer with such ID")
                return
        
            else:
                print("Insert 1 to edit the name of the volunteer")
                print("Insert 2 to edit the address of the volunteer")
                print("Insert 3 to edit the house number of the volunteer")
                print("Insert 4 to edit the phone number of the volunteer")
                print("Insert 5 to edit the email of the volunteer")
                print("Insert 6 to edit the postcode of the volunteer")
                print("Insert 0 if you have finished editing or if you want to go back\n")

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
            
                        editingRecords = 0
        except IndexError:
            print("This ID does not exists in the database, make sure to spell correctly")
            return  


def editDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    print("Insert 1 if you want to edit a donation coming from a donator\n")
    UserChoice = int(input("Choose an option: "))
    if UserChoice == 1:
        k_id = int(input("Insert the id of the donator: "))
        k_role = input("Is the donor a volunteer? y/n: ")
        if k_role.lower() == "y":
            k_date = str(input("Insert the date when the donation happened:  "))
            cursor.execute("""select VolunteerID from volunteers_donations where VolunteerID ='{}'""".format(k_id))
            idcheck = cursor.fetchmany(1)
            print("diqkmdqimd", idcheck)
            if not idcheck:
                print("There is no such donation in the database")
            if idcheck:
                cursor.execute("""select Date from volunteers_donations where Date ='{}'""".format(k_date))
                datecheck = cursor.fetchall()
                if datecheck:
                    k_amount = float(input("Insert the new amount of money"))
                    cursor.execute("""UPDATE volunteers_donations
                        SET Amount = '{}' 
                        WHERE VolunteerId ='{}'
                        AND Date = '{}'""".format(k_amount,k_id,k_date))
                if not datecheck:
                    print("There is no donations in database with the details you have given!")
        else:   
            k_date = str(input("Insert the date when the donation happened:  "))
            cursor.execute("""select DonatorID from donor_donations where DonatorID='{}'""".format(k_id))
            idcheck = cursor.fetchall()
            print("diqkmdqimd", idcheck)
            if not idcheck:
                print("There is no such donation in the database")
            if idcheck:
                cursor.execute("""select Date from donor_donations where Date ='{}'""".format(k_date))
                datecheck = cursor.fetchall()
                if datecheck:
                    k_amount = float(input("Insert the new amount of money"))
                    cursor.execute("""UPDATE donor_donations
                        SET Amount = '{}' 
                        WHERE DonatorID ='{}'
                        AND Date = '{}'""".format(k_amount,k_id,k_date))
                if not datecheck:
                    print("There is no donations in database with the details you have given!")
                
    connection.commit()
    connection.close()       


def editEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    editingRecords = 1
    while editingRecords == 1:
        cursor.execute("PRAGMA foreign_keys=1")
        k_eventName = input("Please insert the name of the event you want to edit: ")
        cursor.execute("""SELECT EventName FROM events WHERE EventName = '{}'""".format(k_eventName))
        checkName = cursor.fetchall()
        if not checkName:
            print("There is no such event in the database!")
        else:
            new_eventName = input("Insert the new name of the event: ")
            cursor.execute("""UPDATE events SET EventName = '{}'
                           WHERE EventName = '{}'""".format(new_eventName,k_eventName))
            cursor.execute("""UPDATE events_history SET EventName = '{}'
                           WHERE EventName = '{}'""".format(new_eventName,k_eventName))
        connection.commit()
        confirmation = input("Do you want to edit another record? y/n: ")
        if confirmation.lower() == "n":
            connection.close()
            editingRecords = 0
        else:
            print("ok")
    


def editEventsInstances():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_eventname = input("Insert the name of the event you want to edit: ")
    k_date = input("Insert the date when the event happened: ")
    k_room = input("Insert the number of the room where the event was hosted: ")
    k_participants = int(input("How many participants were at the event?: "))
    k_price = float(input("How much did the ticket for the event cost?: "))
    k_total = k_participants * k_price
    cursor.execute("""SELECT * from events_history where EventName = '{}'
                   AND Date ='{}'
                   AND RoomInfo = '{}'
                   AND Participants ='{}'
                   AND TicketPrice ='{}'
                   AND TotalDonations ='{}'""".format(k_eventname,k_date,k_room,k_participants,k_price,k_total))
        
    headers = ["Event name","Date","Room info","Participants","Ticket price","Total donations","EventID"]
    eventToEdit = cursor.fetchall()
    if not eventToEdit:
        print("This is empty!!")
    else:
        print(tb(eventToEdit,headers=headers,tablefmt="grid"))
    confirmation = input("Is this the event history you want to edit? y/n: ")
    if confirmation.lower() == "y":
        print("ok")
        print("Insert 1 if you want to edit the name of the event\n")
        print("Insert 2 if you want to edit the date of the event\n")
        print("Insert 3 if you want to edit the room number of the event\n")
        print("Insert 4 if you want to edit the number of participants\n")
        print("Insert 5 if you want to edit the price of the ticket\n")
        print("Insert 6 if you want to edit the ID of the event\n")
        print("Insert 0 if you want to go back")
        UserChoice = int(input("Choose one of details you want to edit: "))

        if UserChoice == 1:
            new_eventName = input("Insert the new name of the event: ")
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
            new_date = input("Insert the new date: ")
            cursor.execute( """UPDATE events_history
                        SET Date ='{}'
                        WHERE EventName = '{}'
                        AND Date ='{}'
                        AND RoomInfo = '{}'
                        AND Participants ='{}'
                        AND TicketPrice ='{}'
                        AND TotalDonations ='{}'
                    """.format(new_date,k_eventname,k_date,k_room,k_participants,k_price,k_total))
        
        if UserChoice == 3:
            new_roomnumber = str(input("Insert the new room number: "))
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
            new_total = new_participants * k_price
            cursor.execute( """UPDATE events_history
                        SET Participants ='{}'
                        WHERE EventName = '{}'
                        AND Date ='{}'
                        AND RoomInfo = '{}'
                        AND Participants ='{}'
                        AND TicketPrice ='{}'
                        AND TotalDonations ='{}'
                        """.format(new_participants,k_eventname,k_date,k_room,k_participants,k_price,k_total))
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
            new_total = k_participants * new_price
            cursor.execute( """UPDATE events_history
                        SET TicketPrice ='{}'
                        WHERE EventName = '{}'
                        AND Date ='{}'
                        AND RoomInfo = '{}'
                        AND Participants ='{}'
                        AND TicketPrice ='{}'
                        AND TotalDonations ='{}'
                        """.format(new_price,k_eventname,k_date,k_room,k_participants,k_price,k_total))
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
    connection.close()