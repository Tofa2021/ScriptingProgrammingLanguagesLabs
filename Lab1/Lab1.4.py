my_dict = {'a':12, 'b':13, 'c': 56,'d':400, 'e':58, 'f': 20}

for item in sorted(my_dict.items(), key=lambda x: x[1])[:3]:
    print(item)
