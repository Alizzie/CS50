students = ["Hermione", "Harry", "Ron"]

#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# More simple
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)