import tkinter as tk

# Function to add a task to the to-do list
def add_task():
    task = task_entry.get()
    priority = priority_entry.get()
    if task:
        todo_list[task] = priority
        update_listbox()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
    else:
        error_label.config(text="Please enter a task.", fg="red")

# Function to remove a task from the to-do list
def remove_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        task_index = int(selected_task[0])
        task = tasks_listbox.get(task_index)
        del todo_list[task]
        update_listbox()
    else:
        error_label.config(text="Please select a task to remove.", fg="red")

# Function to update the listbox with current tasks
def update_listbox():
    tasks_listbox.delete(0, tk.END)
    for task, priority in todo_list.items():
        tasks_listbox.insert(tk.END, f"{task} - Priority: {priority}")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.configure(background="#e6e6e6")

# Create and place widgets
task_label = tk.Label(root, text="Task:", bg="#e6e6e6")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=5, pady=5)

priority_label = tk.Label(root, text="Priority:", bg="#e6e6e6")
priority_label.grid(row=1, column=0, padx=5, pady=5)

priority_entry = tk.Entry(root, width=30)
priority_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=2, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#FF5733", fg="white")
remove_button.grid(row=1, column=2, padx=5, pady=5)

tasks_listbox = tk.Listbox(root, width=50)
tasks_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

error_label = tk.Label(root, fg="red", bg="#e6e6e6")
error_label.grid(row=3, column=0, columnspan=3)

# Initialize to-do list
todo_list = {}

# Start the GUI event loop
root.mainloop()


