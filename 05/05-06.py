sum = 0
c = False
count = 0
n = 1
a = -1
while a != 0:
    a = int(input())
    for i in range(n):
        sum += a
        if c is False:
            count += 1
        if sum == 10:
            c = True
print(count)



