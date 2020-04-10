#пункт 1
import itertools

for i in itertools.repeat(1, 4):
    print(i)

#пункт 2
cycle_end = [1, 2, 3]
length_a =[]
for i in itertools.cycle(cycle_end):
    print(i)
    length_a.append(i)
    if int(len(length_a)) > 10:
        break
print('Количество значений достигло максимума')
