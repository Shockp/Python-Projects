from .Contact import Contact

from typing import Optional

class ContactList:
    def __init__(self, contacts: dict[str, Contact] = None):
        self.contacts = contacts if contacts is not None else {}
    
    @property
    def contacts(self) -> dict[str, Contact]:
        return self._contacts
    
    @contacts.setter
    def contacts(self, value: dict[str, Contact]):
        if not isinstance(value, dict):
            raise ValueError("Contacts must be a dictionary")
        if not all(isinstance(contact, Contact) for contact in value.values()):
            raise ValueError("All values in the dictionary must be instances of Contact")
        self._contacts = value
    
    def add_contact(self, contact: Contact):
        if not isinstance(contact, Contact):
            raise ValueError("Only instances of Contact can be added")
        if contact.phone in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[contact.phone] = contact
    
    def remove_contact(self, contact: Contact):
        if not isinstance(contact, Contact):
            raise ValueError("Only instances of Contact can be removed")
        if contact.phone in self.contacts:
            del self.contacts[contact.phone]
        else:
            raise ValueError("Contact not found")
    
    def update_contact(self, old_contact: Contact, new_contact: Contact):
        if not isinstance(old_contact, Contact) or not isinstance(new_contact, Contact):
            raise ValueError("Both old and new contacts must be instances of Contact")
        if old_contact.phone in self.contacts:
            self.contacts[old_contact.phone] = new_contact
    
    def view_contacts(self) -> str:
        return "\n".join(str(contact) for contact in self.contacts.values())
    
    def search_contact(self, phone: str) -> Optional[Contact]:
        return self.contacts.get(phone)
    
    def to_list_of_dicts(self) -> list[dict]:
        return [contact.to_dict() for contact in self.contacts.values()]
    
    def __str__(self) -> str:
        return "\n".join(str(contact) for contact in self.contacts.values())