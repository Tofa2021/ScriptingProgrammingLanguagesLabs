with open("Students.txt", "r", encoding = 'utf-8') as file:
    lines = file.readlines()

bad_students = [info[0] for line in lines if 4 < float((info := line.split())[1]) <= 6]
good_students = [info[0] for line in lines if 6 < float((info := line.split())[1]) <= 8]
excellent_students = [info[0] for line in lines if 8 < float((info := line.split())[1]) <= 10]

print("Студенты со средним баллом от 4 до 6")
print(bad_students)
print("Студенты со средним баллом от 6 до 8")
print(good_students)
print("Студенты со средним баллом от 8 до 10")
print(excellent_students)
