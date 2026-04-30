# student_record.py

import sqlite3

# Connect to DB or create if not exists
conn = sqlite3.connect('student_records.db')
cursor = conn.cursor()

# Create Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    branch TEXT,
    year INTEGER,
    email TEXT
)
''')
conn.commit()

# Functions for CRUD
def add_student():
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = int(input("Enter Year: "))
    email = input("Enter Email: ")
    cursor.execute("INSERT INTO students (name, branch, year, email) VALUES (?, ?, ?, ?)",
                   (name, branch, year, email))
    conn.commit()
    print("✅ Student added successfully.\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for row in records:
        print(row)

def search_student():
    search = input("Enter ID or Name to search: ")
    cursor.execute("SELECT * FROM students WHERE id=? OR name=?", (search, search))
    data = cursor.fetchall()
    for row in data:
        print(row)

def update_student():
    sid = input("Enter ID of student to update: ")
    name = input("Enter New Name: ")
    branch = input("Enter New Branch: ")
    year = int(input("Enter New Year: "))
    email = input("Enter New Email: ")
    cursor.execute("UPDATE students SET name=?, branch=?, year=?, email=? WHERE id=?",
                   (name, branch, year, email, sid))
    conn.commit()
    print("✅ Record updated.\n")

def delete_student():
    sid = input("Enter ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    print("🗑️ Student deleted.\n")

# Menu Loop
while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Try again.")
