#Write a Python program to count the number of lines in a text file.
fl=open("student_data.txt",'r')
x=len(fl.readlines())
print(x)