try:
    a = int(input("Введите делимое:"))
    b = int(input("Введие делитель:"))
    c = a / b
    print(f"Частное: {c}")
except ValueError:
    print("Делимое и делитель должны быть числами")
except ZeroDivisionError:
    print("Деление на ноль")
finally:
    print("Finally")