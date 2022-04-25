#Задание 1
'''
def find_prime():
    num = 0
    while num < 16:
        if not num % 2 == 0:
            yield num
            num += 1
        else:
            num += 1

    print('...StopIteration...')

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

a_pipeline = find_odd_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)
'''
#Задание 2
'''
list = []
i = 1
for i in range(16):
    if i % 2 != 0:
        list.append(i)
        print(i)
    i += 1
print('...StopIteration...')
'''
#Задание 3
'''
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(klasses) > len(tutors):
    list1 = list(zip(tutors, klasses))
    print(list1)
'''
#Задание 4
'''
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
i = 1
while i < len(src):
    if src[i] > src[i-1]:
        print(src[i])
    i += 1
'''
#Задание 5
'''
from datetime import datetime
import time

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start_time = datetime.now()
for i in src:
    if src.count(i) == 1:
        print(str(i) + ' ')

time.sleep(1) # Время измерить не удалось, поэтому замедлил код, для получения числа больше 0
speed = datetime.now() - start_time
print(speed)
'''