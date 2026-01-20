to_do = []

def option():
    print("\n1. add task \n2. view task \n3. mark complete \n4. delete task \n5. exit")

def add_task():
    add_user = input("ENTER A TASK TO ADD: \t")
    to_do.append({"task" : add_user, "is_completed" : False})

def view_task():
    for t,o in enumerate(to_do,1):
        print(f"{t}. {o["task"]} ")

def mark_complete():
    view_task()
    task_number = int(input("ENTER YOUR TASK TO MARK: \t"))
    to_do[task_number - 1]["is_completed"] = True

def delete_task():
    view_task()
    task_number = int(input("ENTER YOUR TASK TO DELETE TASK"))
    to_do.pop(task_number - 1)

while True:
    option()
    user_choice = int(input("Select AN OPTION :"))
    if user_choice == 1:
        add_task()
    elif user_choice == 2:
        view_task()
    elif user_choice == 3:
        mark_complete()
    elif user_choice == 4:
        delete_task()
    elif user_choice == 5:
        print("thank you for yosing our simple todo app good bye")
        break
