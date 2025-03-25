import os

# Define the filename for storing student data
FILE_NAME = "C:\\Users\\arjun\\Desktop\\pioneer projects\\student_report_card\\student.txt"

# Function to load the student data from the file
def load_student_data():
    students = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                name, subjects_str = line.strip().split(' | ')
                subjects = eval(subjects_str)  # Convert string back to dictionary
                students[name] = subjects
    return students

# Function to save the student data to the file
def save_student_data(students):
    with open(FILE_NAME, 'w') as file:
        for name, subjects in students.items():
            file.write(f"{name} | {str(subjects)}\n")

# Function to compute the average score and assign grade
def compute_average_and_grade(grades):
    average = sum(grades) / len(grades)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return average, grade

# Function to add a student and their grades
def add_student(students):
    name = input("Enter student's name: ")
    subjects = {}
    
    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject_name = input("Enter subject name: ")
        grade = float(input(f"Enter grade for {subject_name}: "))
        subjects[subject_name] = grade
    
    students[name] = subjects
    save_student_data(students)
    print(f"Student {name} added successfully.")

# Function to display a student’s report card
def display_report_card(students):
    name = input("Enter the student's name to display report card: ")
    if name in students:
        subjects = students[name]
        print(f"\nReport Card for {name}")
        print("===============================")
        total_grades = []
        for subject, grade in subjects.items():
            print(f"{subject}: {grade}")
            total_grades.append(grade)
        
        average, grade = compute_average_and_grade(total_grades)
        print(f"\nAverage Score: {average:.2f}")
        print(f"Grade: {grade}")
    else:
        print(f"No data found for student {name}.")

# Function to display the main menu
def display_menu():
    print("\n===== Student Report Card System =====")
    print("1. Add Student and Grades")
    print("2. Display Student Report Card")
    print("3. Exit")

# Main function to run the student report card system
def main():
    students = load_student_data()

    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_report_card(students)
        elif choice == '3':
            print("Exiting the Student Report Card System.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
