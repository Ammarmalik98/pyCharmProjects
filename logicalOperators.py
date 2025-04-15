"""
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
"""
"""
temp = -1
is_sunny =True

if temp >= 28 and is_suny:
    print("It is HOT outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is sunny")
elif temp >= 28 and not is_suny:
    print("It is HOT outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is Cloudy")
"""


num = 8
a = 9
b = 5
age = 19
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# status = "Adult" if age > 18 else "Child"
access_level = "Full Access" if user_role == "admin" else "No Access"


print(access_level)

