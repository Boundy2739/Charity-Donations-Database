import sqlite3 as db

def deleteEvent():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    k_eventName = input("Insert the name of the event you want to delete: ")
    cursor.execute("""DELETE from events WHERE EventName = '{}'""".format(k_eventName))
    connection.commit()
    connection.close()