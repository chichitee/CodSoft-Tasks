import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Listbox, Frame, Entry, Button

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x500")  # Set window size
        self.root.configure(bg='#000000')  # Black background color

        self.tasks = []

        # Header Section
        self.header_frame = Frame(root, bg='#FF69B4', padx=10, pady=10)
        self.header_frame.pack(fill=tk.X)
        
        self.header_label = tk.Label(self.header_frame, text="To-Do List Application", bg='#FF69B4', fg='#000000', font=('Arial', 16, 'bold'))
        self.header_label.pack()

        # Form Section
        self.form_frame = Frame(root, bg='#222222', padx=20, pady=20)
        self.form_frame.pack(pady=20, padx=20, fill=tk.X)
        
        self.task_label = tk.Label(self.form_frame, text="Enter your task:", bg='#222222', fg='#FF69B4', font=('Arial', 12, 'bold'))
        self.task_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        self.task_entry = Entry(self.form_frame, width=40, bg='#333333', fg='#FFFFFF', font=('Arial', 12), borderwidth=2, relief='solid')
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.add_button = Button(self.form_frame, text="Add Task", command=self.add_task, bg='#FF69B4', font=('Arial', 12, 'bold'), fg='#000000', relief='raised')
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.remove_button = Button(self.form_frame, text="Remove Selected Task", command=self.remove_task, bg='#FF69B4', font=('Arial', 12, 'bold'), fg='#000000', relief='raised')
        self.remove_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.update_button = Button(self.form_frame, text="Update Selected Task", command=self.update_task, bg='#FF69B4', font=('Arial', 12, 'bold'), fg='#000000', relief='raised')
        self.update_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Task List Section
        self.task_list_frame = Frame(root, bg='#000000')
        self.task_list_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.task_listbox = Listbox(self.task_list_frame, width=60, height=15, bg='#333333', font=('Arial', 12), selectmode=tk.SINGLE, fg='#FFFFFF', borderwidth=2, relief='solid')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = Scrollbar(self.task_list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    
    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Enter the new task description:")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
