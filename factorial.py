# Nousheen Siddiqui
# Edited on 02/19/2021
# Question 6:A for statement is used to calculate the factorial of a user input value.
# Print this value as well as the calculated value using the factorial function in the math module.


import math
factorial = int(input("Provide a number"))
x=1
for i in range(1, factorial+1):
    x = x*i
print(x)
print(math.factorial(factorial))
