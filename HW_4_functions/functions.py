
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def all_documents(list_documents = documents,dict_directories = directories):   
    for item in list_documents:       
        for shelf, number in dict_directories.items():        
            if item["number"] in number: print(f'№: {item["number"]}, тип: {item["type"]}, владелец: {item["name"]}, полка хранения: {shelf}')

            
# all_documents()

def number_owner(list_documents = documents):
    
    number = input('Введите номер документа: ')
    result = 'Документ не найден в базе'
    for item in list_documents:        
        if item['number'] == number: 
            result = f'Владелец документа: {item["name"]}'     
    print(result)   

# number_owner()

def document_shelf(dict_directories = directories):

    result = 'Документ не найден в базе'
    number_document = input('Введите номер документа: ')    
    for shelf, number in dict_directories.items():        
        if number_document in number:
            result = f'Документ хранится на полке: {shelf}'
    print(result)         
   
# document_shelf()

def new_shelf(dict_directories = directories):
   
    shelf = input("Введите номер полки: ")
    if shelf in dict_directories:
        print(f"Такая полка уже существует. Текущий перечень полок: {(', '.join(dict_directories))}")
    else:
        dict_directories[shelf] = []
        print(f"Полка добавлена. Текущий перечень полок: {(', '.join(dict_directories))}")

#  new_shelf()

def del_shelf(dict_directories = directories):

    shelf = input("Введите номер полки: ")
    if shelf in dict_directories:       
        if dict_directories[shelf] == []:
            del dict_directories[shelf]
            print(f"Полка удалена. Текущий перечень полок: {(', '.join(dict_directories))}")
        else: print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {(', '.join(dict_directories))}")         
    else: print(f"Такой полки не существует. Текущий перечень полок: {(', '.join(dict_directories))}")
    
# del_shelf()

def add_document(list_documents = documents,dict_directories = directories):

    list_documents.append({
        'number': input('Введите номер документа: '),
        'type' :  input('Введите тип документа: '),
        'name' : input('Введите владельца документа: ')})
    shelf = input('Введите полку для хранения: ')
    if shelf in dict_directories:
        dict_directories[shelf].append(list_documents[-1]['number'])
        print('Документ добавлен. ', end="")
    else: print('Такой полки не существует. Добавьте полку командой as. ')
    print('Текущий список документов:')
    all_documents()

# add_document()

def del_document(list_documents = documents,dict_directories = directories):
    number_document = input('Введите номер документа: ')
    result = 'Документ не найден в базе.'
    for shelf in dict_directories.values():
        if number_document in shelf: 
            shelf.remove(number_document)
    for item in list_documents:
        if number_document in item.values():
            list_documents.remove(item)
            result = ('Документ удален.')
    print(result)    
    print('Текущий список документов: ')    
    all_documents()             

# del_document()

def change_shelf(dict_directories = directories):

    number_document = input('Введите номер документа: ')
    number_shelf = input('Введите номер полки: ')
    count_document = 0
    count_shelf = 0
    for document in dict_directories.values():    
        if number_document in document:
            count_document += 1
        if number_shelf in dict_directories.keys():
            count_shelf += 1
        if number_document in document and number_shelf in dict_directories.keys():
            document.remove(number_document)
            dict_directories[number_shelf].append(number_document)
            print (f'Документ перемещен.')
            print('Текущий список документов:')
            all_documents()
            break
    if count_document == 0:
        print('Документ не найден в базе.')  
        print('Текущий список документов:')
        all_documents()
    if count_shelf == 0:  print(f"Такой полки не существует. Текущий перечень полок: {(', '.join(dict_directories))}")
    
# change_shelf()

def help_main():
    print (f"""
    "p" - пользователь может узнать владельца документа по его номеру.
    "s" - пользователь может по номеру документа узнать на какой полке он хранится.
    "l" - пользователь может увидеть полную информацию по всем документам.
    "ads" - пользователь может добавить новую полку.
    "ds" - пользователь может удалить существующую полку из данных (только если она пустая).
    "ad" - пользователь может добавить новый документ в данные.
    "d" - пользователь может удалить документ из данных.
    "m" - пользователь  может переместить документ с полки на полку.
    "h" - помощь.
    "q" - выход.    
    """)

def command_error():
  print('Ошибка ввода данных')

def main():
    
    dict_command = {
        "p" : number_owner,
        "s" : document_shelf,
        "l" : all_documents,
        "ads" : new_shelf,
        "ds" : del_shelf,
        "ad" : add_document,
        "d" : del_document,
        "m" : change_shelf,        
        "h" : help_main
    }
    while True: 
        command = input("Введите команду запроса или 'h' для справки: ").lower()
        if command == "q": break
        dict_command.get(command, command_error)()
    
main()