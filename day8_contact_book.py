contact_book: dict = dict()


def add_contact():
    global contact_book
    if len(contact_book.keys()) > 0: 
        id = max(contact_book.keys()) + 1
    else:
        id = 1

    name: str = input("Name: ")
    phone: str = input("Phone: ")
    email: str = input("email: ")

    contact_book[id] = {"name": name,
                        "phone": phone,
                        "email": email}


def print_contacts():
    global contact_book
    if len(contact_book.keys()) > 0: 
        for id, value in contact_book.items():
            print(f"\nID: {id}")
            print(f"Name: {value['name']}")
            print(f"Phone: {value['phone']}")
            print(f"Email: {value['email']}")
            print("============================")
    else:
        print("No Contacts in Contact Book")


def print_contact_by_name():
    global contact_book
    name = input("Name to Search: ").lower()
    if len(contact_book.keys()) > 0: 
        for id, value in contact_book.items():
            if value['name'].lower() == name:
                print(f"\nID: {id}")
                print(f"Name: {value['name']}")
                print(f"Phone: {value['phone']}")
                print(f"Email: {value['email']}")
                print("============================")
    else:
        print("No Contacts in Contact Book")


def edit_contact_details():
    global cart
    print_contacts()

    id = int(input("Enter the ID to be Edited: "))

    name: str = input("Name: ")
    phone: str = input("Phone: ")
    email: str = input("email: ")

    contact_book[id] = {"name": name,
                        "phone": phone,
                        "email": email}
    
def del_contact ():
    global cart
    print_contacts()

    id = int(input("Enter the ID to be Deleted: "))

    del contact_book[id]


def menu() -> int:
    print("\nMenu")
    print("1. Add Contact")
    print("2. Edit Contact ")
    print("3. Print Contact List")
    print("4. View Contact By Name")
    print("5. Delete Contact")
    print("6. Exit")

    choice:int = int(input("\nEnter Your Choice: "))

    return choice


def contact_list():
    print("==================================================")
    print("========= Welcome to Contact List ==========")
    print("==================================================")

    while True:
        choice:int = menu()

        if choice == 6:
            break
        elif choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact_details()
        elif choice == 3:
            print_contacts()
        elif choice == 4:
            print_contact_by_name()
        elif choice == 5:
            del_contact()
        else:
            print(f"Your Choice {choice} is not a valid one, Please enter a valid choice")


if __name__ =="__main__":
    contact_list()
