import sqlite3 as db
from tabulate import tabulate
def deleteEventHistory():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
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
    connection.close()