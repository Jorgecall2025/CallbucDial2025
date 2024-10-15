import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",    
    database="CallbucDial"
)


print (db)
