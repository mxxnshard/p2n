cf = False
n = 1
ph = 0
count = 1
while ph != 'stop':

    for i in range(n):
        ph = input()
        if 'cat' in ph:
            cf = True
            break
        if cf is False:
            count += 1
if cf is True:
    print(count)
else:
    print(-1)
