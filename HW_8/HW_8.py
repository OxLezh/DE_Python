import re
# Задание 1
# Напишите функцию, которая принимает на вход строку и проверяет, является ли она валидным транспортным номером 
# (1 буква, 3 цифры, 2 буквы, 2–3 цифры). Обратите внимание, что не все буквы кириллического алфавита используются в транспортных номерах.
# Если номер валиден, то функция должна возвращать отдельно номер и регион.
# Примеры работы программы:
car_id = 'A222BC96'
# Результат: Номер A222BС валиден. Регион: 96
# car_id = 'АБ22ВВ193'
# Результат: Номер не валиден

def reg_car_number(car_id):
    
    try:
        rezult = re.findall(r'[a-zA-Z]{1}\d{3}[a-zA-Z]{2}\d{2,3}', car_id)
        if car_id == rezult[0]:
            print(f'Номер {car_id[0:6]} валиден. Регион: {car_id[6:]}')
    except:
        print(f'Номер не валиден')

# reg_car_number(car_id)

# --------------------------------------------------
# Задание 2
# Напишите функцию, которая будет удалять все последовательные повторы слов из заданной строки при помощи регулярных выражений.
# Пример работы программы:
some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений.'
# Результат:
# Напишите функцию, которая будет удалять все последовательные повторы слов из заданной строки при помощи регулярных выражений.


def reg_duplicate(some_string):

    rezult = re.sub(r'([а-яёА-ЯЁ]+)(\s\1)+',r'\1', some_string)        
    print(rezult)    

# reg_duplicate(some_string)


# --------------------------------------------------
# Задание 3
# Напишите функцию, которая будет возвращать акроним по переданной в неё строке со словами.
# Примеры работы программы:
# some_words = 'Информационные технологии'
# Результат: ИТ
some_words = 'Near Field Communication'
# Результат: NFC

def reg_acronym(some_words):

    rezult = "".join(re.findall(r'\b[a-zA-Z]|\b[а-яёА-ЯЁ]', some_words)).upper()
        
    print(rezult)  
    
#   второе решение     return re.sub(r"(\w)\w+\s?", r"\1", word).upper()

# reg_acronym(some_words)


# --------------------------------------------------
# Задание 4
# Напишите функцию, которая будет принимать на вход список email-адресов и выводить их распределение по доменным зонам.

# Пример работы программы:

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']

# Результат:

# gmail.com: 2
# test.in: 1
# ya.ru: 2
# mail.ru: 1


def reg_count_domen(emails):

    my_dict =  {}
    for email in emails:
        domen = re.search(r'@(\w+\.\w+)', email).group(1)
        my_dict[domen] = (my_dict.get(domen, 0) + 1)       
    for key, value in my_dict.items():
        print(f'{key}: {value}')

# reg_count_domen(emails)


# второй вариант:
# listdomain = re.findall(r'(?<=@)\w+.\w{2,3}', ' '.join(listmail))
# for mail in set(listdomain):
# print(f'{mail}: {listdomain.count(mail)}')

# mail_domain(emails)
