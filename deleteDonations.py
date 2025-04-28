import sqlite3 as db
from tabulate import tabulate
def deleteDonorDonation():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=1")
    k_ID = int(input("Insert the ID of the donator whose donation you want to remove: "))
    k_Date = input("Insert the date of the donation")
    k_Amount = float(input("Insert the amount that was donated: "))
    k_role = input("Is the donator a volunteer? y/n")
    if k_role.lower() == "y":
        cursor.execute("""SELECT VolunteerID,Amount,Date from donations 
                       WHERE VolunteerID = '{}'
                       AND Date = '{}'
                       AND Amount = '{}'""".format(k_ID,k_Date,k_Amount))
        checkDetails = cursor.fetchall()
        print(checkDetails[0][0],"hdahhe",checkDetails[0][1],"udidqiqdi",checkDetails[0][2])
        try:
            headers = ["VolunteerID","Amount","Date"]
            if checkDetails[0][0] == k_ID and checkDetails[0][2] == k_Date and checkDetails[0][1] == k_Amount:
                print(tabulate(checkDetails,headers=headers))
                confirmation = input("Is this the donation you want to delete? y/n: ")
                if confirmation == 'y':
                    cursor.execute("""DELETE from donations WHERE VolunteerID ='{}' and Date = '{}'""".format(k_ID,k_Date))
        except:
            print("Cannot find a donation with the details give, check that the ID and the date are correct")
    else:
        cursor.execute("""SELECT DonatorID,Amount,Date from donations 
                       WHERE DonatorID = '{}'
                       AND Date = '{}'
                       AND Amount = '{}'""".format(k_ID,k_Date,k_Amount))
        checkDetails = cursor.fetchall()
        print(checkDetails[0][0],"hdahhe",checkDetails[0][1],"udidqiqdi",checkDetails[0][2])
        try:
            headers = ["DonatorID","Amount","Date"]
            if checkDetails[0][0] == k_ID and checkDetails[0][1] == k_Amount and checkDetails[0][2] == k_Date:
                print(tabulate(checkDetails,headers=headers))
                confirmation = input("Is this the donation you want to delete? y/n: ")
                if confirmation.lower == ("y"):
                    cursor.execute("""DELETE from donations WHERE DonatorID ='{}' and Date = '{}'""".format(k_ID,k_Date))
        except:
            print("Cannot find a donation with the details give, check that the ID and the date are correct")
   
    connection.commit()
    connection.close()