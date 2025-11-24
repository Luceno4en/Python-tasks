from datetime import datetime

formats = [
    "%A, %B %d, %Y",    # The Moscow Times: Wednesday, October 2, 2002
    "%A, %d.%m.%y",     # The Guardian: Friday, 11.10.13
    "%A, %d %B %Y"      # Daily News: Thursday, 18 August 1977
]

print("Введите дату в одном из форматов (или 'стоп' для завершения):")

while True:
    user_input = input().strip()
    if user_input.lower() == 'стоп':
        break

    parsed = False
    for fmt in formats:
        try:
            date_obj = datetime.strptime(user_input, fmt)
            print(date_obj)
            parsed = True
            break
        except ValueError:
            continue

    if not parsed:
        continue