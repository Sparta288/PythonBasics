age = 24

# this is the format function similar to the one used in java for concatenation of two data types
print("My age is {0} years.".format(age))

# this is the way to concatenate two a sting and int data type
print("My age is " + str(age) + " years.")
# this method does not have to be used to combine different replacement fields in a string
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))


