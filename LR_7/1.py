direction = input("Введите направление (left, right, straight, back): ").strip().lower()
directions = {
    "straight": "Иду прямо",
    "left": "Иду влево", 
    "right": "Иду вправо",
    "back": "Иду назад"
}
if direction in directions:
    print(directions[direction])
else:
    print("Неправильное направление")