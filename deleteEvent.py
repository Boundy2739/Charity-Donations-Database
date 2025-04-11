import sqlite3 as db
def deleteEvent():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    eventName = str(input("Insert the name of the event you want to delete: "))
    eventDate = str(input("Insert the date of the event you want to delete: "))
    cursor.execute ( """delete from events
    where EventName  = '{}' 
    and Date = '{}'""".format(eventName,eventDate))
    connection.commit()
    connection.close()