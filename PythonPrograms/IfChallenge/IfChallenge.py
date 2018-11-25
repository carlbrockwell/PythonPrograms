input_name = input("Please enter your name")
input_age = int(input("Please enter your age"))

if 18 <= input_age < 31:
    print("welcome to the holiday")
else:
    print("Sod off no entry")
    print(str(input_age))