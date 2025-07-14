#sqlite is a inbuilt db in python, no external server is required

import sqlite3

# Connect to database (creates file if not exists)
connection = sqlite3.connect('connect.db')
cursor = connection.cursor()

# create table if not exists
cursor.execute('''
               CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT UNIQUE COLLATE NOCASE,
   email TEXT,
   phone TEXT
)
               ''')

connection.commit()

def add_contact(name, email, phone):
    try:
        cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        connection.commit()
        print(f"Contact {name} added.")
    except sqlite3.IntegrityError:
        print(f"Contact {name} already exists.")
    
def list_contacts():
    cursor.execute("SELECT name, email, phone FROM contacts")
    rows = cursor.fetchall()
    if not rows:
        print("No contacts found.")
        return
    print(f"{'Name':<15} {'Email':<30} {'Phone':<15}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<15} {row[1]:<30} {row[2]:<15}")

def update_contact(name, new_email=None, new_phone=None):
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    result = cursor.fetchone()
    if not result:
        print(f"Contact {name} not found.")
        return
    if new_email:
        cursor.execute("UPDATE contacts SET email = ? WHERE name = ?", (new_email, name))
    if new_phone:
        cursor.execute("UPDATE contacts SET phone = ? WHERE name = ?", (new_phone, name))
    connection.commit()
    print(f"Contact {name} updated.")

def delete_contact(name):
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
    if cursor.rowcount == 0:
        print(f"Contact {name} not found.")
    else:
        connection.commit()
        print(f"Contact {name} deleted.")

if __name__ == "__main__":
    add_contact("harsha", "harsha@example.com", "1234567890")
    add_contact("prince", "prince@example.com", "9876543210")
    list_contacts()
    update_contact("harsha", new_email="harsha_new@example.com")
    delete_contact("prince")
    list_contacts()


