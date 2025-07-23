from datetime import datetime

name = input("Name: ")
age = int(input("Age: "))
color = input ("Color: ")
birth_year = int(input("Birth Year: "))

calc_age = datetime.now().year - birth_year

print(f"Hi {name}, you are {age} years old")
print(f"Your favorite color is {color}")
print(f"Your nick name is {name+str(calc_age)}")