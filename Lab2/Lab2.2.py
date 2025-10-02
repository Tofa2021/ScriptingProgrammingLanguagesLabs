from sympy import primerange

def fun(fun_input):
    match fun_input:
        case list():
            evens = [i for i in fun_input if i % 2 == 0]
            print(f"Четные числа: {evens}")

            negatives = [i for i in fun_input if i < 0]
            if len(negatives) >= 2:
                return sum(fun_input[negatives[1] + 1:])
            else:
                print("Нет двух отрицательных чисел")
                return 0

        case set():
            return max(fun_input), min(fun_input)

        case int():
            print(f"Все простые числа до {fun_input}: {list(primerange(0, fun_input))}")

        case str():
            digits = [i for i in fun_input if i.isdigit()]
            print(f"Цифры в строке: {digits}")

numbers_list = [3, -4, 3, -1, 3, 4, 4, 8]
print(f"Сумма чисел после второго отрицательного {fun(numbers_list)}")

numbers_set = {1, 4, 6, -1, 4, 0, 9}
max_element, min_element = fun(numbers_set)
print(f"Максимальный: {max_element}")
print(f"Минимальный: {min_element}")

fun(20)

string = "hu21uk3gjg4k1gkljg5kju1g1-5h1lkj3gh51l3"
fun(string)