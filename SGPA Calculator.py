# the function prints the SGPA in the given system
def printSGPA(credits, grades, system):
    SGPA = 0

    # mapping ductionary for grade to its equivalent points
    grade_map = {"EX": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "R": 0}

    # calculating SGPA and summing up for each subject
    valid_grades = ["EX", "A", "B", "C", "D", "E", "R"]
    for i in range(no_subs):
        if grades[i] not in valid_grades:
            print("\nInvalid Input!!")
            return
        grade_point = grade_map[grades[i]]
        if grade_point:
            SGPA += (credits[i] * grade_point) / sum(credits)
        else:
            print("Uh-oh! You failed this semester :(")
            return

    # print the SGPA in the given system
    print("\nSGPA: ", round((system * SGPA) / 10, 2))


no_subs = int(input("Enter no of subjects: "))
sub_credits = []  # holds subject wise credits
grades = []  # holds subject wise obtained grades

# gets input for each subject
for i in range(no_subs):
    print("\n", "Subject Number ", i + 1)
    sub_credit = float(input("Enter no of credits: "))
    grade = input("Enter the grade: ")
    sub_credits.append(sub_credit)
    grades.append(grade.upper())

# prints the grade in the given GPA system
system = float(input("\nGrade System: "))
printSGPA(sub_credits, grades, system)
