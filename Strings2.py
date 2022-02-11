parrot = "Norwegian Blue"

print(parrot)
# this example uses indexing to print out certain letters
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# indexing backwards
print()
print(parrot[-1])
print(parrot[-14])

print()
# negative index values the last value is -1 and goes a many as letter you can count back to the left in this case -14
print(parrot[-6])
print(parrot[-8])
print(parrot[-11])
print(parrot[-5])
print(parrot[-10])
print(parrot[-11])

# slicing

parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg
# the last character in the index slice is not included in the output
# so only 0 thru 5 are printed out
# up to but not including index 6

print(parrot[3:5]) # we

print(parrot[0:9]) # Norwegian
print(parrot[:9])  # Norwegian

# return the word blue using index slicing

print(parrot[10:14]) # Blue
print(parrot[10:])  # Blue

# square brackets [] are using for indexing, slicing

print(parrot[:6]) # starts at beginning of string
print(parrot[6:]) # runs till the end of the string


# prints out Norwegian Blue
print(parrot[:6] + parrot[6:])

print(parrot[:]) # prints out all of Norwegian Blue

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"
print(number[1::4])

print("Hello")

greeting = "Hello"
name = input("Please enter you name ")
age = 30

age_in_words = "2 years"
print(name + f"is {age} years old")

print("hello")















