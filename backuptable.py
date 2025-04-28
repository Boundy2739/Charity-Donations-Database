import sqlite3 as db
from addDonators import *
 

def CreateTables():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS donators")
    cursor.execute("DROP TABLE IF EXISTS donatortype")
    cursor.execute("DROP TABLE IF EXISTS donations")
    cursor.execute("DROP TABLE IF EXISTS events")
    cursor.execute("DROP TABLE IF EXISTS charitycompany")
    cursor.execute("DROP TABLE IF EXISTS events_history")
    cursor.execute("PRAGMA foreign_keys=1")



    charity_tbl = """CREATE TABLE IF NOT EXISTS charitycompany(
        Name TEXT,
        Adress TEXT,
        HouseNumber INTEGER,
        Postcode TEXT,
        PhoneNumber INTEGER,
        Email TEXT
    

    )"""
    volunteers_table = """CREATE IF NOT EXISTS volunteers(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Address TEXT,
        HouseNumber INTEGER,
        Postcode TEXT,
        PhoneNumber INTEGER,
        Email TEXT,





    )"""
    donator_tbl= """CREATE TABLE IF NOT EXISTS donators(

        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Address TEXT,
        HouseNumber INTEGER,
        Postcode TEXT,
        PhoneNumber INTEGER,
        Email TEXT,
        

        

    )"""

    events_history_tbl= """CREATE TABLE IF NOT EXISTS events_history(
        EventName TEXT,
        Date TEXT,
        RoomInfo TEXT,
        Participants INTEGER,
        TicketPrice Real,
        TotalDonations Real,
        EventID INTEGER,
        FOREIGN KEY (EventID) REFERENCES events(EventID)
        ON DELETE RESTRICT
        


    )"""

    donations_tbl = """CREATE TABLE IF NOT EXISTS donations(
        DonatorID INTEGER,
        Amount REAL,
        Date TEXT,
        FOREIGN KEY ("DonatorID") REFERENCES donators("ID")
        ON DELETE RESTRICT
       
        
        
        
    )"""

    events_tbl = """CREATE TABLE IF NOT EXISTS events(
        EventID INTEGER PRIMARY KEY AUTOINCREMENT,
        EventName TEXT
        
        
        
        
    )"""

    cursor.execute(donator_tbl)
    cursor.execute(events_tbl)
    cursor.execute(donations_tbl)
    cursor.execute(charity_tbl)
    cursor.execute( events_history_tbl)

    cursor.execute("""INSERT into events("EventName") VALUES ("Egg hunt")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Bake off")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Bike ride")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Marathon")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Bingo")""")
    cursor.execute("""INSERT into events("EventName") VALUES ("Auction")""")

    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (1400909,"Abdoulaye Boundy","Leighton Street",7,"M40 9JU",0123456789,"boundye12dsad@gmail.com",2)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (131930,"Hamed Boundy","Leighton Street",7,"M40 9JU",310983102189,"cxscasa@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (2247893,"John Doe","Bankhall Ave",17,"23r 46d",6769854,"aaaaaa@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (3218941,"Frank Calderwood","Wood Glade street",72,"V46 UI3",9965432,"haacscxrty@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (13981,"Kyra Conkel","Ash Street",90,"M40 9JU",23464909,"bfgyty42@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (2901,"Alysha Laguardia","Deercliff Circle",23,"4M9 MJU",31021242,"hcsacscs@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (2488,"Otto Bednar","Broick Road",21,"M40 9JU",14124324,"bovccx42@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (2605,"Wesley Gangwer","Walport Road",11,"DMI 903",3142312189,"hcsacscs@gmail.com",1)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (913,"Ada Dittenberner","Fiat Road",82,"890 9JU",0453352,"bdqsd2@gmail.com",2)""")
    cursor.execute ("""insert into donators(ID,Name,Address,HouseNumber,Postcode,PhoneNumber,Email,DonatorType) VALUES (474920,"Zack Pentecost","Diesel Way",2,"M40 45T",32352532,"haadsdacy@gmail.com",2)""")
    
    
   

    eventName = ["Egg hunt","Marathon","Bake off","Bike ride","Bingo","Auction","Bike ride","Bake off","Bake off","Bingo","Egg hunt"]
    eventDate = ["1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025","1/1/2025"]
    eventRoom=["?","?","?","?","?","?","?","?","?","?","?"]
    eventParticipants=[25,42,14,26,18,20,23,10,12,20,30]
    eventCost = [5.99,9.99,12.99,4.99,2.99,7.99,4.99,12.99,12.99,2.99,5.99]
    eventID = [1,4,2,3,5,6,3,2,2,5,1]

    eventDetails = []
    
    for i in range (11):
        vals = [eventName[i],eventDate[i],eventRoom[i],eventParticipants[i],eventCost[i],eventID[i]]
        eventDetails.append(vals)

    
    
    sql = """insert into events_history(EventName,Date,RoomInfo,Participants,TicketPrice,EventID) VALUES(?, ?, ?, ?, ?,?)"""

    cursor.executemany(sql,eventDetails)
   
   
   
    DonationsDetails = []
    DonorID=[1400909,913,2488,2605,2901,13981,1400909,474920,2247893,3218941,913,2901,2605,1400909]
    Amount = [15.45,100.00,12.32,63.00,9.50,17.99,149.75,181.86,53.82,30.00,20.00,5.90,15.00,129.90]
    Date = ["27/03/2025","27/03/2025","27/03/2025","27/03/2025","27/03/2025","27/03/2025"
            ,"27/03/2025","27/03/2025","27/03/2025","27/03/2025"
            ,"27/03/2025","27/03/2025","27/03/2025","27/03/2025"]

    for i in range (14):
        
        vals =[DonorID[i],Amount[i],Date[i]]
        DonationsDetails.append(vals)
    
    sql = """insert into donations (DonatorID,Amount,Date) VALUES(?,?,?)"""
    cursor.executemany(sql,DonationsDetails)
    
    #cursor.execute("""insert into donations (DonatorID,Amount,Date) VALUES(1400909,1000,)""")
   # cursor.execute("""insert into donations (DonatorID,Amount,Date) VALUES(131930,725,"18/03/2025")""")
    #cursor.execute("""insert into donations (DonatorID,Amount,Date) VALUES(13981,1250,"31/01/2025")""")
    #cursor.execute("""insert into donations (DonatorID,Amount,Date) VALUES(913,645,"12/12/2024")""")
    #cursor.execute("""insert into donations (SourceEvent,Amount,Date) VALUES("Egg hunt",149.75,"12/12/2024")""")
    #cursor.execute("""insert into donations (SourceEvent,Amount,Date) VALUES("Bake off",181.86,"12/12/2024")""")
        

    connection.commit()

    connection.close()