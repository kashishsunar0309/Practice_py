"""3. To-Do List (Basic Version)
Show a menu:
Add task
View tasks
Remove task
Exit

Use a list to store tasks
Keep running until user chooses Exit
"""
print("======MENU========")
option = ['1. Add Task','2. View Tasks','3. Remove task','4. Exit']
print(option)
tasks = []
for i in range(1,10000):
  num = int(input("Enter the number option :"))
  if num == 1:
    task_name = input("Enter the tasks: ")
    tasks.append(task_name)
    print(f"Adding .... {tasks}")
  elif num == 2:
    print("TASK-View ...")
    print(tasks)
  elif num == 3:
    tasks_remove = input("Enter the tasks: ")
    if tasks_remove in tasks:
      tasks.remove(tasks_remove)
      print(f"Removing Task ...{tasks_remove}")
    else:
      print("NOT-FOUND")
  elif num == 4:
    print("Exiting ...")
    break;