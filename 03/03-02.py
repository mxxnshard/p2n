password = input()
if len(password) < 8:
    print('короткий')
else:
    password2 = input()
    if password2 == password:
        print('ок')
    else:
        print('различаются')