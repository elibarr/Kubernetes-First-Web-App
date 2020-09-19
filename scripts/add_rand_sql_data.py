# Purpose: Add random data to SQL database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
#   print(type(x))
# print("realestate" in mycursor)

# Create "Real Estate" database:
# mycursor.execute("CREATE DATABASE realestate")

# Create some fields...
redb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="realestate"
) 
mycursor = redb.cursor()
mycursor.execute("CREATE TABLE houses (id INT AUTO_INCREMENT PRIMARY KEY, price INT, address VARCHAR(255), city VARCHAR(255), state VARCHAR(255))")