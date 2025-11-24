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

def find_shelf():
    doc_number = input("Введите номер документа: ")
    for shelf, docs in directories.items():
        if doc_number in docs:
            print("Документ хранится на полке: " + shelf)
            return
    print("Документ с таким номером не найден")

while True:
    cm = input("Введите команду(s-узнать полку хранения, q-выйти): ")
    if cm == 's':
        find_shelf()
    elif cm == 'q':
        break