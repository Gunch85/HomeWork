# import random
#
# a = random.randint(100, 999)
# print('Случайное число =', a)
# print(a // 100 + a // 10 % 10 + a % 10)

import random
num = random.randint(100, 999)
print(num)
a = num // 100
b = (num // 10) % 10
c = num % 10
print(a + b + c)
