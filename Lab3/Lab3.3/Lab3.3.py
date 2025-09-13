file = open("Subjects.txt", "r", encoding = "utf-8")
lines = file.readlines()
file.close()

dict = {}
for line in lines:
    split_line = line.split()
    subject_name = split_line[0][:-1]
    hours = split_line[1:]

    total_hours = 0
    for hour in hours:
        total_hours += int(hour.split(sep = "(")[0])

    dict[subject_name] = total_hours
print(dict)