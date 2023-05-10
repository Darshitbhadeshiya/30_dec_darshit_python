# Write a Python program to write a list to a file.

f=open('list.txt','w')

fruit=['apple','banana','orange','kiwi','litchi']
for i in fruit:
    f.write(i+'\n')
    #print(i+'\n')
f.close()