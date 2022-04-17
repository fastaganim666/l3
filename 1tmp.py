documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def document(documents, directories):
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        if command == 'p':
            number = input("Введите номер документа: ")
            found = False
            for docs in documents:
                if number == docs['number']:
                    print(docs['name'])
                    found = True
            if found == False:
                print('Не нашел(((')
        
        
        if command == 's':
            number = input("Введите номер документа: ")
            found = False
            for shelves in directories:
                if found == True:
                        break
                for doc_number in directories[shelves]:
                    if number == doc_number:
                        print(f'Номер полки: {shelves}')
                        found = True
                        break
            if found == False:
                print('Не нашел(((')
                
        if command == 'l':
            for docs in documents:
                for docs_ in docs:
                    print(f'{docs[docs_]}', end = ' ')
                print()
                
        if command  == 'a':
            doc_number = input('Введите номер документа: ')
            doc_type = input('Введите тип документа: ')
            name = input('Введите имя владельца: ')
            shelf_num = input('Введите номер полки: ')
            correct = False
            for shelf in directories:
                if shelf_num == shelf:
                    directories[shelf].append(shelf_num)
                    documents.append({"type": doc_type, "number": doc_number, "name": name})
                    correct = True
                    break
            if correct == False:
                print('Данной полки не сущесвует(((')
        if command == 'd':
            found = False
            doc_number = input('Введите номер документа: ')
            for doc in documents:
                if doc['number'] == doc_number:
                    documents.remove(doc)
                    found = True
            for shelf in directories:
                for numbers in directories[shelf]:
                    if numbers == doc_number:
                        directories[shelf].remove(doc_number)
                        found = True
            if found == False:
                print('Документ не найден')
        
        if command == 'm':
            doc_number = input('Введите номер документа: ')
            shelf_number = input ('На какую полку перемесить: ')
            shelf_found = False
            doc_found = False
            for shelf in directories:
                if shelf_number == shelf:
                    shelf_found = True
                    break
            if shelf_found == True:
                for shelf in directories:
                    if doc_number in  directories[shelf]:
                        directories[shelf].remove(doc_number)
                        directories[shelf_number].append(doc_number)
                        doc_found = True
                        break
            if doc_found == False or shelf_found == False:
                print('Документ или полка не найдены')
                
        if command == 'as':
                shelf_number = input ('Введите номер полки: ')
                shelf_exists = False
                for shelves in directories:
                    if shelf_number == shelves:
                        shelf_exists = True
                        break
                if shelf_exists == False:
                    directories.update({shelf_number: []})
                if shelf_exists:
                    print('Такая полка уже существует')

document(documents, directories)
print(documents)
print(directories)