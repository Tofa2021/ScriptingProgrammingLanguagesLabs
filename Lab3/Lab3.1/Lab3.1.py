with open("F1.txt","w") as file_1:
    while (True):
        string = input("Enter a string: ")
        if string == "":
            break
        file_1.write(string + "\n")

with open("F1.txt","r") as file_1:
    strings = file_1.readlines()

with open("F2.txt","w") as file_2:
    for string in strings:
        if string[-2] == "A":
            file_2.write(string)
