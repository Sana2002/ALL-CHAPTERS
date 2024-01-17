## Exercise II: Working with JSON file (Extension)
# In the above Exercise 4: Working with JSON File add details of another student and display the contents of JSON File.

import json

def write_to_json(student_details):
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file)

def read_and_display():
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    print("\nDetails of the Student are")
    print(f"\tName: {student_details['Name']}")
    print(f"\tID: {student_details['ID']}")
    print(f"\tcourse: {student_details['course']}")
    
    # Check if CourseDetails exists before accessing its values
    if 'CourseDetails' in student_details:
        print(f"\tGroup: {student_details['CourseDetails']['Group']}")
        print(f"\tYear: {student_details['CourseDetails']['Year']}")

def add_student_details():
    student_details = {}
    student_details["Name"] = input("Enter student name: ")
    student_details["ID"] = int(input("Enter student ID: "))
    student_details["course"] = input("Enter student course: ")

    course_details = {
        "Group": input("Enter student group: "),
        "Year": int(input("Enter student year: "))
    }

    student_details["CourseDetails"] = course_details

    return student_details

if __name__ == "__main__":
    # Read existing details
    read_and_display()

    # Add details for another student
    new_student_details = add_student_details()

    # Read and display updated details
    write_to_json(new_student_details)
    read_and_display()
