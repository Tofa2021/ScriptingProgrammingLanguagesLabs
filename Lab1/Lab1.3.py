my_list = [12, 511, 'Python', 311, 122, 'love']
for element in my_list:
    if isinstance(element, int):
        if element % 2 == 0:
            digits_sum = sum(int(digit) for digit in str(abs(element)) if int(digit) % 2 == 0)
            print(f"Сумма цифр числа {element} {digits_sum}")
        else:
            my_list[my_list.index(element)] = 1
print(my_list)
