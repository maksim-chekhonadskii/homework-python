length_a = int(input('Введите длину строки: '))
import random
my_list = []
while len(my_list) != length_a:
    a = random.randint(1,100)
    my_list.append(a)

my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(f'Исходный список {my_list}')

print(f'Новый список {my_new_list[1:]}')
