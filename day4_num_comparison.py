num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if num1 == num2:
    print(f"Numbers {num1}, {num2} are equal")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is less than {num2}")

if num1 == 0 and num2 == 0:
    print("Both Numbers are 0")
elif num1 == 0 or num2 == 0:
    print("Atleast one of the Numbers is 0")
else:
    print("Both Numbers are non zero")