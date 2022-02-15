list1 = set()
list2 = set()
num1 = 0
num2 = 0
while num1 != '':
    num1 = input()
    list1.add(num1)
while num2 != '':
    num2 = input()
    list2.add(num2)
same = list1 & list2
same.discard('')
if len(same) > 0:
    print(same)
else:
    print('empty')
