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
  # database="realestate"
) 

# Open script and execute commands
f = open("fill_data.sql", "r")
sql_exec_str = f.read()
print(sql_exec_str) 

mycursor = redb.cursor()
for command in sql_exec_str.split(";"):
  print("Command: " + command)
  # if command:
  #   mycursor.execute(command)