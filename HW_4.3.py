import random
list_1 = random.randint(3, 10)
list_random = [random.randint(1, 100) for _ in range(list_1)]

print(list_random)