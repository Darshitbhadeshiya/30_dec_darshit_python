'''Q.      Explain Inheritance in Python with an example? 


Ans.    Inheritance allows us to define a class that inherits 
        all the methods and properties from another class.
        
        Python supports 3 types of inheritance:
        1.single 
        2.multiple
        3.multilevel

        Parent class: 
        Parent class is the class being inherited from , also called
        a base class.

        Child class:
        Child class that inherits from another class , also called
        derived class.
        
------------------Inheritance Example------------------------        
        '''

class Parent:
    def getdata(self):
        self.a=int(input("Enter value of a :"))
        self.b=int(input("Enter value of b :"))
class Child(Parent):
    def sum(self):
        print("Sum of a and b :",self.a+self.b)

ch=Child()
ch.getdata()
ch.sum()


'''

Q.      What is init? Or What Is A Constructor In Python?

Ans.    A constructor is a special method that the program 
        calls upon an object's creation. The constructor is used 
        in the class to initialize data members to the object.
        The special method __init__ is the Python constructor. 


        '''
