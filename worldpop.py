import json
from country_codes import get_country_code

# load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # convert periods in strings to decimals, drop fractions
        code = get_country_code(country_name)
        population = int(float(pop_dict['Value']))
        if code:
            print(code + ": "+ str(population))
        else:
            print('ERROR - ' + country_name)