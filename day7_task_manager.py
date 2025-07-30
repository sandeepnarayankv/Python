import os

FILE_NAME: str = "tasks.txt"

def load_tasks(file_name: str) -> dict:
    tasks: dict = dict()
    try:
        with open(file=file_name, mode="r") as f:
            task_details = f.readlines()
            for task_detail in task_details: 
                task_id, task, task_status = task_detail.strip().split(sep='|')

                tasks[int(task_id)] = {"id": task_id,
                                       "task": task,
                                       "status": task_status}

        return tasks
    except FileNotFoundError:
        print("Task list does not exist")
        return {}


def save_tasks(file_name: str, tasks: dict):
    with open(file_name, 'w') as f:
        for id, task in tasks.items():
            f.write(f"{task['id']}|{task['task']}|{task['status']}\n")


def add_task(tasks:dict) -> dict:
    id = max(tasks.keys(), default=0) + 1    
    task = input("Enter Task: ")
    status = "Incomplete"

    tasks[id] = {"id": id,
                "task": task,
                "status": status}
    
    return tasks

        
def view_tasks (tasks: dict):
    if not tasks:
        print("No Tasks exists");
    else:
        for task in tasks:
            print(f"\nTask ID: {task['id']}")
            print(f"Task Title: {task['name']}")
            print(f"Task Status: {task['status']}")
            print("============================")


def mark_complete (tasks: dict) -> dict:

    id = int(input ("Enter Task ID to Mark as Complete: "))
    if id in tasks:
        tasks[id]["status"] = "Complete"
        print(f"Task {tasks[id]['name']} Completed")
    else:
        print(f"Task {id} Does not exist")

    return tasks


def delete_task (tasks: dict) -> dict:

    id = int(input ("Enter Task ID to Mark as Complete: "))
    if id in tasks:
        print(f"Task {tasks[id]['name']} Deleted")
        tasks.pop(id)
    else:
        print(f"Task {id} Does not exist")

    return tasks

def menu() -> int:
    print("\nMenu")
    print("1. Add Task")
    print("2. View Tasks ")
    print("3. Mark Task Complete")
    print("4. Delete Contact")
    print("5. Exit")

    choice:int = int(input("\nEnter Your Choice: "))

    return choice


def task_manager():
    global FILE_NAME
    tasks = load_tasks(file_name=FILE_NAME)

    print("==================================================")
    print("========= Welcome to Task Manager ==========")
    print("==================================================")

    while True:
        choice:int = menu()

        if choice == 5:
            save_tasks(file_name=FILE_NAME, tasks=tasks)
            break
        elif choice == 1:
            tasks = add_task(tasks=tasks)
        elif choice == 2:
            tasks = view_tasks(tasks)
        elif choice == 3:
            tasks = mark_complete(tasks)
        elif choice == 4:
            tasks = delete_task(tasks)
        else:
            print(f"Your Choice {choice} is not a valid one, Please enter a valid choice")


if __name__ =="__main__":
    task_manager()
