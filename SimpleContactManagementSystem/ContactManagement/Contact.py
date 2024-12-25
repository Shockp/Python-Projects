import re

class Contact:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value
        
    @property
    def phone(self) -> str:
        return self._phone
    
    @phone.setter
    def phone(self, value: str):
        if not re.match("^\+?\d{7,15}$", value):
            raise ValueError("Invalid phone number. Example: +1234567890")
        self._phone = value
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str):
        if not re.match("^[^@]+@[^@]+\.[^@]+$", value):
            raise ValueError("Invalid email address. Example: example@domain.com")
        self._email = value
        
    def to_dict(self) -> dict:
        return {"name": self.name, "phone": self.phone, "email": self.email}
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\n"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Contact):
            return self.number == other.number
        return False