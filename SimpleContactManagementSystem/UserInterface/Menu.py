from ContactManagement.ContactList import ContactList

class Menu:
    def __init__(self):
        self.contact_list = ContactList(set())
    
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
        self.contact_list.add_contact(name, phone, email)
    
    def remove_contact(self):
        number = input("Enter number to remove: ")
        contact = self.contact_list.search_contact(number)
        if contact:
            self.contact_list.remove_contact(number)
        else:
            print("Contact not found")
            
    def update_contact(self):
        number = input("Enter number to update: ")
        contact = self.contact_list.search_contact(number)
        if contact:
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            self.contact_list.update_contact(number, name, phone, email)
        else:
            print("Contact not found")
    
    def view_contacts(self):
        print(self.contact_list)
    
    def search_contact(self):
        number = input("Enter number: ")
        contact = self.contact_list.search_contact(number)
        if contact:
            print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n")
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
                break
            else:
                print("Invalid choice")