m = int(input())
n = int(input())
library = set()
task = set()
for i in range(m):
    books = input()
    library.add(books)
for i in range(n):
    books = input()
    task.add(books)
    if books in library:
        print('YES')
    else:
        print('NO')
