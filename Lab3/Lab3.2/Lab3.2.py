file = open("Students.txt", "r", encoding = 'utf-8')
lines = file.readlines()
file.close()

bad_students = []
good_students = []
excellent_students = []

for line in lines:
    info = line.split()
    surname = info[0]
    mark = float(info[1])
    if 4 < mark <= 6:
        bad_students.append(surname)
    elif 6 < mark <= 8:
        good_students.append(surname)
    elif 8 < mark <= 10:
        excellent_students.append(surname)

print("Студенты со средним баллом от 4 до 6")
print(bad_students)
print("Студенты со средним баллом от 6 до 8")
print(good_students)
print("Студенты со средним баллом от 8 до 10")
print(excellent_students)