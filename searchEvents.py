import sqlite3 as db
from tabulate import tabulate as tb

def searchEvents():
    connection = db.connect("Charity.db")
    cursor = connection.cursor()
    