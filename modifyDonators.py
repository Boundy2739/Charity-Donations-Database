import sqlite3 as db

def editDonators():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    k_id= int(input("Insert the ID of the donator whose details you want to edit: "))

    
    print("Insert 1 if you want to edit the name of the donator\n")
    print("Insert 2 if you want to edit the address of the donator\n")
    print("Insert 3 if you want to edit the house number of the donator\n")
    print("Insert 4 if you want to edit the phone number of the donator\n")
    print("Insert 5 if you want to edit the email of the donator\n")

    UserChoice = int(input("Choose one of details you want to edit: "))

    if UserChoice == 1:
     k_name = str(input("put your name: "))
     cursor.execute( """UPDATE donators
                   SET Name ='{}'
                   WHERE ID = '{}'
                   """.format(k_name,k_id))
    
    if UserChoice == 2:
        k_address = str(input("Insert the new address: "))
        cursor.execute( """UPDATE donators
                   SET Address ='{}'
                   WHERE ID = '{}'
                   """.format(k_address,k_id))
    
    if UserChoice == 3:
     k_housenumber = str(input("Insert the new house number: "))
     cursor.execute( """UPDATE donators
                   SET HouseNumber ='{}'
                   WHERE ID = '{}'
                   """.format(k_housenumber,k_id))
    
    if UserChoice == 4:
     k_phone = str(input("Insert the new phone number: "))
     cursor.execute( """UPDATE donators
                   SET PhoneNumber ='{}'
                   WHERE ID = '{}'
                   """.format(k_phone,k_id))
    if UserChoice == 5:
     k_email = str((input("Insert the new email: ")))
     cursor.execute( """UPDATE donators
                   SET Email ='{}'
                   WHERE ID = '{}'
                   """.format(k_email,k_id))

    #k_address = str(input("put your adress: "))
    #k_housenumber = str(input("put your housenum: "))
    #k_postcode = str(input("put your postcode: "))
    #k_phone = str(input("put your phone: "))
    #k_email = str((input("put email: ")))
    
    connection.commit()
    connection.close()
