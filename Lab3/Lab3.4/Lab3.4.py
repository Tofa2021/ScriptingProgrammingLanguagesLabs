import json

with open("Firms.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

firm_net_income_dict = {}
for line in lines:
    split_line = line.split()
    firm_name = split_line[0]
    employment_firm_form = split_line[1]
    income = int(split_line[2])
    cost = int(split_line[3])
    net_income =  income - cost
    firm_net_income_dict[firm_name] = net_income

all_net_income = 0
for firm_name, net_income in firm_net_income_dict.items():
    if net_income > 0:
        all_net_income += net_income
average_net_income = all_net_income / len(firm_net_income_dict.keys()) # Нужно ли тут включать фирмы с убытками???
average_net_income_dict = {"average_net_income": average_net_income}

info_list = [firm_net_income_dict, average_net_income_dict]
with open('Firms.json', 'w', encoding='utf-8') as file:
    json.dump(info_list, file, ensure_ascii=False)
print(info_list)
