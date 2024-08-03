import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x500")
        self.root.configure(bg='#FFC0CB')  # Light pink background
        
        self.contacts = {}
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Contact Manager", font=('Arial', 18, 'bold'), bg='#FFC0CB', fg='#000000')
        self.title_label.pack(pady=20)

        # Add Contact Button
        self.add_button = tk.Button(self.root, text="Add Contact", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=self.add_contact)
        self.add_button.pack(pady=5)

        # View Contact List Button
        self.view_button = tk.Button(self.root, text="View Contacts", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=self.view_contacts)
        self.view_button.pack(pady=5)

        # Search Contact Button
        self.search_button = tk.Button(self.root, text="Search Contact", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=self.search_contact)
        self.search_button.pack(pady=5)

        # Update Contact Button
        self.update_button = tk.Button(self.root, text="Update Contact", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=self.update_contact)
        self.update_button.pack(pady=5)

        # Delete Contact Button
        self.delete_button = tk.Button(self.root, text="Delete Contact", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=self.delete_contact)
        self.delete_button.pack(pady=5)

        # Result Text Area
        self.result_text = tk.Text(self.root, height=15, width=70, font=('Arial', 12), bg='#FFFFFF', fg='#000000', wrap=tk.WORD)
        self.result_text.pack(pady=20)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name or name in self.contacts:
            messagebox.showerror("Error", "Invalid or duplicate contact name.")
            return

        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        if not self.contacts:
            self.result_text.insert(tk.END, "No contacts available.")
            return
        
        contacts_list = "\n".join([f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n" for name, info in self.contacts.items()])
        self.result_text.insert(tk.END, f"Contacts:\n{contacts_list}")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search term.")
            return
        
        self.result_text.delete(1.0, tk.END)
        result = ""
        for name, info in self.contacts.items():
            if query.lower() in name.lower() or query in info['phone']:
                result += f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n"

        if result:
            self.result_text.insert(tk.END, f"Search Results:\n{result}")
        else:
            self.result_text.insert(tk.END, "No matching contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        phone = simpledialog.askstring("Input", "Enter new phone number:")
        email = simpledialog.askstring("Input", "Enter new email:")
        address = simpledialog.askstring("Input", "Enter new address:")

        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
