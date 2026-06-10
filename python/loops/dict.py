# students = {"Alice": "Gryffindor", "Bob": "Hufflepuff", "Charlie": "Ravenclaw", "David": "Slytherin", "Eve": "Hufflepuff"}

# for student in students: 
#     if students[student] == "Gryffindor":
#         print(f"{student} is in Gryffindor.")
#     else:
#         continue

# students = [
#     {"name": "Alice", "house": "Gryffindor", "patronus": "Lion"},
#     {"name": "Bob", "house": "Hufflepuff", "patronus": "Badger"},
#     {"name": "Charlie", "house": "Ravenclaw", "patronus": "Eagle"},
#     {"name": "David", "house": "Slytherin", "patronus": "Snake"},
#     {"name": "Eve", "house": "Hufflepuff", "patronus": None}
# ]

# for student in students:
#     print(f"{student['name']} is in {student['house']} and their patronus is a {student['patronus']}.")


for i in range(7):
    for j in range(7):
        print(f"#", end="")
    print("")