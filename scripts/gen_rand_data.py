# Purpose: Generate random data to insert into SQL database

import random 

def main():
  # print(gen_rand_house())
  f_out = "../db-container/db_init_scripts/fill_data.sql"
  gen_sql_file_realestate(f_out, 200)
  gen_user_pass(f_out, 200)
  create_sql_users(f_out)

# Write SQL file and fill with real estate info
def gen_sql_file_realestate(filename, num_houses, overwrite=True):
  if overwrite:
    f_out = open(filename, "w")
  else:
    f_out = open(filename, "a")

  # Preamble
  preamble = """CREATE DATABASE realestate;

USE realestate;

CREATE TABLE houses (id INT AUTO_INCREMENT PRIMARY KEY, price INT, address VARCHAR(255), city VARCHAR(255), state VARCHAR(255));

"""
  f_out.write(preamble)

  houses = gen_rand_houses(num_houses)

  for house in houses:
    # print(house)
    sql_cmd = f"INSERT INTO houses (price, address, city, state)\n"
    sql_cmd += f'VALUES ({house["price"]}, "{house["address"]}", "{house["city"]}", "{house["state"]}");'
    f_out.write(sql_cmd + "\n")

# Create a table and add user/pass info to it
# Assume that gen_sql_file_realestate() gets run first, so all we have to do is add to the existing sql file
def gen_user_pass(filename, num_users):

  # Preamble
  preamble = """CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), email VARCHAR(255));
  
"""
  f_out = open(filename, "a")

  f_user = open("usernames.txt", "r")
  usernames = []
  for user in f_user:
    if user.startswith("#"):
      continue
    usernames.append(user.strip())

  f_pass = open("passwords.txt", "r")
  passwords = []
  for c_pass in f_pass:
    if c_pass.startswith("#"):
      continue
    passwords.append(c_pass.strip())

  f_email = open("emails.txt", "r")
  emails = []
  for email in f_email:
    if email.startswith("#"):
      continue
    emails.append(email.strip())

  sql_cmd = preamble
  for x in range(num_users):
    user_data = {
        "user": usernames[int(random.random()*(len(usernames)-1))],
        "password": passwords[int(random.random()*(len(passwords)-1))],
        "email": emails[int(random.random()*(len(emails)-1))]
    }
    sql_cmd += "INSERT INTO users (username, password, email)\n"
    sql_cmd += f'VALUES ("{user_data["user"]}", "{user_data["password"]}", "{user_data["email"]}");\n'

  f_out.write(sql_cmd + "\n")

# Assume filename is already created and we're just appending to it
# Creates an app db user for houses, an app db user for users, and an app db master user (for both tables)
def create_sql_users(filename):
  sql_cmd = """
CREATE USER svc_houses@localhost IDENTIFIED BY 'hunter2';
grant all privileges on houses.* to svc_houses@localhost;
CREATE USER svc_users@localhost IDENTIFIED BY 'sup3rs3cr3tp@$$';
grant all privileges on users.* to svc_users@localhost;
CREATE USER svc_master@localhost IDENTIFIED BY 'foobar';
grant all privileges on *.* to svc_master*localhost;

"""
  # Third user has weak password and no hostname control

  f_out = open(filename, "a")
  f_out.write(sql_cmd)


def gen_rand_houses(num_houses):
  # Import city/states:
  cities_f = open("us_cities_states_counties.csv", "r")

  # format: City|State short|State full|County|City alias
  cities = []
  for line in cities_f:
    if line.startswith("#"):
      continue
    cities.append(line)

  # print(cities)

  # Import street names:
  streets_f = open("Street_Names.csv", "r")

  # format: FullStreetName,StreetName,StreetType,PostDirection
  streets = []
  for line in streets_f:
    if line.startswith("#"):
      continue
    streets.append(line.split(",")[0])

  # print("Streets: ")
  # print(streets)

  houses = []
  for x in range(num_houses):
    city_data = cities[int(random.random()*len(cities)-1)] 
    house = {
      'price': 25000 + int(random.random()*5000000),
      'address': str(int(random.random()*99999)) + " " + streets[int(random.random()*len(streets)-1)],
      'city': city_data.split("|")[0],
      'state': city_data.split("|")[2]
    }
    houses.append(house)
  
  return houses


if __name__ == "__main__":
  main()