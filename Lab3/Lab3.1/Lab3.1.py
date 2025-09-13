file1 = open("F1.txt","w")

while (True):
    string = input("Enter a string: ")
    if string == "":
        break
    file1.write(string + "\n")
file1.close()

file1 = open("F1.txt","r")
strings = file1.readlines()
print(strings)
file1.close()

file2 = open("F2.txt","w")
for string in strings:
    if string[-2] == "A":
        file2.write(string)
file2.close()
