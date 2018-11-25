# Author: Carl Brockwell
# 29th December 2017

# Create dictionary
fruit = {"Orange": "a sweet, orange citrus fruit",
         "Apple": "good for making cider",
         "Lemon": "a yellow, sour citrus fruit",
         "Grape": "a small sweet fruit growing in bunches",
         "Lime": "a sour green citrus fruit"}
valid_input = False

# Print value information by declaring associated key
# print(fruit["Lemon"])  # Print existing value associated with stated key
# fruit["pear"] = "an odd shaped apple"  # Create additional key and value into dictionary
# print(fruit["pear"])  # Print new value using new key

# Sort dictionary into an ordered list and print out
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:  # Print list and associated values from dictionary
    print(f + ": " + fruit[f])
print(ordered_keys)  # Print keys from sorted list

print('-' * 50)  # Separator
print(fruit.items())  # Print items from dictionary
print(fruit.keys())  # Print keys from dictionary
print(fruit.values())  # Print values from dictionary
print('=' * 50)  # Separator

f_tuple = tuple(fruit.items())  # pass dictionary items  {key,  value} into a tuple
print(f_tuple)  # Print tuple

for snack in f_tuple:  # iterate through each tuple item and pass into separate variables
    item, description = snack
    print(item + " is " + description)  # Output variables to demonstrate
print('=' * 50)  # Separator

# User input loop
while True:
    dict_key = input('Please enter a fruit:')
    valid_input = False
    if dict_key == "quit":  # Close program
        valid_input = True
        break

    if dict_key in fruit:
        valid_input = True
        description = fruit.get(dict_key, "fruit not recognised/found")
        print(description)

    if dict_key == "all":  # Iterate through dictionary and print all keys and associated values
        valid_input = True
        for key, value in fruit.items():
            print(key, value)

    if dict_key == "add":  # Add a dictionary entry
        valid_input = True
        key_value = input("Please state the key to add to dictionary:")
        fruit[key_value] = ""
        value_value = input("Please state the value to associate with the new key:")
        fruit[key_value] = value_value
        print("New entry has been added to dictionary with Key: " + key_value + " Value: " + value_value)

    if dict_key == "delete":  # Remove a dictionary entry
        valid_input = True
        key_value = input("Please state the key to remove from the dictionary:")
        del fruit[key_value]
        print("Entry has been removed from dictionary")

    if valid_input is False:  # Error handling should any input not match any of above conditions and
        # subsequently valid_input set to True
        print("fruit/command not recognised")
