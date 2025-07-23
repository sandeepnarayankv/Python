cart: list = list()

def menu() -> int:
    print("\nMenu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Print Cart")
    print("4. Clear Cart")
    print("5. Edit Item")
    print("6. Exit")

    choice:int = int(input("\nEnter Your Choice: "))

    return choice


def add_item():
    global cart

    item: str = input("Enter the Item: ").lower()

    cart.append(item)

def print_cart():
    global cart

    for i, item in enumerate(cart):
        print(f"{i+1}. {item}")

def remove_item():
    global cart

    print_cart()

    item: str = input("Enter the Item to Remove: ").lower()

    cart.remove(item)


def edit_item():
    global cart

    print_cart()

    item_2_remove: str = input("Enter the Item to Remove: ").lower()

    idx = cart.index(item_2_remove)

    cart.remove(item_2_remove)

    item_2_add: str = input("Enter the Item: ").lower()

    cart.insert(idx, item_2_add)




def clear_cart():
    global cart

    cart.clear()        

def shopping_list():
    print("==================================================")
    print("========= Welcome to Shopper's PaRADICE ==========")
    print("==================================================")

    while True:
        choice:int = menu()

        if choice == 6:
            break
        elif choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            print_cart()
        elif choice == 4:
            clear_cart()
        elif choice == 5:
            edit_item()
        else:
            print(f"Your Choice {choice} is not a valid one, Please enter a valid choice")


if __name__ =="__main__":
    shopping_list()




