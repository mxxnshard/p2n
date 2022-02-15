cf = False
n = 1
ph = 0
count = 1
c2 = 0
while ph != 'stop':
    ph = input()
    for i in range(n):
        if 'cat' in ph:
            c2 += 1
            cf = True
        if cf is False:
            count += 1
if cf is True:
    print(c2, count, sep=' ')
else:
    print(0, -1)
