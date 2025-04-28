import sqlite3 as db
from tabulate import tabulate
def viewDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from donations""")
    data = cursor.fetchall()
    headers = ["Donor ID","Volunteer ID","Amount donated","Date"]
    print(tabulate(data, headers=headers, tablefmt="grid"))