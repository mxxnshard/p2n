print('Введите логин: ')
login = input()
print('Ввелите электронный адрес: ')
mail = input()
if '@' not in login and '@' in mail:
    print('OK')
elif '@' in login and '@' in mail:
    print('Некорректный логин')
elif '@' not in mail and '@' not in login:
    print('Некорректный электронный адрес')
else:
    print('Некорректный формат')