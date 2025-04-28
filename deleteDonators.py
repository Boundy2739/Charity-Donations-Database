import sqlite3 as db
from tabulate import tabulate
def DeleteDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    ID = int(input("Insert the ID of the donor you want to delete: "))
    cursor.execute("""SELECT * from donators WHERE ID = '{}'""".format(ID))
    IDCheck = cursor.fetchall()
    try:
        print(tabulate(IDCheck))
        if ID == IDCheck[0][0]:
            confirmation = input("Is this the donor you want to delete? y/n: ")
            if confirmation == "y":
                try:
                    cursor.execute ( """delete from donators 
                where ID = '{}' """.format(ID))
                except db.IntegrityError:
                    print("You cant delete this donator until you have removed all the donations made by them from the database")
    except IndexError:
        print("This ID does not exist in the database, make sure to write it correctly")
    connection.commit()
    connection.close()