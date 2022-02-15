a = False
n = int(input())
for i in range(n):
    ph = str(input())
    if 'кот' in ph:
        a = True
        continue
if a is True:
    print('meow')
else:
    print('no')
