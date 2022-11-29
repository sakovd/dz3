quantity=""
while not quantity.isdigit():
    quantity = input("Введите количество элементов списка: ")

numbers =[]
for i in range(1, int(quantity) + 1):
    number = input(f'Введите {i} значение: ')

    while not number.isdigit():
        number = input(f'Введите целое число для значения {i}: ')

    numbers.append(int(number))

numbers.sort()
print(f'Итоговый список: {numbers}')