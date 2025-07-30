import os

FILE_NAME: str = "notes.txt"

def load_notes(file_name: str) -> dict:
    notes: dict = dict()
    try:
        with open(file=file_name, mode="r") as f:
            note_details = f.readlines()
            for note_detail in note_details: 
                note_id, note = note_detail.strip().split(sep='|')

                notes[int(note_id)] = note

        return notes
    except FileNotFoundError:
        print("note list does not exist")
        return {}


def save_notes(file_name: str, notes: dict):
    with open(file_name, 'w') as f:
        for id, note in notes.items():
            f.write(f"{id}|{note}\n")


def add_note(notes:dict) -> dict:
    id = max(notes.keys(), default=0) + 1    
    note = input("Enter note: ")

    notes[id] = note
    
    return notes

        
def view_notes (notes: dict):
    if not notes:
        print("No notes exists");
    else:
        for id, note in notes.items():
            print(f"\nnote ID: {id}")
            print(f"note: {note}")
            print("============================")

def delete_note (notes: dict) -> dict:

    id = int(input ("Enter note ID to Mark as Complete: "))
    print(notes.keys())
    print(id in notes.keys())
    if id in notes.keys():
        print(f"note {id} - {notes[id]} Deleted")
        notes.pop(id)
    else:
        print(f"note {id} Does not exist")

    return notes

def menu() -> int:
    print("\nMenu")
    print("1. Add note")
    print("2. View notes ")
    print("3. Delete Note")
    print("4. Exit")

    choice:int = int(input("\nEnter Your Choice: "))

    return choice


def note_manager():
    global FILE_NAME
    notes:dict = load_notes(file_name=FILE_NAME)
    print(notes)

    print("==================================================")
    print("========= Welcome to note Manager ==========")
    print("==================================================")

    while True:
        choice:int = menu()

        if choice == 4:
            save_notes(file_name=FILE_NAME, notes=notes)
            break
        elif choice == 1:
            notes = add_note(notes=notes)
        elif choice == 2:
            view_notes(notes)
        elif choice == 3:
            notes = delete_note(notes)
        else:
            print(f"Your Choice {choice} is not a valid one, Please enter a valid choice")


if __name__ =="__main__":
    note_manager()