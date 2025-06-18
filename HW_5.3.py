text_1 = input("Введи текст: ")

hashtag = '#' + ''.join(text_1.capitalize() for text_1 in text_1.split())

print("Хештег:", hashtag)
