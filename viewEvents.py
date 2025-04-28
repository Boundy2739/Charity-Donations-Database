import sqlite3 as db
from tabulate import tabulate
def viewEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT EventName,Date,RoomInfo,Participants,TicketPrice,TotalDonations from events_history""")
    data = cursor.fetchall()
    headers = ["Event name","Date","Room info","Participants","Ticket price","Total donations"]
    print(tabulate(data, headers=headers, tablefmt="grid"))