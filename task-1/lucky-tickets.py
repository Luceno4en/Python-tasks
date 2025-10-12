number = input("Введите номер билета(только 6 цифр): ")

sum1 = int(number [0]) + int(number [1]) + int(number [2])
sum2 = int(number [3]) + int(number [4]) + int(number [5])

if sum1 == sum2:
    print("Счастливый булет")
else:
    print("Несчастливый билет")