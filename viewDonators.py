import sqlite3 as db
from tabulate import tabulate
def viewDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from donators""")
    data = cursor.fetchall()
    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email","To be removed"]
    print(tabulate(data, headers=headers, tablefmt="grid"))