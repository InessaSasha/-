# Задача "Однокоренные":
def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        #делаем нижний регистр для всех слов
        root_word = root_word.lower()
        word = word.lower()
        #сравниваем слова из списка с параметром и наоборот
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words


result = single_root_words('сор', 'Сорбент', 'сор', 'сорока', 'Дверь')
print(result)