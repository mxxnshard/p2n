sec = int(input())
if sec > 0:
    for i in range(sec+1):
        print('Осталось секунд:', sec)
        sec -= 1
    print('Пуск!')
else:
    print('Пуск!')
