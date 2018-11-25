# Author: Carl Brockwell
# 30th December 2017

my_list = ["a", "b", "c", "d"]
new_string = ",".join(my_list)
print(new_string)

#  Joining dictionaries, create list of locations from dictionary keys and values.
locations = {0: "You're sitting in front of a computer learning python",
             1: "You're standing at the end of the road before a small brick building",
             2: "you're at the top of the hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You're in a valley beside a stream",
             5: "You're in the forest"}

# Create list of exit opportunities from dictionary keys and values. As locations is a list of dictionary keys and
# values their positions won't changes and can be used as a positional reference to state available exits.
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1}]

loc = 1  # variable to force start at location 'n'
while True:
    available_exits = ",".join(exits[loc].keys())  # Join keys from this dictionary location
    if loc == 0:
        break

    direction = input("Available exits are: " + available_exits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("cannot go in the direction")