n = int(input())
eng = set()
du = set()
for i in range(n):
    pupileng = input()
    eng.add(pupileng)
m = int(input())
for i in range(m):
    pupildu = input()
    du.add(pupildu)
count = len(du ^ eng)
if count > 0:
    print(count)
else:
    print('No')
