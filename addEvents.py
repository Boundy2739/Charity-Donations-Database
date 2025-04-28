import sqlite3 as db
from tables import *

def addEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    k_eventName = input("Please insert the name of the event you want to add: ")
    cursor.execute("""INSERT INTO events (EventName) VALUES('{}')""".format(k_eventName))
    connection.commit()
    connection.close()
