def long_words(word):
   return list(filter(lambda word:len(word)>5,word))
w=input("Enter words seperated by space:")
words=w.split()
n=long_words(words)
print("Words with more than five characters:",n)
