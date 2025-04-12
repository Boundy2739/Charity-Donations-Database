import sqlite3 as db
from tables import *

def addEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_eventName = str(input("Insert the name of the event:"))
    k_date = str(input("Insert the date of the event: "))
    k_room = str(input("In which room is the event going to take place: "))
    k_participants = int(input("Insert the number of participants that will be there: "))
    k_price = float(input("Insert the price of the ticket: "))
    cursor.execute("""insert into events(EventName,Date,RoomInfo,Participants,TicketPrice) VALUES ('{}','{}','{}','{}','{}')""".format(k_eventName,k_date,k_room,k_participants,k_price))
   
    connection.commit()
    connection.close()

