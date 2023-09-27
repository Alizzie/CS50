# LISTS
students = ["Hermoine", "Harry", "Ron"]

#print(students[0])
#print(students[1])
#print(students[2])

# Improved
for student in students:
    print(student)

# Length and position in list
print("Length and position in list")
for i in range(len(students)):
    print(i + 1, students[i])


# DICTIONARIES

# Cumbersome
#students = ["Hermoine", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]


students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print("DICTIONARY access houses (values) only\n")
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("DICTIONARY access students (keys) only\n")
for student in students:
    print(student)

print("DICTIONARY access the key-values pair\n")
for student in students:
    print(student, students[student], sep=", ")

print("DICTIONARY with multiple values associated with one key\n")
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

