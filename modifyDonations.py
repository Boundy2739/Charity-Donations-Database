import sqlite3 as db

def editDonations():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    print("Insert 1 if you want to edit a donation coming from a donator\n")
    print("Insert 2 if you want to edit a donation coming from an event\n")
    UserChoice = int(input("Choose an option: "))
    if UserChoice == 2:
        k_eventName = str(input("Insert the name of the source event: "))
        k_date = str(input("Insert the date that donation happened:  "))
        cursor.execute("""select SourceEvent from donations where SourceEvent='{}'""".format(k_eventName))
        namecheck = cursor.fetchall()
        print("diqkmdqimd", namecheck)
        if not namecheck:
            print("There is no such donation in the database")
        if namecheck:
            cursor.execute("""select Date from donations where Date ='{}'""".format(k_date))
            datecheck = cursor.fetchall()
            if datecheck:
                k_amount = float(input("Insert the new amount of money"))
                cursor.execute("""UPDATE donations
                    SET Amount = '{}' 
                    WHERE SourceEvent ='{}'
                    AND Date = '{}'""".format(k_amount,k_eventName,k_date))
            if not datecheck:
                print("There is no donations in database with the details you have given!")
    if UserChoice == 1:
        k_id = int(input("Insert the id of the donator: "))
        k_date = str(input("Insert the date when the donation happened:  "))
        cursor.execute("""select DonatorID from donations where DonatorID='{}'""".format(k_id))
        idcheck = cursor.fetchall()
        print("diqkmdqimd", idcheck)
        if not idcheck:
            print("There is no such donation in the database")
        if idcheck:
            cursor.execute("""select Date from donations where Date ='{}'""".format(k_date))
            datecheck = cursor.fetchall()
            if datecheck:
                k_amount = float(input("Insert the new amount of money"))
                cursor.execute("""UPDATE donations
                    SET Amount = '{}' 
                    WHERE DonatorID ='{}'
                    AND Date = '{}'""".format(k_amount,k_id,k_date))
            if not datecheck:
                print("There is no donations in database with the details you have given!")
                
    connection.commit()
    connection.close()