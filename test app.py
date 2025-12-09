class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactsManager:
    def __init__(self):
        # dictionary: key = contact name, value = Contact object
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
            return
        self.contacts[name] = Contact(name, phone, email)
        print("Contact added successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found.")

    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print("Contact not found.")
            return

        if phone:
            self.contacts[name].phone = phone
        if email:
            self.contacts[name].email = email

        print("Contact updated.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        for contact in self.contacts.values():
            print(contact)

def main():
    manager = ContactsManager()

    while True:
        print("\n--- CONTACTS APP ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. List Contacts")
        print("6. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("New phone (leave blank to keep current): ")
            email = input("New email (leave blank to keep current): ")
            manager.update_contact(name, phone or None, email or None)

        elif choice == "5":
            manager.list_contacts()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()