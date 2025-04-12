import sqlite3 as db
from tables import *

def addRecords():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_id= int(input("put your id: "))
    k_name = str(input("put your name: "))
    k_address = str(input("put your adress: "))
    k_housenumber = str(input("put your housenum: "))
    k_postcode = str(input("put your postcode: "))
    k_phone = str(input("put your phone: "))
    k_email = str((input("put email: ")))
    cursor.execute( """insert into donators VALUES ('{}','{}','{}','{}','{}','{}','{}',1)""".format(k_id,k_name,k_address,k_housenumber,k_postcode,k_phone,k_email))
    connection.commit()
    connection.close()


