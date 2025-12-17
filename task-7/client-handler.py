def main():
    with open('web_clients_correct.csv', 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    with open('descriptions_clients.txt', 'w', encoding='utf-8') as f_out:
        for line in lines[1:]:
            parts = line.strip().split(',')

            name = parts[0]
            sex = parts[3]
            age = parts[4]
            device = parts[1]
            browser = parts[2]
            bill = parts[5]
            region = parts[6]

            if sex == 'female':
                gender_word = 'женского'
                verb = 'совершила'
            else:
                gender_word = 'мужского'
                verb = 'совершил'

            if device == 'mobile':
                device_word = 'мобильного'
            elif device == 'desktop':
                device_word = 'компьютерного'
            elif device == 'laptop':
                device_word = 'ноутбука'
            elif device == 'tablet':
                device_word = 'планшетного'
            else:
                device_word = device

            description = f"Пользователь {name} {gender_word} пола, {age} лет {verb} покупку на {bill} y.e. с {device_word} браузера {browser}. Регион, из которого совершалась покупка: {region}.\n"

            f_out.write(description)

#Запускаю программу
if __name__ == '__main__':
    main()