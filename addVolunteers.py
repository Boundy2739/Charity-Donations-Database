import sqlite3 as db

def addVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_ID = int(input("Insert the ID: "))
    k_name = input("Insert the name and surname of the Volunteer: ")
    k_address = input("Insert the name of the street where they live: ")
    k_housenumber = int(input("Insert the house number"))
    k_postcode = input("Insert the postcode: ")
    k_phonenumber = int(input("Insert their phone number: "))
    k_email = input("Insert the email: ")
    cursor.execute("""INSERT into volunteers VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(k_ID,k_name,k_address,k_housenumber,k_postcode,k_phonenumber,k_email))
    connection.commit()
    connection.close()