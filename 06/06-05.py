n = int(input())
m = int(input())
k = int(input())
lang = set()
lang2 = set()
count = 0
for i in range(n + m + k):
    pupil = input()
    if pupil in lang:
        count += 1
        lang2.add(pupil)
    lang.add(pupil)
if (n == k == m) and len(lang) == n:
    print('NO')
else:
    if len(lang2) + count > 0:
        if (len(lang2) + count) % 2 != 0:
            print((len(lang2) + count) % 2)
        else:
            print((len(lang2) + count) // 2)
    else:
        print('NO')
