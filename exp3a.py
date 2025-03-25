
todo_list = []

todo_list.append("Buy groceries")
todo_list.append("Clean the house")
todo_list.append("Pay bills")

print("Current To-Do List:")
print(todo_list)

todo_list.remove("Clean the house")
print("\nAfter completing a task:")
print(todo_list)

todo_list.insert(0, "Finish project report")
print("\nAfter adding a high-priority task:")
print(todo_list)

todo_list.sort()
print("\nAfter sorting the tasks alphabetically:")
print(todo_list)

todo_list.reverse()
print("\nAfter reversing the task order:")
print(todo_list)

todo_list.clear()
print("\nAfter clearing all tasks:")
print(todo_list)