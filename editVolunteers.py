import sqlite3 as db

def editVolunteers():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_id = int(input("Insert the ID of volunteer whose details you want to edit: "))
    cursor.execute("SELECT ID from volunteers WHERE ID = '{}'".format(k_id))
    IDcheck = cursor.fetchall()
    try:
        if k_id != IDcheck[0][0]:
            print("There is no volunteer with such ID")
    
        else:
            print("Insert 1 if you want to edit the name of the volunteer\n")
            print("Insert 2 if you want to edit the address of the volunteer\n")
            print("Insert 3 if you want to edit the house number of the volunteer\n")
            print("Insert 4 if you want to edit the phone number of the volunteer\n")
            print("Insert 5 if you want to edit the email of the volunteer\n")
            print("Insert 6 if you want to edit the postcode of the volunteer\n")
            print("Insert 0 if you want to go back")

            UserChoice = int(input("Choose an option: "))
            if UserChoice == 1:
                k_name = str(input("put your name: "))
                cursor.execute("""UPDATE volunteers
                            SET Name ='{}'
                            WHERE ID = '{}'
                            """.format(k_name,k_id))
        
            if UserChoice == 2:
                k_address = str(input("Insert the new address: "))
                cursor.execute( """UPDATE volunteers
                        SET Address ='{}'
                        WHERE ID = '{}'
                        """.format(k_address,k_id))
            
            if UserChoice == 3:
                k_housenumber = str(input("Insert the new house number: "))
                cursor.execute( """UPDATE volunteers
                            SET HouseNumber ='{}'
                            WHERE ID = '{}'
                            """.format(k_housenumber,k_id))
            
            if UserChoice == 4:
                k_phone = str(input("Insert the new phone number: "))
                cursor.execute( """UPDATE volunteers
                            SET PhoneNumber ='{}'
                            WHERE ID = '{}'
                            """.format(k_phone,k_id))
            if UserChoice == 5:
                k_email = str((input("Insert the new email: ")))
                cursor.execute( """UPDATE volunteers
                            SET Email ='{}'
                            WHERE ID = '{}'
                            """.format(k_email,k_id))
            if UserChoice == 6:
                k_postcode = (input("Insert the new postcode: "))
                cursor.execute( """UPDATE volunteers
                            SET Postcode ='{}'
                            WHERE ID = '{}'
                            """.format(k_postcode,k_id))
                if UserChoice == 0:
                    connection.close()
                    return
    except IndexError:
        print("This ID does not exists in the database, make sure to spell correctly")   
    connection.commit()
    connection.close()       