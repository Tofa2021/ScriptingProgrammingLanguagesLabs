import json

with open("Firms.txt", "r", encoding="utf-8") as file:
    firm_dict = {parts[0]: int(parts[2]) - int(parts[3]) for parts in (line.split() for line in file)}

average_net_income = (sum(income for income in firm_dict.values() if income > 0) //
                      sum(1 for income in firm_dict.values() if income > 0))
average_income_dict = {"average_net_income": average_net_income}
info_list = [firm_dict, average_income_dict]

with open('Firms.json', 'w', encoding='utf-8') as file:
    json.dump(info_list, file, ensure_ascii=False)
print(info_list)
