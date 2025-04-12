import sqlite3 as db

def addDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_id= int(input("Insert the donator's ID: "))
    k_eventsource= str(input("Insert the name of the event from which came the donation: "))
    k_amount = float(input("Insert the amount donated: "))
    k_date = str(input("Insert the date of the donation: "))
    cursor.execute("""insert into donations VALUES ('{}','{}','{}','{}')""".format(k_id,k_eventsource,k_amount,k_date))
    connection.commit()
    connection.close()
