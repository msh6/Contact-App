'''Contact Application with CRUD functionailty'''

import json

class Contact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        
class AddressBook:
    def __init__(self):
        self.contacts = []
        
    def add_contacts(self, contact):
        self.contacts.append(contact)
        
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                break
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def edit_contact(self, name, new_address, new_phone, new_email):
        contact = self.search_contact(name)
        if contact:
            contact.address = new_address
            contact.phone = new_phone
            contact.email = new_email
            return True
        return False
    
    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print("Name: ", contact.name)
                print("Address: ", contact.address)
                print("Phone: ", contact.phone)
                print("Email: ", contact.email)
                print("-----------------------------")
        else:
            print("No contact found.")
            
    def save_to_file(self, filename):
        data = []
        for contact in self.contacts:
            contact_data = {
                "name": contact.name,
                "address": contact.address,
                "phone": contact.phone,
                "email": contact.email
            }
            data.append(contact_data)
        with open(filename, 'w') as file:
            json.dump(data, file)
    
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        for contact_data in data:
            contact = Contact(contact_data['name'], contact_data['address'], contact_data['phone'], contact_data['email'])
            self.contacts.append(contact)
    
# Create an instance of the AddressBook class
address_book = AddressBook()

# Load contacts from a file (if available)
address_book.load_from_file('address_book.json')

while True:
    print("Address Book Menu:")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Save and Quit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact = Contact(name, address, phone, email)
        address_book.add_contacts(contact)
        print("Contact added successfully.")
        
    elif choice == '2':
        name = input("Enter name to edit: ")
        contact = address_book.search_contact(name)
        if contact:
            new_address = input("Enter new address: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            address_book.edit_contact(name, new_address, new_phone, new_email)
            print("Contact edited successfully.")
        else:
            print("Contact not found.")

    elif choice == '3':
        name = input("Enter name to delete: ")
        address_book.delete_contact(name)
        print("Contact deleted successfully.")
        
    elif choice == '4':
        name = input("Enter name to search: ")
        contact = address_book.search_contact(name)
        if contact:
            print("Contact found:")
            print("Name:", contact.name)
            print("Address:", contact.address)
            print("Phone:", contact.phone)
            print("Email:", contact.email)
        else:
            print("Contact not found.")

    elif choice == '5':
        address_book.display_contacts()
        
    elif choice == '6':
        address_book.save_to_file('address_book.json')
        print("Address book saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")