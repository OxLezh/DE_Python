import json
import csv



#  Переведите содержимое файла purchase_log.txt в словарь purchases вида:
#  {‘1840e0b9d4’: ‘Продукты’, …}

def purchases():
    purchases ={}
    with open('purchase_log.txt', "r",  encoding="utf-8") as f:
        for line in f:       
            line = json.loads(line)
            purchases[line['user_id']] = line['category']
    return purchases

        
# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки
#  (если покупка была, сам файл visit_log.csv изменять не надо). Запишите в файл funnel.csv визиты
#  из файла visit_log.csv, в которых были покупки с указанием категории.
# Учтите условия на данные:
# содержимое purchase_log.txt помещается в оперативную память компьютера
# содержимое visit_log.csv - нет; используйте только построчную обработку этого файла

# первый вариант
def visit_log():

    with open('visit_log.csv', "r",  encoding="utf-8") as f: 
        with open('funnel.csv', "w",  encoding="utf-8",  newline='') as f2: 
            dict_purche = purchases()
            for i in rows:                    
                if i[0] in dict_purche:  
                    i.append(dict_purche[i[0]])                    
                    datawriter.writerow(i)
                    
# второй вариант                    
def visit_log():

    with open('visit_log.csv', "r",  encoding="utf-8") as f: 
        with open('funnel.csv', "w",  encoding="utf-8",  newline='') as f2: 
            dict_purche = purchases()
            for item in f:
                user_id = item.split(",")[0]
                if user_id in  dict_purche:                
                    join_word = f'{item.strip()},{dict_purche[user_id]}\n'
                    f2.write( join_word)                    
                         
visit_log()

   
