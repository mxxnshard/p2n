n = int(input())
towns = set()
for i in range(n):
    sometown = input()
    towns.add(sometown)
newtown = input()
if newtown in towns:
    print('Try another')
else:
    print('OK')
