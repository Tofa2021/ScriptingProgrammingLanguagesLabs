my_dict = {'a':12, 'b':13, 'c': 56,'d':400, 'e':58, 'f': 20}

sorted_my_dict = sorted(my_dict.items(), key=lambda x: x[1])
smallest_items = sorted_my_dict[:3]
for item in smallest_items:
    print(item[0])
