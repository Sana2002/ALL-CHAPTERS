# Create a JSON file named 'StudentJson.json' with the following details
# 1. Ask the user to enter the student name, ID, and course and write these contents to the JSON file.
# 2.Read the contents from the JSON file and display the individual values.  
#   Expected Output :
#   ```
#   Details of the Student are
#  		Name: Alpha
#  		ID: 1
#  		course: BSc CC
# ```
# 3. Append another dictionary as follows as key value pair for student 1 in StudentDetails dictionary to form a nested dictionay. Later update the JSON file.
# ```
#  "CourseDetails":{ 
#              		 "Group": "A",
#              		 "Year": 2
# 		}
# ```
# 4. Print the individual vlaues of the Student details reading from JSON file.

#   Expected Output :
# ```
# Details of the Student are
# 		  Name: Alpha
# 		  ID: 1
#  		 course: BSc CC
#  		 Group: A
#  		 Year: 2
# ```
 
import json

# Task 1: Write to JSON file
def write_to_json():
    student_details = {}
    student_details["Name"] = input("Enter student name: ")
    student_details["ID"] = int(input("Enter student ID: "))
    student_details["course"] = input("Enter student course: ")

    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file)

# Task 2: Read from JSON file and display values
def read_and_display():
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    print("\nDetails of the Student are")
    print(f"\tName: {student_details['Name']}")
    print(f"\tID: {student_details['ID']}")
    print(f"\tcourse: {student_details['course']}")

# Task 3: Append and update JSON file
def append_and_update():
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    course_details = {
        "Group": "A",
        "Year": 2
    }

    student_details["CourseDetails"] = course_details

    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file)

# Task 4: Print updated individual values
def print_updated_values():
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    print("\nDetails of the Student are")
    print(f"\tName: {student_details['Name']}")
    print(f"\tID: {student_details['ID']}")
    print(f"\tcourse: {student_details['course']}")
    print(f"\tGroup: {student_details['CourseDetails']['Group']}")
    print(f"\tYear: {student_details['CourseDetails']['Year']}")

if __name__ == "__main__":
    # Task 1
    write_to_json()

    # Task 2
    read_and_display()

    # Task 3
    append_and_update()

    # Task 4
    print_updated_values()
