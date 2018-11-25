# Author: Carl Brockwell
# January 2018


# Sets have no inherent ordering or duplicates and not accessed via keys, set members are hashed. Useful for
# cleaning up data.
# Create sets ans perform typical functions to demonstrate use.

empty_set = set()  # Create an empty set.

even = set(range(0, 40, 2))  # Create a set from a range list from 0-40 every 2 steps ensuring each number is even.
print(sorted(even))

squares_tuple = (4, 6, 9, 16, 25)  # Create square numbers
squares = set(squares_tuple)  # Create a set called squares from the 'squares_tuple' tuple.
print(sorted(squares))  # Print squares set in order.

print("even minus squares")
print(sorted(even.difference(squares)))  # Remove the square numbers from the the 'even' set
print(sorted(even - squares))  # Performs same functions as 'differences()'.

print("squares minus even")
print(squares.difference(even))  # Remove the even numbers form the 'square' set.
print(squares - even)  # Performs same function as 'difference()'


