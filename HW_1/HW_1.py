# Задание 1
# Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
# Напишите код, который проверяет какая из этих строк длиннее.

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640 должно хватить для любых задач. Билл Гейтс (по легенде)333'
if len(phrase_1) > len(phrase_2):
    print('phrase_1 длиннее phrase_2')
elif len(phrase_1) < len(phrase_2):
    print('phrase_2 длиннее phrase_1')
else:
    print('Фразы равной длины')

# Задание 2
# Дана переменная, в которой хранится четырехзначное число (год). 
# Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.


year = 2019

if year % 4 == 0:
    if year % 100 != 0:
        print('Високосный год')
    elif year % 100 == 0:
        if year % 400 == 0:
            print('Високосный год')
        else:
            print('Обычный год ')
else:
    print('Обычный год ')


# Задание 3
# Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.

month = (input('Введите месяц рождения: ')).lower()
birth_date = int(input('Введите число рождения: '))
if (month == 'март' and 21 <= birth_date <= 31) or (month == 'апрель' and 1 <= birth_date <= 20):
    print('Овен')
elif (month == 'апрель' and 21 <= birth_date <= 30) or (month == 'май' and 1 <= birth_date <= 20):
    print('Телец')  
elif (month == 'май' and 21 <= birth_date <= 31) or (month == 'июнь' and 1 <= birth_date <= 21):
    print('Близнецы')
elif (month == 'июнь' and 22 <= birth_date <= 30) or (month == 'июль' and 1 <= birth_date <= 22):
    print('Рак')
elif (month == 'июль' and 23 <= birth_date <= 31) or (month == 'август' and 1 <= birth_date <= 23):
    print('Лев')
elif (month == 'август' and 24 <= birth_date <= 31) or (month == 'сентябрь' and 1 <= birth_date <= 23):
    print('Дева')
elif (month == 'сентябрь' and 24 <= birth_date <= 30) or (month == 'октябрь' and 1 <= birth_date <= 23):
    print('Весы')
elif (month == 'октябрь' and 24 <= birth_date <= 31) or (month == 'ноябрь' and 1 <= birth_date <= 22):
    print('Скорпион')
elif (month == 'ноябрь' and 23 <= birth_date <= 30) or (month == 'декабрь' and 1 <= birth_date <= 21):
    print('Стрелец')
elif (month == 'декабрь' and 22 <= birth_date <= 31) or (month == 'январь' and 1 <= birth_date <= 20):
    print('Козерог')
elif (month == 'январь' and 21 <= birth_date <= 31) or (month == 'февраль' and 1 <= birth_date <= 20):
    print('Водолей')
elif (month == 'февраль' and 21 <= birth_date <= 29) or (month == 'март' and 1 <= birth_date <= 20):
    print('Рыбы')
else:
     print('В календаре нет такой даты')


# Задание 4
# Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):
# Используйте следующие правила:
# если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран “Коробка №1”;
# если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите “Коробка №2”;
# если длина товара больше 2 метров, то выводите “Упаковка для лыж”;
# во всех остальных случаях выводите “Стандартная коробка №3”.

width = 60
length = 205
height = 60

if width <= 15 and length <= 15 and height <= 15:
    print('Коробка №1')
elif length > 200:
    print('Упаковка для лыж')
elif length < 200:
    if 15 < width < 50 or 15 < length < 50 or 15 < height < 50:
        print('Коробка №2')
    else:
        print('Стандартная коробка №3')
else:
    print('Стандартная коробка №3')