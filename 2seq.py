sequence_numbers = input('Введите последовательность цифр через ",",";" или "/": ').replace(';', ' ').replace(',', ' ').replace('/', ' ').split()

unique_sequence_numbers = set(sequence_numbers)

print('Исходный список: ', sequence_numbers)
print('Уникальный список: ', list(unique_sequence_numbers))