# Task : For contacts book, create a CRUD application using in-memory data structure
# You'll build functions for
# 1. Adding a new contact
# 2. List/Search all contacts
# 3. Modify contact by name
# 4. Remove contact by detail

{
  "name": "Alice",
  "email": "alice@example.com",
  "phone": "1234567890"
}

contacts = []

def add_contact(name, email, phone):
    contact = {
  "name": name,
  "email": email,
  "phone": phone
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully")

def list_contacts():
    if not contacts:
        print("No contacts found")
        return
    for index, contact  in enumerate(contacts):
        print(f"{index}. {contact['name']} - {contact['email']} - {contact['phone']}")

def update_contact(name, new_email=None, new_phone=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_email:
                contact['email'] = new_email
            if new_phone:
                contact['phone'] = new_phone
            print(f"Contact {name} updated successfully")
            return
        print(f"Contact {name} not found")

def delete_contact(name):
    global contacts
    contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    # Only those contacts whose names do not match the given name are kept in the new list.
    print(f"Contact deleted: {name}")

add_contact("Alice", "alice@example.com", "1234567890")
add_contact("Bob", "bob@example.com", "0987654321")
list_contacts()
update_contact("Alice", "aliice@example.com", "1334567890")
list_contacts()
delete_contact("Bob")
list_contacts()







