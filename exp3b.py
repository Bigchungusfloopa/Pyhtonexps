
todo_list = ()

todo_list += ("Buy groceries",)
todo_list += ("Clean the house",)
todo_list += ("Pay bills",)

print("Current To-Do List:")
print(todo_list)

todo_list = tuple(task for task in todo_list if task != "Clean the house")
print("\nAfter completing a task:")
print(todo_list)

todo_list = ("Finish project report",) + todo_list
print("\nAfter adding a high-priority task:")
print(todo_list)

todo_list = tuple(sorted(todo_list))
print("\nAfter sorting the tasks alphabetically:")
print(todo_list)

todo_list = tuple(reversed(todo_list))
print("\nAfter reversing the task order:")
print(todo_list)

todo_list = ()
print("\nAfter clearing all tasks:")
print(todo_list)