import tkinter as tk
from tkinter import messagebox, font

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Set main window background color to white
        self.root.configure(bg='white')

        # Set main frame background color to light blue baby (#ADD8E6)
        self.frame = tk.Frame(root, bg='#ADD8E6')
        self.frame.pack(pady=10)

        # Add a title label to the body
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.title_label = tk.Label(self.frame, text="TO DO LIST", bg='#ADD8E6', font=title_font)
        self.title_label.pack(pady=10)

        self.task_frame = tk.Frame(self.frame, bg='#ADD8E6')
        self.task_frame.pack()

        self.canvas = tk.Canvas(self.task_frame, width=400, height=300, bg='#ADD8E6')
        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#ADD8E6')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Define serif font for the entry widget
        serif_font = font.Font(family="Times", size=12)

        self.entry = tk.Entry(root, width=50, font=serif_font)
        self.entry.pack(pady=10)

        # Configure buttons with white background
        button_bg = 'white'

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg=button_bg)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg=button_bg)
        self.update_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg=button_bg)
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_task_complete, bg=button_bg)
        self.complete_button.pack(pady=5)

        # Define a custom font for tasks that is bold, uppercase, and serif
        self.task_font = font.Font(family="Times", size=10, weight="bold")

    def add_task(self):
        task = self.entry.get()
        if task:
            var = tk.BooleanVar()
            task_upper = task.upper()  # Convert task text to uppercase
            cb = tk.Checkbutton(self.scrollable_frame, text=task_upper, variable=var, bg='#ADD8E6', font=self.task_font)
            cb.pack(anchor="w")
            self.tasks.append((cb, var))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.get_selected_task_index()
            new_task = self.entry.get()
            if new_task:
                task_upper = new_task.upper()  # Convert task text to uppercase
                checkbox, var = self.tasks[selected_task_index]
                checkbox.config(text=task_upper)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def remove_task(self):
        try:
            selected_task_index = self.get_selected_task_index()
            checkbox, var = self.tasks.pop(selected_task_index)
            checkbox.destroy()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def mark_task_complete(self):
        try:
            selected_task_index = self.get_selected_task_index()
            checkbox, var = self.tasks[selected_task_index]
            checkbox.config(state=tk.DISABLED, fg='grey')
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def get_selected_task_index(self):
        for index, (checkbox, var) in enumerate(self.tasks):
            if var.get():
                return index
        raise IndexError

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
