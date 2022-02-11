a = 12  # not an expression (these are bound or assigned variables)
b = 3   # not an expression (these are bound or assigned variables)


# All of the following below are expressions that include the (a + b) or whatever operator
#

print(a + b)   # 15
print(a - b)   # 9
print(a * b)   # 36
print(a / b)   # 4.0
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)   # 0 modulo: the remainder after integer division

print() # creates a space

for i in range(1, a//b): # the i is not an expression
    print(i)

for i in range(1, 4):
    print(i)




i = 1  # not an expression
print(i)
i = 2  # not an expression
print(i)
i = 3  # not an expression
print(i)

print(a + b // 3 - 4 * 12)      # -35
print(a + (b // 3) - (4 * 12))  # -35
print((((a+b) // 3) - 4) * 12)  # 12
print(((a + b) // 3 - 4) * 12)  # 12

# order of operations
# multiplication and division have equal precedence (higher precedence than addition and subtraction.
# addition and subtraction have equal precedence
# precedence is evaluated left to right











