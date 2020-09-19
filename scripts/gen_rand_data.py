# Purpose: Generate random data to insert into SQL database

import random 

def main():
  # print(gen_rand_house())
  gen_sql_file_realestate("fill_data.sql", 200)

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
    print(house)
    sql_cmd = f"INSERT INTO houses (price, address, city, state)\n"
    sql_cmd += f'VALUES ({house["price"]}, "{house["address"]}", "{house["city"]}", "{house["state"]}");'
    f_out.write(sql_cmd + "\n")


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