fio = input("Введите свое фио через пробел: ")
try:
    surname, name, Ot4estvo = fio.split()
    print(f"Фамилия: {surname.upper()}")
    print(f"Имя: {name.upper()}")
    print(f"Отчество: {Ot4estvo.upper()}")
except ValueError:
    print("Ошибка: введите Фамилию, Имя и Отчество через пробел!")