import json
from country_codes import get_country_code
import pygal

# load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # convert periods in strings to decimals, drop fractions
        code = get_country_code(country_name)
        population = int(float(pop_dict['Value']))
        if code:
            cc_populations[code] = population

wm = pygal.maps.world.World()
wm.title = 'Word Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('worldpopulation.svg')
