# Nousheen Siddiqui
# Edited 02/19/2021
# Question 5: program to compute the conversion given a user input value.
# Printed this value as well as the calculated value using the degrees function in the math module.



import math
radians = int(input("Provide a number"))
degrees = (radians*180/math.pi)
print (degrees)
print(math.degrees(radians))