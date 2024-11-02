"""

Author:  Maiwase Tembo
Date written: 11/01/24
Assignment:   Module2  lab
Short Desc:   This python code classifies student GPAs as being on the Dean's List, Honor Roll (3.25) or neither

"""
#deanslisthonoroll.py

def main():
    while True:
        # Accept student's last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        
        # Quit if 'ZZZ' is entered
        if last_name.upper() == 'ZZZ':
            print("Exiting the program.")
            break
        
        # Accept student's first name
        first_name = input("Enter student's first name: ")
        
        # Accept and validate student's GPA
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a number.")
            continue
        
        # Check for Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        # Check for Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.").ven
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")

# Run the program
main()
