students = []
# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")
    for student in students:
        if student["roll"] == roll:
            print("Error: A student with this Roll Number already exists!\n")
            return
   
    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            if age>0:
                break
            print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")    
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully.\n")

# Function to view all students

def view_students():

    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\nStudent Records:")

    for student in students:
        print("----------------------")
        print("Roll Number :", student["roll"])
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])

    print()

# Function to search student

def search_student():

    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll"] == roll:

            print("\nStudent Found")
            print("----------------------")
            print("Roll Number :", student["roll"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print()

            return

    print("Student not found.\n")

# Function to update student

def update_student():

    roll = input("Enter Roll Number to Update: ")

    for student in students:

        if student["roll"] == roll:

            print("Enter New Details")

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            print("Student details updated successfully.\n")

            return

    print("Student not found.\n")

# Function to delete student

def delete_student():

    roll = input("Enter Roll Number to Delete: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student deleted successfully.\n")

            return

    print("Student not found.\n")

# Main menu function

def menu():

    while True:

        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.\n")

# Program starts here
menu()