# map state names to their postal abbreviations
states = {
'Oregon' : 'OR',
'Florida' : 'FL',
'Texas' : 'TX',
'Colorado' : 'CO',
'California' : 'CA',
'New York' : 'NY',
'Rhode Island' : 'RI',
'Michigan' : 'MI',
'Illinois' : 'IL'
}

# create a set of states and some cities in them
cities = {
'TX' : 'Dallas',
'CO' : 'Colorado Springs',
'IL' : 'Chicago',
'FL' : 'Miami',
'NY' : 'Albany',
'RI' : 'Providence',
'MI' : 'Detroit',
'CA' : 'Los Angeles',
'OR' : 'Portland'
}

# print some cities
print (' - ' * 10)
print("NY has: ", cities['NY'])
print("IL has: ", cities['IL'])
print("TX has: ", cities['TX'])
print("CO has: ", cities['CO'])
print("CA has: ", cities['CA'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Texas' abbreviation is: ", states['Texas'])

# print using the state then cities dict
print('-' * 10)
print("Illinois has: ", cities[states['Illinois']])
print("Colorado has: ", cities[states['Colorado']])

# print all known state abbreviations
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has the abbreviation {abbrev}.")

# print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

# do both at once, why not
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
# what if we don't intersect?

state = states.get('Wyoming')

if not state:
    print("Wyoming is actually Latin for 'no state here'.")

city = cities.get('WY', 'Does Not Exist')
print(f"The city for the state 'WY' is {city}.")
