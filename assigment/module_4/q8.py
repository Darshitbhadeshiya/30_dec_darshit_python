# Write a python program to find the longest words.

sentence=input("Enter any sentence :")
longest_word=max(sentence.split(),key=len)
print(longest_word)
print(len(longest_word))