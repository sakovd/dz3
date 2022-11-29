quantity_first=""
while not quantity_first.isdigit():
    quantity_first = input("Введите количество элементов первого списка: ")

numbers_first =[]
for i in range(1, int(quantity_first) + 1):
    number = input(f'Введите {i} значение: ')

    while not number.isdigit():
        number = input(f'Введите целое число для значения {i}: ')

    numbers_first.append(int(number))

quantity_second=""
while not quantity_second.isdigit():
    quantity_second = input("Введите количество элементов второго списка: ")

numbers_second =[]
for i in range(1, int(quantity_second) + 1):
    number = input(f'Введите {i} значение: ')

    while not number.isdigit():
        number = input(f'Введите целое число для значения {i}: ')

    numbers_second.append(int(number))

result_list=[]
for number in numbers_first:
    if number not in numbers_second:
        result_list.append(number)

print('Первый список: ', numbers_first)
print('Второй список: ', numbers_second)
print('Результат: ', result_list )