# Nousheen Siddiqui
# Edited on 02/19/2021
# Question 4: Calculated an approximation for pi using internet search.
# A program is written to compute the approximation
# and then print that value as well as the value of math.pi from the math module.


import math
k = 1
s = 0
for i in range(1000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
    k +=2
print(s)
print (math.pi)
