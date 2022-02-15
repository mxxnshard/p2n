n = int(input())
surnames = set()
second = set()
sur = 0
count = 0
for i in range(n):
    sur = input()
    if sur in second and sur in surnames:
        count += 1
    if sur in surnames:
        second.add(sur)
    surnames.add(sur)

dif = surnames & second
print(2 * len(dif) + count)
