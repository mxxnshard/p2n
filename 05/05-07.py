e = True
o = False
n = int(input())
for i in range(n):
    comm = input()
    if comm == 'С кем война?':
        if e:
            print('Евразия')
        elif o:
            print('Октазия')
    if comm == 'С кем мир?':
        if e:
            print('Октазия')
        elif o:
            print('Евразия')
    if comm == 'Меняем':
        e, o = o, e
