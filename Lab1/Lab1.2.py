vowels = "аеёуоыяию"
consonants = "йцкнгшщзхъфвпрлджчсмтьб"

text = str(input("Введите текст\n"))
words = text.split()
vowelCount = 0
consonantCount = 0
vowelString = ""
for word in words:
    for letter in word:
        if letter in vowels:
            vowelCount += 1
            vowelString += letter
        elif letter in consonants:
            consonantCount += 1
print(f"Количество слов: {len(words)}")
print(f"Количество гласных: {vowelCount}")
print(f"Количество согласных: {consonantCount}")
if vowelCount == consonantCount:
    print(f"Гласные буквы в текст: {vowelString}")
