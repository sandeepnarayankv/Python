def add (a:int, b:int)-> int:
    return a + b


def minus (a:int, b:int)-> int:
    return a - b


def multiply (a:int, b:int)-> int:
    return a * b


def divide (a:int, b:int)-> float:
    if b!=0:
        return a / b
    else:
        print("Division by 0 not allowed")
        return 0.0
    

def exponent (a:int, b:int)-> int:
    return a ** b

functions = [add, minus, multiply, divide, exponent]


while True:
    print("\nMenu:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exponent")
    print("6: Exit")
    
    choice = int(input("\nEnter your choice: "))

    if choice == 6:
        break
    else:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))

        result = functions[choice - 1] (a, b)
        print(result)
