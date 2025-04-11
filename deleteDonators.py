import sqlite3 as db
def DeleteRecords(UserID):
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    cursor.execute ( """delete from donators 
     where ID = '{}' """.format(UserID))
    connection.commit()
    connection.close()