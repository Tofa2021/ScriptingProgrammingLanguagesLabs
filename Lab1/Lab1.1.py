n = int(input("Введите натуральное число\n"))
print(sum(int(digit) for digit in str(n) if int(digit) % 2 == 0))
