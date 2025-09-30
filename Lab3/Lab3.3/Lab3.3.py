with open("Subjects.txt", encoding="utf-8") as file:
    subject_hours_dict = {
        parts[0][:-1]: sum(int(h.split("(")[0]) for h in parts[1:])
        for parts in (line.split() for line in file)
    }

print(subject_hours_dict)
