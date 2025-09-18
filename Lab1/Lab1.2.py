vowels = "аеёуоыяию"
consonants = "йцкнгшщзхъфвпрлджчсмтьб"

text = str(input("Введите текст\n"))
vowelCount = sum(1 for ch in text if ch.lower() in vowels)
consonantCount = sum(1 for ch in text if ch.lower() in consonants)
vowels_list = [ch for ch in text if ch.lower() in vowels]

print(f"Количество слов: {len(text.split())}")
print(f"Количество гласных: {vowelCount}")
print(f"Количество согласных: {consonantCount}")
if vowelCount == consonantCount:
    print(f"Гласные буквы в текст: {vowels_list}")
