a = int(input())
b = int(input())
n = b - a
for i in range(n+1):
    if a % 3 == 0 and a % 5 == 0:
        print('fizzbuzz')
    elif a % 3 == 0:
        print('fizz')
    elif a % 5 == 0:
        print('buzz')
    else:
        print(a)
    a += 1
