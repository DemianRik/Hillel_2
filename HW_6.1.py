import string

latter_a_c = input("Введіть діапазон через дефіс (наприклад a-c): ")
start, end = latter_a_c.split("-")
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)
result = letters[start_index:end_index + 1]
print(result)
