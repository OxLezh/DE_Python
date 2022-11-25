from datetime import datetime
from datetime import timedelta

# Задание 1
# Печатные газеты использовали свой формат дат для каждого выпуска. 
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
dict_date = {'The Moscow Times' : 'Wednesday, October 2, 2002', 'The Guardian' : 'Friday, 11.10.13', 'Daily News' : 'Thursday, 18 August 1977'}


def str_datetime():

    for i in dict_date:       
        if i == 'The Moscow Times':
            data = datetime.strptime(dict_date[i], '%A, %B %d, %Y')
            print(data)
        elif i == 'The Guardian':
            data = datetime.strptime(dict_date[i], '%A, %d.%m.%y')
            print(data)
        elif i == 'Daily News':
            data = datetime.strptime(dict_date[i], '%A, %d %B %Y')
            print(data)


# str_datetime()

# Задание 2
# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
stream = ['2018-12-02', '2018-02-29', '2018-19-02']

# Напишите функцию, которая проверяет эти даты на корректность. Т. е. 
# для каждой даты возвращает True (дата корректна) или False (некорректная дата).


def date_correctness():
 
    format_date = '%Y-%m-%d'
    for item in stream:
        try:              
            res = bool(datetime.strptime(item, format_date))            
        except:        
            res = False      
        print(res)

date_correctness()

# Задание 3
# Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date.
# Даты должны вводиться в формате YYYY-MM-DD. 
# В случае неверного формата или при start_date > end_date должен возвращаться пустой список.


def date_range():

    format_date = '%Y-%m-%d'
    try: 
        start_date = datetime.strptime((input("Введите дату начала: ").strip()), format_date)
                 
        end_date = datetime.strptime((input("Введите дату окончания: ").strip()), format_date)
        range_days = int((end_date - start_date).days)       
    
        date_range = [(start_date + timedelta(days=x)).strftime(format_date) for x in range(range_days+1)]
        print(date_range)
    except:
        print([])
   
# date_range()

