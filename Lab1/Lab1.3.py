def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

list = [12, 511, 'Python', 311, 122, 'love']
for i in range(5):
    element = list[i]
    if element is int:
        if element % 2 == 0:
            print(f"Сумма цифр числа {element} {sum_of_digits(element)}")
        else:
            list[i] = 1
print(list)
