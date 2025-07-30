def factorial(a:int) -> int:
    if a <= 1:
        return 1
    else:
        return a*factorial(a-1)
    
if __name__ == "__main__":
    a = int(input("Number: "))
    factorial_of_num = factorial(a=a)
    print(f"The Factorial of {a} is {factorial_of_num}")