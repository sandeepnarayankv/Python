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
        raise ZeroDivisionError("Cannot Devide by Zero")
    

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
        try:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
        except (ValueError):
            print("Please Enter a Number")
        else:
            try:
                result = functions[choice - 1] (a, b)
            except ZeroDivisionError as e:
                print(e)
            except Exception as e:
                print(e)
            else:
                print(result)
