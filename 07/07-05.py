word1 = input()
word2 = input()
while word1[-1] == word2[0]:
    word1 = word2
    word2 = input()
else:
    print(word2)
