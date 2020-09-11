the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this for-loop iterates over a list
for number in the_count:
    print(f"This is count {number}.")

# as does this
for fruit in fruits:
    print (f"A fruit of type: {fruit}.")

# we can iterate over mixed lists too, but we'll need some curly boys to avoid
# type mismatching

for i in change:
    print(f"I got {i}.")

# we can build lists too! first, initalize the list by making an empty one
elements = []

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}.")
