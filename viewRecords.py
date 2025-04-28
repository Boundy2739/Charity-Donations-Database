import sqlite3 as db
from tabulate import tabulate
def viewDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from donators""")
    data = cursor.fetchall()
    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email","To be removed"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def viewDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from donations""")
    data = cursor.fetchall()
    headers = ["Donor ID","Volunteer ID","Amount donated","Date"]
    print(tabulate(data, headers=headers, tablefmt="grid"))


def viewEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history""")
    data = cursor.fetchall()
    headers = ["Event name","Date","Room info","Participants","Ticket price","Total donations"]
    print(tabulate(data, headers=headers, tablefmt="grid"))