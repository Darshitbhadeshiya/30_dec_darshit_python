# Write a Python program to count the frequency of words in a file.


fl=open('student_data.txt','r')

for mystr in fl:
    x=mystr.count('Rukhsar')
    print(x)