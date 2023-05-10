'''Write a Python program to read a file line by line and store it 
into a list'''

with open('student_data.txt') as file:
    l=file.readlines()
    l=[line.rstrip() for line in l]
print(l)