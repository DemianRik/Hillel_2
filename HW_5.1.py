import string
import keyword
name = input("Введіть можливе ім'я змінної: ")

result = (name.isidentifier() and
    name not in keyword.kwlist and
    not any(char in string.punctuation.replace("_", "") for char in name) and
    name == name.lower() and
    not name[0].isdigit())

print(result)
