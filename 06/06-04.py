n = int(input())
m = int(input())
lang = set()
count = 0
for i in range(n + m):
    newpupil = input()
    if newpupil in lang:
        count += 1
    else:
        lang.add(newpupil)
if count > 0:
    print(count)
else:
    print('No')
