import json
from country_codes import get_country_code
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

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

# group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# see how many countries are in each tier
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Word Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('worldpopulation.svg')
