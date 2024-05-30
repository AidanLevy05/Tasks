import tkinter as tk

# constants
file = "tasks.txt"

class Todo:
    def __init__(self, root):
        # Initialize tasks
        self.tasks = []

        # Screen
        self.root = root
        self.root.title("To-Do List")

        # Label
        self.label = tk.Label(root, text="Click '+' to \nadd a new task!", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # + Button
        self.add_button = tk.Button(root, text="+", command=self.add_task, font=("Helvetica", 14))
        self.add_button.pack(side="bottom", padx=20)

        # Save all
        self.save_all_button = tk.Button(root, text="Save all", command=self.save_all, font=("Helvetica", 14))
        self.save_all_button.pack(side="bottom", padx=20)

        # Load last save
        self.load_button = tk.Button(root, text="Load", command=self.load_save, font=("Helvetica", 14))
        self.load_button.pack(side="bottom", padx=20)

    def add_task(self):
        # Frame to hold each task
        task_frame = tk.Frame(self.root)
        task_frame.pack(pady=5)

        # Create new entry
        new_entry = tk.Entry(task_frame, font=("Helvetica", 14))
        new_entry.pack(side="left", padx=10)

        # Track the state of the check button
        check_var = tk.BooleanVar()

        # Create check button
        new_check = tk.Checkbutton(task_frame, text="Done", variable=check_var, font=("Helvetica", 14))
        new_check.pack(side="left")

        # Create remove button
        remove_button = tk.Button(task_frame, text="Remove", font=("Helvetica", 14), command=lambda: self.remove_task(task_frame, (new_entry, check_var)))
        remove_button.pack(side="left")

        # Bind Enter key to save input
        new_entry.bind("<Return>", lambda event: self.save_task(new_entry, check_var))

        # Save the task entry and check button state in a list
        self.tasks.append((new_entry, check_var))

    def save_task(self, entry, check_var):
        task_text = entry.get()
        task_bool = check_var.get()
        print(f"Task: {task_text} | Completed: {task_bool}")

    def save_all(self):
        # Save all tasks to file
        with open(file, 'w') as f:
            for entry, check_var in self.tasks:
                task_text = entry.get()
                task_bool = check_var.get()
                f.write(f"{task_text},{int(task_bool)}\n")
        print(f"Tasks saved to {file}")

    def load_save(self):
        # Read tasks in from file
        with open(file, 'r') as f:
            for line in f:
                task_text, task_bool = line.strip().split(',')
                self.add_task()
                new_entry, check_var = self.tasks[-1]
                new_entry.insert(0, task_text)
                check_var.set(int(task_bool))
        print(f"Tasks loaded from {file}")

    def remove_task(self, frame, task):
        # Remove task frame from GUI
        frame.pack_forget()

        # Remove task from list
        self.tasks.remove(task)

if __name__ == "__main__":
    root = tk.Tk()
    app = Todo(root)
    root.mainloop()