# cities = ["London", "Birmingham", "Gloucester", "Bristol"]
#
# # Open and write list into a file
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)


# Read file back in strip new lines, special chars.

cities = []

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)



