import sqlite3 as db
from tabulate import tabulate
def viewDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from donators""")
    data = cursor.fetchall()
    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()
def viewVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * from volunteers""")
    data = cursor.fetchall()
    headers = ["ID","Name","Address","House number","Postcode","Phone number","Email"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()

def viewDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT DonatorID,Amount,Date from donor_donations
                   UNION
                   SELECT VolunteerID,Amount,Date from volunteers_donations""")
    data = cursor.fetchall()
    headers = ["Donor ID","Amount donated","Date"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()


def viewEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history""")
    data = cursor.fetchall()
    headers = ["Event name","Date","Room info","Participants","Ticket price","Total donations"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    connection.close()