m = int(input())
all = set()
was = set()
lesson = 0
surnames = 0
for i in range(m):
       surnames = input()
       all.add(surnames)
n = int(input())
for i in range(n):
    lesson = input()
    was.add(lesson)
same = was & all
print(same)
