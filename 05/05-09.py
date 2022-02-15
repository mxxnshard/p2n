n = int(input())
cf = False
for i in range(n):
    ph = str(input())
    if 'кот' or 'Кот' in ph:
        cf = True
        continue
    if 'Пес' or 'пес' in ph:
        cf = False

if cf is True:
    print('MEOW')
elif cf is False:
    print('NO')