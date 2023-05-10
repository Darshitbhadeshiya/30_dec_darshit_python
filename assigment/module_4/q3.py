'''Write a Python program to append text to a file and 
display the text.'''

f=open("Mobile.txt",'a')
def getMobileData():
    brand=input("Enter mobile brand :")
    price=input("Enter mobile price :")
    f.write(f"Mobile Brand = {brand}\nPrice ={price}\n")
   

n=int(input("Enter number of data :"))
for i in range(n):
    getMobileData()













