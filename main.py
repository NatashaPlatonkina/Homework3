# 1 задание
with open('text.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingridient_count = int(f.readline())
        ingridients = []
        for i in range(ingridient_count):
            ing = f.readline().strip()
            ingridient_name, quantity, measure = ing.split(' | ')
            ingridients.append({
                'ingridient_name': ingridient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = ingridients
print(cook_book)
print()
print()


# 2 задание
def get_list_shop_by_dishes(dishes, person_count):
    dishes_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                dishes_dict[ingridient['ingridient_name']] = {'quantity': ingridient['quantity'] * person_count,
                                                              'measure': ingridient['measure']}
    return dishes_dict


print(get_list_shop_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2))

print()
print()

full_text = {}
sum_str = {}
with open('text2.txt', 'r', encoding='utf-8') as f:
    name = 'text2.txt'
    sum_ = 0
    str_list = []
    for line in f:
        sum_ += 1
        str_list.append(line)
        full_text[name] = str_list
    sum_str.setdefault(name, sum_)

with open('text3.txt', 'r', encoding='utf-8') as f:
    name = 'text3.txt'
    sum_ = 0
    str_list = []
    for line in f:
        sum_ += 1
        str_list.append(line)
        full_text[name] = str_list
    sum_str.setdefault(name, sum_)

with open('text4.txt', 'r', encoding='utf-8') as f:
    name = 'text4.txt'
    sum_ = 0
    str_list = []
    for line in f:
        sum_ += 1
        str_list.append(line)
        full_text[name] = str_list
    sum_str.setdefault(name, sum_)

sorted_dict = {}
sorted_keys = sorted(sum_str, key=sum_str.get)
for i in sorted_keys:
    sorted_dict[i] = sum_str[i]
print(sorted_dict)

with open('new.txt', 'w', encoding='utf-8') as f:
    for k, v in sorted_dict.items():
        f.writelines(k)
        f.writelines('\n')
        f.writelines(str(v))
        f.writelines('\n')
        key = full_text[k]
        f.writelines(key)
        f.writelines('\n')