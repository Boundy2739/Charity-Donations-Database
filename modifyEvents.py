import sqlite3 as db
from tabulate import tabulate as tb

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

    
    