# 40P
# Calculate the diagonal of a rectangle with sides lenght recievd from input

# Formula: diag^2 = l^2 + L^2, adica diag = sqrt(l^2 + L^2)

import math

length = int(input("Give length: "))
width = int(input("Give width: "))

if length and width > 0:
    diagonal = math.sqrt(length ** 2 + width ** 2)
    print('The length of the diagonal is', diagonal)
else:
    print("The length can not be 0 or a negative number")

