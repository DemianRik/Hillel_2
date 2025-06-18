while True:
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))
    c = input("Що робимо? (+, -, *, /) ")

    if c == '+':
        print("Результат:", a + b)
    elif c == '-':
        print("Результат:", a - b)
    elif c == '*':
        print("Результат:", a * b)
    elif c == '/':
        if b == 0:
            print("Помилка: ділення на нуль!")
        else:
            print("Результат:", a / b)
    else:
        print("Невідома операція!")

    work_next = input("Бажаєте зробити ще одне обчислення?"
                      " (y/yes щоб продовжити): ").lower()
    if work_next not in ('y', 'yes'):
        print("Дякую за користування калькулятором!")
        break
