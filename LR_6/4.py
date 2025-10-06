text = input("Введите произвольный текст: ")
try:
    start, end = map(int, input("Введите диапазон (начало конец через пробел): ").split())
    if start < 0 or end < 0:
        print("Ошибка: индексы не могут быть отрицательными")
    elif start >= len(text) or end >= len(text):
        print(f"Ошибка: максимальный индекс должен быть {len(text)-1}")
    elif start > end:
        print("Ошибка: начальный индекс не может быть больше конечного")
    else:
        result = text[start:end+1]
        print("Подстрока:")
        print(result)
except ValueError:
    print("Ошибка: введите два целых числа через пробел")
except Exception as e:
    print(f"Произошла ошибка: {e}")