import sqlite3 as db
from tables import *

def addEventsHistory():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_eventName = input("Insert the name of the event:")
    k_date = input("Insert the date of the event: ")
    k_room = input("In which room is the event going to take place: ")
    k_participants = int(input("Insert the number of participants that will be there: "))
    k_price = float(input("Insert the price of the ticket: "))
    k_total = k_price * k_participants

    cursor.execute("""SELECT EventID from events WHERE EventName ='{}' """.format(k_eventName))
    k_eventID = cursor.fetchall()
    print(type(k_eventID[0]))

    cursor.execute("""insert into events_history(EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations,EventID) VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(k_eventName,k_date,k_room,k_participants,k_price,k_total,k_eventID[0][0]))
    
    connection.commit()
    connection.close()

