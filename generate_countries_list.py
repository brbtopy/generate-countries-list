#!/usr/bin/env python
import pycountry

def generate_country_list():
    countries = pycountry.countries
    country_length = len(countries)

    a = 0
    country_list = [0 for _ in range(country_length)]

    for country in countries:
        country_list[a] = country.name
        a = a + 1

    with open("countries_list.txt", "w+") as file:
        for items in country_list:
            file.write(items + "\n")
    file.close()

generate_country_list()