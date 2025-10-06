fio_input = input("Введите ваше ФИО через пробел: ")
formatted_fio = " ".join(part.capitalize() for part in fio_input.split())
if len(formatted_fio.split()) == 3:
    print(f"Добро пожаловать {formatted_fio}")
else:
    print("Ошибка: пожалуйста, введите Фамилию, Имя и Отчество через пробел")
