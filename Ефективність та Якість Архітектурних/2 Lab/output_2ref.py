class ContactInfo:
    def __init__(self, phone_code, phone_number):
        self.phone_code = phone_code
        self.phone_number = phone_number

    def get_full_phone_number(self):
        return f"{self.phone_code}{self.phone_number}"

class UserType:
    ENGINEER = "Engineer"
    MANAGER = "Manager"

class User:
    def __init__(self, name, age, user_type, contact_info):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.contact_info = contact_info

    def print_details(self):
        # Виведення інформації про користувача
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type)
        print("Phone:", self.contact_info.get_full_phone_number())

# Приклад використання класу
contact_info = ContactInfo("050", "9379992")
user = User("John", 25, UserType.ENGINEER, contact_info)
user.print_details()
