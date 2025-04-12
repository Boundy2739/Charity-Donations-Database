import sqlite3 as db
def deletebyEvent(EventName):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    cursor.execute ( """delete from donations
    where SourceEvent  = '{}' """.format(EventName))
    connection.commit()
    connection.close()

def deleteByDonator(DonatorID):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    cursor.execute ( """delete from donations
     where ID = '{}' """.format(DonatorID))
    connection.commit()
    connection.close()