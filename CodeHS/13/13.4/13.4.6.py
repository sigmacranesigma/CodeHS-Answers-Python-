text = input("Text: ").split()
words = {}
for i in text:
    if i not in words:
        words[i] = 1
    else:
        words[i] += 1
print(words)
