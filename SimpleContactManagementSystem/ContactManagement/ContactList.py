from Contact import Contact

from typing import Optional

class ContactList:
    def __init__(self, contacts: set[Contact]):
        self.contacts = contacts
    
    @property
    def contacts(self) -> set[Contact]:
        return self._contacts
    
    @contacts.setter
    def contacts(self, value: set[Contact]):
        if not isinstance(value, set):
            raise ValueError("Contacts must be a set")
        if not all(isinstance(contact, Contact) for contact in value):
            raise ValueError("All contacts must be of type Contact")
        self._contacts = value
    
    def add_contact(self, contact: Contact):
        if not isinstance(contact, Contact):
            raise ValueError("Only instances of Contact can be added")
        self.contacts.add(contact)
    
    def remove_contact(self, contact: Contact):
        if not isinstance(contact, Contact):
            raise ValueError("Only instances of Contact can be removed")
        if contact in self.contacts:
            self.contacts.discard(contact)
        else:
            raise ValueError("Contact not found")
    
    def update_contact(self, old_contact: Contact, new_contact: Contact):
        if not isinstance(old_contact, Contact) or not isinstance(new_contact, Contact):
            raise ValueError("Both old and new contacts must be instances of Contact")
        self.contacts.discard(old_contact)
        self.contacts.add(new_contact)
    
    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n")
    
    def search_contact(self, name: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact.name == name:
                return contact
        print("Contact not found")
        return None