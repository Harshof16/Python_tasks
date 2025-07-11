# Task: Perform CRUD operations on a CSV file

import csv
import os

csv_file = "contacts.csv"

def add_contact(name, email, phone):
    # Check if the contacts CSV file exists
    file_exists = os.path.isfile(csv_file)
    # Prevent duplicate contacts by name (case-insensitive)
    if file_exists:
        with open(csv_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].lower() == name.lower():
                    print(f"Contact {name} already exists.")
                    return
    # Determine if we need to write the header (if file is new or empty)
    write_header = not file_exists or os.stat(csv_file).st_size == 0
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Name", "Email", "Phone"])  # Write the header row only if file is new/empty
        writer.writerow([name, email, phone])  # Write the new contact's data
        print(f"Contact {name} added successfully")  # Confirm addition to the user
        return

def list_contacts():
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        contacts = list(reader)
        if not contacts:
            print("No contacts found.")
            return
        # Print header
        print(f"{'Name':<15} {'Email':<30} {'Phone':<15}")
        print("-" * 60)
        for row in contacts:
            print(f"{row['Name']:<15} {row['Email']:<30} {row['Phone']:<15}")

def update_contact(name, email=None, phone=None):
    updated = False
    rows = []
    with open(csv_file, "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == name.lower(): #fetching by their header name
                if email:
                    row['Email'] = email
                if phone:
                    row['Phone'] = phone
                updated = True
                print(f"Contact {name} updated successfully")
            rows.append(row)
    if not updated:
        print(f"Contact {name} not found")
    else:
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'Phone'])
            writer.writeheader()
            writer.writerows(rows)

def delete_contact(name):
    rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = [c for c in reader if c["Name"].lower() != name.lower()]
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'Phone'])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    add_contact('harsha','harsh@gmail.com','3424324')
    list_contacts()
    update_contact('harsha','lol@gmail.com')
    add_contact('prince','hassrsh@gmail.com','3424324')
    list_contacts()
    delete_contact('princE')
    list_contacts()