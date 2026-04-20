vowel=['a','e','i','o','u','A','E','I','O','U']
unique_vowel=[]
word=input("Enter a word:")
for ch in word:
          if ch in vowel:
                    if ch not in unique_vowel:
                              unique_vowel.append(ch)
print(unique_vowel)
