
import random, os

os.system('clear')

# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все 
# монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

print('Задача 1')
coins = []
for i in range(10):
    coins.append(random.randint(0,1))

print('Список монеток. Где 1 – орел, 0 – решка\n', coins)

eagles = 0
tails = 0
for coin in coins:
    if coin == 0:
        tails += 1
    else:
        eagles += 1    

if eagles >= tails:
    print(f'Вам нужно перевернуть {tails} монеток на орла')
else:
    print(f'Вам нужно перевернуть {eagles} монеток на решку')


# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

x = random.randint(1,1000)
y = random.randint(1,1000)

s = x+y
p = x*y

print('Задача 2. \nЧисла: \nS = ', s, '\nP = ', p)

for a in range(1000):
    for b in range(1000):
        if a+b == s and a*b == p:
            print(f'Загаданные числа: x = {a} и y = {b}')

#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
print('Задача 3.')
n = 1000
while 2 ** i <= n:
    print(2 ** i)
    i += 1