try:
    print("Введите делимое")
    a = int(input())
    print("Введие делитель")
    b = int(input())
    c = a / b
    print(f"Частное: {c}")
except ValueError:
    print("Делимое и делитель должны быть числами")
except ZeroDivisionError:
    print("Деление на ноль")
finally:
    print("Finally")