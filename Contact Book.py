import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize data storage
        self.contacts = {}

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame for form input
        self.form_frame = tk.LabelFrame(self.root, text="Contact Details", padx=10, pady=10, bg="#f0f0f0")
        self.form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Define labels and entries for contact details
        tk.Label(self.form_frame, text="Name", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(self.form_frame, text="Mobile Number", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.mobile_entry = tk.Entry(self.form_frame)
        self.mobile_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(self.form_frame, text="Email", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(self.form_frame, text="Address", bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = tk.Entry(self.form_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Add contact button
        tk.Button(self.form_frame, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame for list and search
        self.list_frame = tk.LabelFrame(self.root, text="Contact List", padx=10, pady=10, bg="#f0f0f0")
        self.list_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Search box
        tk.Label(self.list_frame, text="Search", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_entry = tk.Entry(self.list_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        tk.Button(self.list_frame, text="Search", command=self.search_contact, bg="#2196F3", fg="white").grid(row=0, column=2, padx=5, pady=5)

        # Scrollbar and listbox
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.grid(row=1, column=2, sticky="ns")

        self.contact_listbox = tk.Listbox(self.list_frame, width=50, height=15, yscrollcommand=self.scrollbar.set)
        self.contact_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.scrollbar.config(command=self.contact_listbox.yview)
        self.contact_listbox.bind('<<ListboxSelect>>', self.on_contact_select)

        # Update and Delete buttons
        tk.Button(self.list_frame, text="Update Contact", command=self.update_contact, bg="#FFC107").grid(row=2, column=0, pady=5, sticky="ew")
        tk.Button(self.list_frame, text="Delete Contact", command=self.delete_contact, bg="#F44336", fg="white").grid(row=2, column=1, pady=5, sticky="ew")

        # Configure grid weights for responsive design
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        self.form_frame.grid_rowconfigure(4, weight=1)
        self.list_frame.grid_rowconfigure(1, weight=1)

        # Update contact list initially
        self.update_contact_list()

    def add_contact(self):
        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and mobile and email and address:
            if name in self.contacts:
                messagebox.showwarning("Duplicate Entry", "Contact with this name already exists.")
                return
            self.contacts[name] = {'mobile': mobile, 'email': email, 'address': address}
            self.update_contact_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def update_contact_list(self, search_query=""):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            if search_query.lower() in name.lower():
                self.contact_listbox.insert(tk.END, name)

    def search_contact(self):
        query = self.search_entry.get().strip()
        self.update_contact_list(query)

    def on_contact_select(self, event):
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected[0])
            contact = self.contacts.get(name)
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.mobile_entry.delete(0, tk.END)
            self.mobile_entry.insert(0, contact['mobile'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, contact['address'])

    def update_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            old_name = self.contact_listbox.get(selected[0])
            new_name = self.name_entry.get().strip()
            mobile = self.mobile_entry.get().strip()
            email = self.email_entry.get().strip()
            address = self.address_entry.get().strip()
            if new_name and mobile and email and address:
                if new_name != old_name and new_name in self.contacts:
                    messagebox.showwarning("Duplicate Entry", "Contact with this name already exists.")
                    return
                self.contacts.pop(old_name)
                self.contacts[new_name] = {'mobile': mobile, 'email': email, 'address': address}
                self.update_contact_list()
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "All fields are required.")

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected[0])
            del self.contacts[name]
            self.update_contact_list()
            self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Create the main application window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
