#with open("students.csv") as file:
#    for line in file:
#        row = line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")


# Extraction
#students = []

#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {"name": name, "house": house}
#        students.append(student)

#for student in students:
#    print(f"{student['name']} is in {student['house']}")

#print(students)

# Sorting for a dictionary
students = []

#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        students.append({"name": name, "house": house})

# Wtih csv library
import csv
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

def get_name(student):
    return student["name"]


#for student in sorted(students, key=get_name):
#    print(f"{student['name']} is in {student['house']}")

# Lambda function 
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")