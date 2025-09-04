toys_dict = {
    'Плюшевый Медведь':[
        'Искусственный мех, Синтепух, Пластик',
        120,
        5
    ],
    'Конструктор': [
        'Пластиковые детали, Металлические соединители, Инструкция из картона',
        75,
        9
    ],
}

def view_descriptions():
    print("Описания игрушек")
    for name, info in toys_dict.items():
        print(f"{name} – {info[0]}")

def view_prices():
    print("Цены игрушек")
    for name, info in toys_dict.items():
        print(f"{name} – {info[1]} руб.")

def view_counts():
    print("Количества игрушек")
    for name, info in toys_dict.items():
        print(f"{name} – {info[2]} шт.")

def view_all_info():
    print("Вся информация")
    for name, info in toys_dict.items():
        print(f"{name}:")
        print(f"  Состав: {info[0]}")
        print(f"  Цена: {info[1]} руб.")
        print(f"  В наличии: {info[2]} шт.")

def make_purchase():
    total_cost = 0
    bill = "Чек\n"
    while True:
        print("Доступные игрушки")
        for name, info in toys_dict.items():
            if info[2] > 0:
                print(name)

        toy_name = input("Введите название игрушки или 'n' для выхода\n")

        if toy_name == 'n':
            break

        if toy_name not in toys_dict:
            print("Такой игрушки нет в магазине")
            continue

        available_count = toys_dict[toy_name][2]
        print(f"В наличии: {available_count} шт.")

        count = int(input("Введите количество\n"))

        if count <= 0:
            print("Количество должно быть положительным")
            continue

        if count > available_count:
            print("Невозможное количество")
            continue

        price = toys_dict[toy_name][1]
        cost = count * price
        total_cost += cost
        toys_dict[toy_name][2] -= count

        print(f"Добавлено в корзину: {toy_name} x{count} = {cost} руб.")
        bill += (f"Название: {toy_name}\n"
                 f"Цена за шт:{price}\n"
                 f"{count} шт.\n"
                 f"Цена: {cost}\n")
    if total_cost != 0:
        bill += f"Итого: {total_cost}"
        print(bill)
    else:
        print("Ничего не куплено")

while True:
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Просмотр всей информации")
    print("5. Покупка")
    print("6. До свидания")

    choice = int(input("Выберите пункт меню\n"))

    match choice:
        case 1:
            view_descriptions()
        case 2:
            view_prices()
        case 3:
            view_counts()
        case 4:
            view_all_info()
        case 5:
            make_purchase()
        case 6:
            print("До свидания! Приходите еще!")
            break
        case _:
            print("Неверный выбор! Попробуйте снова.")