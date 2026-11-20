s=input()
words = s.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
print(len(longest_word))

#Второй способ
print(max(words, key=len))