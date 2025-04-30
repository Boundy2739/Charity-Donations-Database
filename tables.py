import sqlite3 as db

import numpy as np
 

def CreateTables():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS volunteers")
    cursor.execute("DROP TABLE IF EXISTS donators")
    cursor.execute("DROP TABLE IF EXISTS donatortype")
    cursor.execute("DROP TABLE IF EXISTS donations")
    cursor.execute("DROP TABLE IF EXISTS events")
    cursor.execute("DROP TABLE IF EXISTS charitycompany")
    cursor.execute("DROP TABLE IF EXISTS events_history")
    cursor.execute("DROP TABLE IF EXISTS volunteers_donations")
    cursor.execute("PRAGMA foreign_keys=1")



    charity_tbl = """CREATE TABLE IF NOT EXISTS charitycompany(
        Name TEXT,
        Adress TEXT,
        HouseNumber INTEGER,
        Postcode TEXT,
        PhoneNumber INTEGER,
        Email TEXT
    

    )"""
    volunteers_tbl = """CREATE TABLE IF NOT EXISTS volunteers(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Address TEXT,
        HouseNumber INTEGER,
        Postcode TEXT,
        PhoneNumber INTEGER,
        Email TEXT





    )"""
    donator_tbl= """CREATE TABLE IF NOT EXISTS donators(

        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Address TEXT,
        HouseNumber INTEGER,
        Postcode TEXT,
        PhoneNumber INTEGER,
        Email TEXT
        

        

    )"""

    events_history_tbl= """CREATE TABLE IF NOT EXISTS events_history(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EventID INTEGER,
        Date DATE,
        RoomInfo TEXT,
        Participants INTEGER,
        TicketPrice Real,
        TotalDonations Real,
        FOREIGN KEY (EventID) REFERENCES events(EventID)
        ON DELETE RESTRICT
       
        


    )"""

    donations_tbl = """CREATE TABLE IF NOT EXISTS donor_donations(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DonatorID INTEGER,
        Amount REAL,
        Date DATE,
        FOREIGN KEY ("DonatorID") REFERENCES donators("ID")
        ON DELETE RESTRICT
       
        
        
        
    )"""
    volunteer_donations_tbl = """CREATE TABLE IF NOT EXISTS volunteers_donations(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        VolunteerID INTEGER,
        Amount REAL,
        Date DATE,
        FOREIGN KEY ("VolunteerID") REFERENCES volunteers("ID")
        ON DELETE RESTRICT
       
        
        
        
    )"""

    events_tbl = """CREATE TABLE IF NOT EXISTS events(
        EventID INTEGER PRIMARY KEY AUTOINCREMENT,
        EventName TEXT
        
        
        
        
    )"""
    cursor.execute(volunteers_tbl)
    cursor.execute(donator_tbl)
    cursor.execute(events_tbl)
    cursor.execute(donations_tbl)
    cursor.execute(charity_tbl)
    cursor.execute(events_history_tbl)
    cursor.execute(volunteer_donations_tbl)

    cursor.execute("""INSERT into events("EventName") VALUES ("Egg hunt")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Bake off")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Bike ride")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Marathon")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Bingo")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Auction")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Winter Festival")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Sports tournament")""")

   
   
    volunteerDetails = []
    volunteerID = [1400909,913,474920,6729012]
    volunteerName = ["ABC DEF","Ada Dittenberner","Zack Pentecost","Mario Luna"]
    volunteerAddress = ["Light Street","Fiat Road","Diesel Way","Hexham Pines"]
    volunteerHouseNum = [77,82,2,97]
    volunteerPostcode = ["M44 9JJ", "890 9JU","M40 45T","XHM P12"]
    volunteerPhone = [123456789,453352,32352532,3289101]
    volunteerEmail = ["boundye12dsad@gmail.com","bdqsd2@gmail.com","haadsdacy@gmail.com","email@gmail.com"]
    for i in range (4):
        vals = [volunteerID[i],volunteerName[i],volunteerAddress[i],volunteerHouseNum[i],volunteerPostcode[i],volunteerPhone[i],volunteerEmail[i]]
        volunteerDetails.append(vals)
    sql = """INSERT INTO volunteers VALUES (?,?,?,?,?,?,?)"""
    cursor.executemany(sql,volunteerDetails)

    donorDetails = []
    donorID = [131930,2247893,3218941,13981,2901,2488,2605,]
    donorName = ["HB","John Doe","Frank Calderwood","Kyra Conkel","Alysha Laguardia","Otto Bednar","Wesley Gangwer"]
    donorAddress = ["Light Street","Bankhall Ave","Wood Glade street","Ash Street","Deercliff Circle","Broick Road","Walport Road"]
    donorHouseNum = [7,17,72,90,23,21,11]
    donorPostcode = ["M40 9JU","23R 46D","V46 UI3","M40 AS8","4M9 MJU","M40 9JU","DMI 903",]
    donorPhone = [310983102189,6769854,9965432,23464909,31021242,14124324,3142312189]
    donorEmail = ["cxscasa@gmail.com","aaaaaa@gmail.com","haacscxrty@gmail.com","bfgyty42@gmail.com","hcsacscs@gmail.com","bovccx42@gmail.com","etrucscs@gmail.com",]
   
    for i in range (7):
        vals = [donorID[i],donorName[i],donorAddress[i],donorHouseNum[i],donorPostcode[i],donorPhone[i],donorEmail[i]]
        donorDetails.append(vals)
    sql = """INSERT INTO donators VALUES (?,?,?,?,?,?,?)"""
    cursor.executemany(sql,donorDetails)


    eventID = [1,4,2,8,3,5,6,3,7,2,2,5,1,1]
    eventDate = ["2025-01-01","2025-01-01","2025-01-01","2025-01-01","2025-01-01","2025-01-01","2024-10-8","2024-12-19","2025-02-17","2025-01-01","2025-01-01","2025-01-01","2025-01-01"]
    eventRoom=["?","?","?","?","?","?","?","?","?","?","?","?","?"]
    eventParticipants= np.array([25,42,14,36,26,18,20,50,23,10,12,20,30])
    eventCost = np.array([5.99,9.99,12.99,4.99,2.99,4.99,7.99,4.99,4.99,12.99,12.99,2.99,5.99])
    eventTotalDonations = np.multiply(eventParticipants,eventCost)
    print(eventTotalDonations)
    

    eventDetails = []
    
    for i in range (13):
        vals = [eventID[i],eventDate[i],eventRoom[i],int(eventParticipants[i]),float(eventCost[i]),round(float(eventTotalDonations[i]), 2)]
        eventDetails.append(vals)

    
    
    sql = """insert into events_history(EventID,Date,RoomInfo,Participants,TicketPrice,TotalDonations) VALUES(?,?,?,?,?,?)"""

    cursor.executemany(sql,eventDetails)
   
   
   
    DonationsDetails = []
    DonorID=[2488,2605,2901,13981,2247893,3218941,2901,2605]
    Amount = [15.45,100.00,63.00,9.50,30.00,20.00,5.90,15.00]
    Date = ["2025-03-27","2025-03-27","2025-03-27","2025-03-27","2025-03-27","2025-03-27"
            ,"2025-03-27","2025-03-27"]

    for i in range (8):
        
        
        vals =[DonorID[i],Amount[i],Date[i]]
        DonationsDetails.append(vals)

    
    sql = """insert into donor_donations (DonatorID,Amount,Date) VALUES(?,?,?)"""
    cursor.executemany(sql,DonationsDetails)
    
    VolunteerDonationsDetails = []
    VolunteerID = [1400909,913,474920,913,913,6729012,6729012]
    Amount = [17.45,10.00,73.10,8.50,30.00,30.00,9.99,27.17]
    Date = ["2025-03-27","2025-03-27","2025-03-27","2025-03-27","2025-03-27","2025-03-27"
            ,"2025-03-27","2025-03-27"]
    
    for i in range (6):
        
        
        vals =[VolunteerID[i],Amount[i],Date[i]]
        VolunteerDonationsDetails.append(vals)
    sql = """insert into volunteers_donations (VolunteerID,Amount,Date) VALUES(?,?,?)"""
    cursor.executemany(sql,VolunteerDonationsDetails)

    connection.commit()

    connection.close()