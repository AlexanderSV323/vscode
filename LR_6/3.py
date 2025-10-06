text = input("Введите произвольный текст: ")
try:
    step = int(input("Введите шаг: "))
except ValueError:
    print("Ошибка: шаг должен быть целым числом")
    exit()
if step <= 0:
    print("Ошибка: шаг должен быть положительным числом")
else:
    result = text[::step]
    print("Текст с заданным шагом:")
    print(result)