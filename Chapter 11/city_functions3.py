# 11-2

def get_formatted_city3(city, country, population=''):
    if population:
        full_string = city.title() + ', ' + country.title() + ' - population ' + population.split('=')[1]
    else:
        full_string = city.title() + ', ' + country.title()
    return full_string
