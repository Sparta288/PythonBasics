name = input("Hello please enter your name: ")
age = int(input("Please enter your age: "))

if (age >= 18) and (age <= 30):
    print(f"Welcome " + name + ", to the Holiday, you are {0} years old.".format(age))
else:
    print("Sorry " + name + " you are not old enough to enter the Holiday.")