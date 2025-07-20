import json
import os

contacts_file = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(contacts_file, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new name: ")
        contacts[index]['phone'] = input("Enter new phone: ")
        contacts[index]['email'] = input("Enter new email: ")
        print("Contact updated.")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        print("Contact deleted.")
    else:
        print("Invalid contact number.")

# Main loop
def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
