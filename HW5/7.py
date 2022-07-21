a = input('Введите семизначное число: ')


chet = 0
nechet = 0

for i in a:
    if int(i) % 2 == 0:
        chet += 1
    else:
        nechet += 1
print('Введеное число: ', a)
print('Чётных чисел: ', chet, 'Нечётных чисел: ', nechet)

sum = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) + int(a[4]) + int(a[5]) + int(a[6])
pr = int(a[0]) * int(a[2]) * int(a[5])


if chet > nechet:
    print('Cумма: ', sum)
elif chet < nechet:
    print('Произведение: ', pr)