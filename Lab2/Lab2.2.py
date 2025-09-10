from unittest import case

from sympy import primerange

def fun(fun_input):
    match fun_input:
        case list():
            even_numbers = []
            for element in fun_input:
                if element % 2 == 0:
                    even_numbers.append(element)
            print(f"Четные числа: {even_numbers}")

            is_first_negative_found = False
            second_negative_index = 0
            for index, element in enumerate(fun_input):
                if element < 0:
                    if is_first_negative_found:
                        second_negative_index = index
                        break
                    else:
                        is_first_negative_found = True
            if second_negative_index != 0:
                return sum(fun_input[second_negative_index + 1:])
            else:
                print("Нет двух отрицательных чисел")
                return 0
        case set():
            return max(fun_input), min(fun_input)
        case int():
            print(f"Все простые числа до {fun_input}: {list(primerange(0, fun_input))}")
            return None
        case str():
            digits = []
            for char in fun_input:
                if char.isdigit():
                    digits.append(int(char))
            print(f"Цифры в строке: {digits}")
            return None
        case _:
            return fun_input

numbers_list = [3, -4, 3, -1, 3, 4, 4, 8]
print(f"Сумма чисел после второго отрицательного {fun(numbers_list)}")

numbers_set = {1, 4, 6, -1, 4, 0, 9}
max_element, min_element = fun(numbers_set)
print(f"Максимальный: {max_element}")
print(f"Минимальный: {min_element}")

fun(20)

string = "hu21uk3gjg4k1gkljg5kju1g1-5h1lkj3gh51l3"
fun(string)