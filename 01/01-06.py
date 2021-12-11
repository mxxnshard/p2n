print('Любите ли вы котиков?')
first = input()
print('Любите ли вы собак?')
second = input()
if first == 'да' and second == 'да':
    print('Вы любите и кошек, и собак.')
elif first == 'да' and second == 'нет':
    print('Вы любите кошек, но не любите собак.')
elif first == 'нет' and second == 'да':
    print('Вы любите собак, но не любите кошек.')
else:
    print('Вы не любите ни собак, ни кошек.')