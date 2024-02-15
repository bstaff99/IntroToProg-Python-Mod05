# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   BStaff, 2/14/2024, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Converted to JSON
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

import json
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    json_data = json.load(file)     # removed previous code using a list and CSV and used json load code
    for each in json_data:
        student_data = {"FirstName" : each['FirstName'], "LastName" : each['LastName'], "CourseName" : each['CourseName']}
        students.append(student_data)
    file.close()
except FileNotFoundError as e:
    print("Please create file before running this script.\n")
    print("Technical Explanation: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("An unexpected error occurred.\n")
    print("Technical Explanation: ")
    print(e, e.__doc__, type(e), sep='\n')


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print("Please make sure to use only letters.\n")
            print("Technical Explanation: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("An unexpected error occurred.\n")
            print("Technical Explanation: ")
            print(e, e.__doc__, type(e), sep='\n')


    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for row in students:
            print(f"{row["FirstName"]} {row["LastName"]} is registered for {row["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            for row in students:
                print(f"{row["FirstName"]} {row["LastName"]} is registered for {row["CourseName"]}")
            continue
        except FileNotFoundError as e:
            print("Please create file before running this script.\n")
            print("Technical Explanation: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("An unexpected error occurred.\n")
            print("Technical Explanation: ")
            print(e, e.__doc__, type(e), sep='\n')


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
