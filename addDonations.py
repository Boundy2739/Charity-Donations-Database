import sqlite3 as db

def addDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_id= int(input("Insert the donator's ID: "))
    k_amount = float(input("Insert the amount donated: "))
    k_date = str(input("Insert the date of the donation: "))
    k_role = input("Is the donator a volunteer? y/n: ")
    if k_role.lower() == "y":
        cursor.execute("""Select ID FROM volunteers WHERE ID = '{}'""".format(k_id))
        checkIDs = cursor.fetchall()
        try:
            if checkIDs[0][0]== k_id:
                cursor.execute("""insert into donations (VolunteerID,Amount,Date) VALUES ('{}','{}','{}')""".format(k_id,k_amount,k_date))
        except IndexError:
            print("The ID you inserted does not exist in the database")
    else:
        cursor.execute("""Select ID FROM donators WHERE ID = '{}'""".format(k_id))
        checkIDs = cursor.fetchall()
        try:
            if checkIDs[0][0]== k_id:
                cursor.execute("""insert into donations (DonatorID,Amount,Date) VALUES ('{}','{}','{}')""".format(k_id,k_amount,k_date))
        except IndexError:
            print("The ID you inserted does not exist in the database\n")
            print("You need to add the donor's ID into the donators table before linking a donation to it")
    connection.commit()
    connection.close()
