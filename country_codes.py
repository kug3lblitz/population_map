from pygal.maps.world import COUNTRIES as cnt

# for country_code in sorted(cnt.keys()):
    # print(country_code, cnt[country_code])

def get_country_code(country_name):
    """return pygal 2 digit country code from peripheral lib"""

    for code, name in cnt.items():
        if name == country_name:
            return code

    # if code not found
    return None

# print(get_country_code('Norway'))
# print(get_country_code('Australia'))
# print(get_country_code('United States'))
