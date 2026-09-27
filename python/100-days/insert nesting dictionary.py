travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country, visit_num, cities):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = visit_num
    new_country['cities'] = cities
    # travel_log.append(new_country)
    travel_log += [new_country]
# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log[2])
