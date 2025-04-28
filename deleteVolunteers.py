import sqlite3 as db
from tabulate import tabulate
def deleteVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    k_id = int(input("Insert the ID of volunteer you want to remove from the database: "))
    cursor.execute("""SELECT * from volunteers WHERE ID ='{}'""".format(k_id))
    IDcheck = cursor.fetchall()
    try:
        if k_id == IDcheck[0][0]:
            headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
            print(tabulate(IDcheck, headers=headers,tablefmt="grid"))
            confirmation = input("Is this the volunteer you want to delete? y/n: ")
            if confirmation == "y":
                try:
                    cursor.execute ( """delete from volunteers
                where ID = '{}' """.format(k_id))
                except db.IntegrityError:
                    print("You cant delete this volunteer until you have removed all the donations made by them from the database")
    except IndexError:
        print("This ID does not exists in the database, make sure to spell correctly")
    
    connection.commit()
    connection.close()