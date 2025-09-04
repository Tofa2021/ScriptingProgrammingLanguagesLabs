n = str(input("Введите натуральное число"))
result = 0
for num in n:
    if int(num) % 2 == 0:
        result += int(num)
print(result)
