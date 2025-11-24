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

def find_owner():
    doc_number = input("Введите номер документа: ")
    for doc in documents:
        if doc['number'] == doc_number:
            print("Результат: ")
            print("Владелец документа: " + doc['name'])
            return
    print("Результат: ")
    print("Документ с таким номером не найден")

while True:
    cm = input("Введите команду(p-найти владельца, q-выйти): ")
    if cm == 'p':
        find_owner()
    elif cm == 'q':
        break
