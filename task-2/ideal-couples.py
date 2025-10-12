boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары.')
else:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    #Функция sorted возвращает новый список, в котором имена отсортированы в алфавитном порядке
    print('Идеальные пары:')
    for boys, girls in zip(boys_sorted, girls_sorted):
        print(f'{boys} и {girls}')