students = {}


# 1: Add Student

def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")
    admission = input("Enter Admission Date: ")
    fee = input("Enter Fee: ")

    students[name] = {
        "Age": age,
        "Gender": gender,
        "Course": course,
        "Admission": admission,
        "Fee": fee
    }

    print("\n✅ Student Added Successfully!\n")



# 2: Check Student Data

def check_student():
    name = input("Enter student name: ")

    if name in students:
        data = students[name]

        print("\n Data is as follows:\n")
        print("Name:", name)
        print("Age:", data["Age"])
        print("Gender:", data["Gender"])
        print("Course:", data["Course"])
        print("Admission:", data["Admission"])
        print("Fee:", data["Fee"])
    else:
        print("\n❌ Student not found!\n")



# MAIN MENU

while True:
    print("\n School Management System")
    print("1: Add Student")
    print("2: Check Student Data")
    print("3: Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        check_student()
    elif choice == "3":
        print("Exiting system...")
        break
    else:
        print("❌ Invalid choice")