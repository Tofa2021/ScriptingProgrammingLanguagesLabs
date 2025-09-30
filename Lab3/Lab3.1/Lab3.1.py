with open("F1.txt","w") as file_1:
    while (string := input("Введите строку: ")) != "":
        file_1.write(string + "\n")

with open("F1.txt") as file_1, open("F2.txt","w") as file_2:
    file_2.writelines(s for s in file_1 if s.rstrip()[-1] == "A")
