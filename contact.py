class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print()

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                contact.display()

    def search_contact(self, search_key):
        found_contacts = []
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone:
                found_contacts.append(contact)
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print(f"Matching contacts for '{search_key}':")
            for contact in found_contacts:
                contact.display()

    def update_contact(self, search_key, new_contact):
        for i, contact in enumerate(self.contacts):
            if search_key.lower() in contact.name.lower() or search_key in contact.phone:
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, search_key):
        for i, contact in enumerate(self.contacts):
            if search_key.lower() in contact.name.lower() or search_key in contact.phone:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.\n")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)

        elif choice == '4':
            search_key = input("Enter name or phone number of contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(search_key, new_contact)

        elif choice == '5':
            search_key = input("Enter name or phone number of contact to delete: ")
            contact_book.delete_contact(search_key)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
