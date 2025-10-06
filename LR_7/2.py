print("=== РЕГИСТРАЦИЯ ===")
password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")
if password != confirm_password:
    print("Ошибка: пароли не совпадают!")
    exit()
print("Пароль успешно установлен!\n")
print("=== АВТОРИЗАЦИЯ ===")
attempts = 3
while attempts > 0:
    login_password = input(f"Введите пароль для входа (осталось попыток: {attempts}): ")
    
    if login_password == password:
        print("Access")
        break
    else:
        print("Denied")
        attempts -= 1   
if attempts == 0:
    print("Доступ заблокирован!")