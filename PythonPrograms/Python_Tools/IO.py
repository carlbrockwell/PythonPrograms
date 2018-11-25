
# honest_serving_men = open("D:\\Users\\carlb\\IdeaProjects\\PythonPrograms\\"
#                           "Python_Tools\\I Keep Six Honest Serving Men.txt", 'r')
#
# for line in honest_serving_men:  # For each line read in from file.
#     print(line, end='')  # Print out line removing and '' characters e.g. '\n' hidden chars.

# for line in honest_serving_men:
#     if "send" in line.lower():  # if 'send' is found in a line once converted to lower case
#         print(line, end='')  # Print line removing hidden chars.

# honest_serving_men.close()

# More efficient way of coding file input, and read whole file in.
# with open("D:\\Users\\carlb\\IdeaProjects\\PythonPrograms\\"
#           "Python_Tools\\I Keep Six Honest Serving Men.txt", 'r') as honest_serving_men:
#     for line in honest_serving_men:
#         if "send" in line.lower():
#             print(line, end='')

# Read file in line by line. read a single line for a file and returns a string
with open("D:\\Users\\carlb\\IdeaProjects\\PythonPrograms\\"
          "Python_Tools\\I Keep Six Honest Serving Men.txt", 'r') as honest_serving_men:
    line = honest_serving_men.readline()  # read line by line into the 'line' variable
    while line:  # While line exists in file, for each line
        print(line, end=' ')  # print line out
        line = honest_serving_men.readline()  # read line by line into the 'line' variable

print('\n\n')
print('=' *40)

# utilise 'readlines()' function reads entire file and feeds lines into a list.
with open("D:\\Users\\carlb\\IdeaProjects\\PythonPrograms\\"
          "Python_Tools\\I Keep Six Honest Serving Men.txt", 'r') as honest_serving_men:
        lines = honest_serving_men.readlines()  # read line by line into the lines list.
print(lines, end='/n')

print('\n\n')
print('=' *40)

# Read whole file into a variable and print in reverse to demonstrate the function steps backwards per character.
with open("D:\\Users\\carlb\\IdeaProjects\\PythonPrograms\\"
          "Python_Tools\\I Keep Six Honest Serving Men.txt", 'r') as honest_serving_men:
    lines = honest_serving_men.read()  # read whole file into variable.

for line in lines[::-1]:
    print(line, end='')

