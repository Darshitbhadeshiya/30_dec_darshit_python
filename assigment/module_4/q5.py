# Write a Python program to read last n lines of a file.

f=open('student_data.txt','r')
print(f.readlines()[-1])