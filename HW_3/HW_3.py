# # from pprint import pprint
# # # Задание 1
# # # Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных приведен ниже). Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

# # ids = {'user1': [213, 213, 213, 15, 213],
# # 'user2': [54, 54, 119, 119, 119],
# # 'user3': [213, 98, 98, 35]}

# # new_set = set()  
# # item = [new_set.update(i) for i in ids.values()]
# # print(new_set)

# # # print(set(sum(ids.values(), [])))

# # # Задание 2
# # # Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже).
# # #  Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

# # queries = [
# # 'смотреть сериалы онлайн',
# # 'новости спорта',
# # 'афиша кино',
# # 'курс доллара',
# # 'сериалы этим летом',
# # 'курс по питону',
# # 'сериалы про спорт'
# # ]

# # word_count = {}
# # for item in  queries:
# #   count = len(item.split())
# #   word_count[count] = word_count.get(count, 0) + 1
# # for item in word_count:
# #   print(f' Поисковых запросов, содержащих {item} слов(а): {round(word_count[item]*100/sum(word_count.values()),2)}%')

# # # for i in set([len(i.split()) for i in queries]):
# # #     print(f'Поисковых запросов, содержащих {i} слов(а): {len([s for s in queries if len(s.split()) == i ]) / len(queries) :.2%}')

# # #   Задание 3
# # # Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. 
# # # Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100

# # results = {
# # 'vk': {'revenue': 103, 'cost': 98},
# # 'yandex': {'revenue': 179, 'cost': 153},
# # 'facebook': {'revenue': 103, 'cost': 110},
# # 'adwords': {'revenue': 35, 'cost': 34},
# # 'twitter': {'revenue': 11, 'cost': 24},
# # }

# # for item in results.values(): 
# #   item['ROI'] = round((item['revenue'] / item['cost'] - 1) * 100, 2)
# # pprint(results)

# # # Задание 4
# # # Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже).
# # #  Напишите программу, которая возвращает название канала с максимальным объемом продаж.
# # # Результат: Максимальный объем продаж на рекламном канале: vk

# # stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

# # keys, value  = list(stats.keys()), list(stats.values())
# # print(f' Максимальный объем продаж на рекламном канале: {keys[value.index(max(value))]}')



# # # Задание 5 (необязательно)
# # # Дан список произвольной длины. Необходимо написать код, который на основе исходного списка составит словарь такого уровня вложенности, 
# # # какова длина исхондого списка.

# # my_list = ['2018-01-01', 'yandex', 'cpc', 100]
# # # my_list = ['a', 'b', 'c', 'd', 'e', 'f']

# # dict = {my_list[-2]:my_list[-1]}
# # for i in range(len(my_list)-2, 0, -1):
# #   dict = {my_list[i-1]:dict}
# # print(dict)

# # # Задание 6 (необязательно)
# # # Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию (пример данных представлен ниже).
# # # Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и отображать информацию о суммарном количестве требуемых ингредиентов в указанном виде.
# # # Внимание! Одинаковые ингридиенты с разными размерностями нужно считать раздельно!
# # # Пример работы программы:

# cook_book = {
# 'салат': [
# {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
# {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
# {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
# {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
# {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
# {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
# {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
# ],
# 'пицца': [
# {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
# {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
# {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
# {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
# {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
# {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
# ],
# 'лимонад': [
# {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
# {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
# {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
# {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
# ]
# }

# # # наверное, можно сделать как-то проще.

# # count = int(input("Укажите количество порций: "))
# # my_dict = {}
# # for k in cook_book.values():  
# #   for i in k: 
# #     key = (i['ingridient_name'], i['measure'])
# #     value = i['quantity']
# #     if key not in my_dict:
# #       my_dict[key] = value * count    
# #     else:     
# #       my_dict[key] = value * count + my_dict[key]

# # for i in my_dict.items():
# #   print(f'{i[0][0].capitalize()}: {i[1]} {i[0][1]}.')  

 
# numb_servings = int(input('Укажите количество порций: '))
# quantity_book = {}

# for ingred_book in sum(cook_book.values(), []):
#   print(ingred_book)
#   ingred_key = (ingred_book['ingridient_name'], ingred_book['measure'])
#   print(ingred_key)
#   quantity_book[ingred_key] = quantity_book.get(ingred_key, 0) + ingred_book['quantity']
#   print(quantity_book)

# for (ingred_name, measure), quantity in quantity_book.items():
#   print(f'{ingred_name.capitalize()}: {quantity * numb_servings} {measure}')
