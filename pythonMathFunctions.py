from fileinput import hook_encoded

x = 3.142
y = -7
z = 4

# result = round(x, 2)
# result = abs(y)
# result = pow(y, 3)
# result = max(x,y,z)


# print(result)

import math

"""
#print(math.pi)
result = math.sqrt(13000)


print(result)


#Calculating possible time dilation for each heaven

first = 7
second = first * 77
third = second * 77
fourth = third * 77
fifth = fourth * 77
sixth = fifth * 77
seventh = sixth * 77

print(first, second/365, third/365, fourth/365, fifth/365, sixth/365, seventh/365)
"""

# result = math.ceil(x)
# result = math.floor(x)


# print(result)

#pi = math.pi
#r = float(input("Enter a value for the radius: "))

#circumference = 2*pi*r

#print(f"The circumference is {round(circumference, 2)}cm square")

# r = float(input("Input a value for the Radius: "))

# area = math.pi * pow(r, 2)
# print(f"The area of the circle is {round(area, 2)}cm^2")


a = float(input("Input the value for side A: "))
b = float(input("Input the value for side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(round(c, 2))