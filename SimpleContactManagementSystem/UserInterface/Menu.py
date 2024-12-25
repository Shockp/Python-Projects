from ContactManagement.Contact import Contact
from ContactManagement.ContactList import ContactList

from typing import Optional

class Menu:
    def __init__(self):
        self.contact_list = ContactList()
    
    @property
    def contact_list(self) -> ContactList:
        return self._contact_list
    
    @contact_list.setter
    def contact_list(self, value: ContactList):
        if not isinstance(value, ContactList):
            raise ValueError("Contact list must be an instance of ContactList")
        self._contact_list = value
    
    @staticmethod
    def display_menu():
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Update contact")
        print("4. View contacts")
        print("5. Search contact")
        print("6. Exit")
    
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = Contact(name, phone, email)
        self.contact_list.add_contact(contact)
    
    def remove_contact(self):
        phone = input("Enter phone to remove: ")
        contact = self.contact_list.search_contact(phone)
        if contact:
            self.contact_list.remove_contact(contact)
        else:
            print("Contact not found")
            
    def update_contact(self):
        phone = input("Enter phone number to update: ")
        contact = self.contact_list.search_contact(phone)
        if contact:
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            
            existing_contact = self.contact_list.search_contact(phone)
            if existing_contact:
                print("Phone number already in use.")
            else:
                self.contact_list.update_contact(contact, Contact(name, phone, email))
        else:
            print("Contact not found")
                
    def view_contacts(self):
        print("Contacts:\n")
        print(self.contact_list)
    
    def search_contact(self, phone: str) -> Optional[Contact]:
        phone = input("Enter phone number to search: ")
        contact = self.contact_list.search_contact(phone)
        if contact:
            print(contact)
        else:
            print("Contact not found")
            
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.remove_contact()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.view_contacts()
            elif choice == "5":
                self.search_contact()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")