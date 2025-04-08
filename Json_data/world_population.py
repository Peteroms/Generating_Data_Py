import json

# Load the data into a list.
filename = 'population.json'
with open(filename) as fn:
    popu_data = json.load(fn) # The json.load() function converts the data into a format Python can work with, in this case a list.

# Print the 2020 population for each country.
for popu_dict in popu_data:
    if popu_dict[int('population_by_year')] == int(2020):
        country_name = popu_dict['name']
        print(country_name)


