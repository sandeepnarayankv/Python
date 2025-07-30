check_num = int(input("Enter Number: "))

div = check_num//2 + 1
is_prime = True
if check_num == 2:
    is_prime = True
else:
    for i in range(2, div):
        if check_num%i == 0:
            is_prime = False            
            break;

if check_num <= 1:
    print(f"Number {check_num} is neither prime or non-prime")
elif is_prime:
    print(f"Number {check_num} is prime")
else:
    print(f"Number {check_num} is non-prime")