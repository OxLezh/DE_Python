

import requests
from pprint import pprint

class Rate:
    def __init__(self, format='value', diff = True):
        self.format = format
        self.diff = diff
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        
        return r.json()['Valute']     
    
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value' and self.diff == "True":
                return response[currency]['Value'] -  response[currency]['Previous']
            
            if self.format == 'value' and self.diff == "False":
                return response[currency]['Value']                 
        
        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def AZN(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format"""
        return self.make_format('AZN')

    def max_name(self):
        """
            Функция, которая возвращает название валюты (поле ‘Name’) с максимальным значением
            курса с помощью сервиса www.cbr-xml-daily.ru...ly_json.js
        """
        dict_my = {}
        for value in self.exchange_rates().values():
            dict_my[value['Name']] = value['Value']        
        max_result = max(dict_my, key=dict_my.get)
        return max_result

r = Rate()
print(r.max_name())

# параметр diff (значения True или False) в случае значения True в методах курсов валют
#  (eur, usd итд) будет возвращать не курс валюты, а изменение по сравнению в прошлым значением.

b = Rate(format ='value', diff = "True")
print(b.eur())


#  Задание 3
#  Напишите класс Designer, который учитывает количество международных премий. Подсказки в коде занятия в разделе “Домашнее задание задача 3”.
#  Комментарий по классу Designer такой:
#  Напишите класс Designer, который учитывает количество международных премий для дизайнеров (из презентации: “Повышение на 1 грейд за каждые 7 баллов.
#  Получение международной премии – это +2 балла”). Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем 
# (конечно если хотите это можно вручную менять).

#  Класс Designer пишется по аналогии с классом Developer из материалов занятия.

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)
    
    def check_if_it_is_time_for_upgrade(self):
        pass


class Designer(Employee):

    def __init__(self, name, seniority, premium = 2) :
        super().__init__(name, seniority)
        self.premium = premium
        self.seniority = seniority + premium *2

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все дизайнеры проходят аккредитацию
        self.seniority += 1
        # условие повышения сотрудника из презентации
        if self.seniority % 7 == 0:
            self.grade_up()
        # публикация результатов
        return self.publish_grade()



# разработчик Александр только что пришел в компанию
alex = Designer('Александр', 0)

for i in range(20):
    alex.check_if_it_is_time_for_upgrade()