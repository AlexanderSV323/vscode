text = input("Введите произвольный текст: ")
search_word = input("Введите слово для поиска: ")
words = text.split()
exact_matches = 0
for w in words:
    clean_word = w.strip('.,!?;:()\"\'')
    if clean_word == search_word:
        exact_matches += 1
if exact_matches > 0:
    print(f"Слово '{search_word}' найдено в тексте")
    print(f"Количество точных вхождений: {exact_matches}")
else:
    print(f"Слово '{search_word}' не найдено в тексте")
substring_count = text.count(search_word)
if substring_count > exact_matches:
    print(f"Как подстрока встречается: {substring_count} раз")