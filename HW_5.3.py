import string
text = input("Введіть рядок: ")
for symbol in string.punctuation + " ":
    text = text.replace(symbol, " ")
words = text.split()
hashtag = '#' + ''.join(word.capitalize() for word in words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print("Хештег:", hashtag)
