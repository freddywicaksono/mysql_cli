import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="demo"
)

# Create a cursor to interact with the database
cursor = db.cursor()