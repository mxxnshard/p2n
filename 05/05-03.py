cf = False
n = 1
ph = 0
count = 1
while ph != 'stop':
    ph = input()
    for i in range(n):
        if 'cat' in ph:
            cf = True
        if cf is False:
            count += 1
if cf is True:
    print(count)
else:
    print(-1)

