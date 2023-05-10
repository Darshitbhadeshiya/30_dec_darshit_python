'''
Q.      How to Define a Class in Python?
Ans.    By using a 'class' keyword. For i.e. class Student:

Q.      What Is Self? 
Ans.    It's an identifier which holds object of the class.
        It helps to identify local and instance variables.    



---------------Give An Example Of A Python Class------------------
'''
class Student:
    id=0
    name=''
    def getdata(self):
        self.id=input("Enter id :")
        self.name=input("Enter name :")
    def printdata(self):
        print("Id :",self.id)
        print("Name :",self.name)
   

st=Student()
st.getdata()
st.printdata()
