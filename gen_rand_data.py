# Purpose: Generate random data to insert into SQL database

import random 

def main():
  print(gen_rand_house())

def gen_sql_file(filename):
  f_out = open(filename, "w")

def gen_rand_house():
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

  city_data = cities[int(random.random()*len(cities)-1)] 
  house = {
    'price': 25000 + int(random.random()*5000000),
    'address': str(int(random.random()*99999)) + " " + streets[int(random.random()*len(streets)-1)],
    'city': city_data.split("|")[0],
    'state': city_data.split("|")[2]
  }
  
  return house


if __name__ == "__main__":
  main()