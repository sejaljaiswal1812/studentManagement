import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
conn.commit()


# Function to add student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("✅ Student Added Successfully!\n")


# Function to view students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No records found.\n")
    else:
        print("\n--- Student List ---")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
        print()


# Function to search student
def search_student():
    student_id = int(input("Enter Student ID: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    record = cursor.fetchone()

    if record:
        print(f"\nFound: ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Course: {record[3]}\n")
    else:
        print("❌ Student Not Found\n")


# Function to update student
def update_student():
    student_id = int(input("Enter Student ID to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")

    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", 
                   (name, age, course, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Student Updated Successfully!\n")
    else:
        print("❌ Student Not Found\n")


# Function to delete student
def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Student Deleted Successfully!\n")
    else:
        print("❌ Student Not Found\n")


# Main menu
def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()

