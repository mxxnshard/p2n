n = int(input())
message = input()
letters = 'абвгдежзийклмнопрстуфцчшщъыьэюя'
m = 0
for i in range(len(message)):
    if message[m] in letters:
        mm = chr(ord(message[m]) + n)
    else:
        mm = message[m]
    m += 1
    print(mm, end='')
