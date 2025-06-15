list_1 = [0, 1, 7, 2, 4, 8]
par_list = list_1[::2]
sum_list = sum(par_list)
element = list_1[-1]

print("Сума парних елементів: ", sum_list)
print("Множимо на: ", element)
print("Результат: ", sum_list * element)
