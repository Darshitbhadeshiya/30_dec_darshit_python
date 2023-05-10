'''Q.      What is used to check whether an object o is an instance
        of class A?

Ans.    The Python’s isinstance() function checks whether the object
        or variable is an instance of the specified class type or 
        data type.'''

class fruits:
    def getdata(self):
        self.name="Apple"
        self.color="Red"
        print(self.name,self.color)

class Flower:       
        def getdata2(self):
            self.name="Rose"
            self.color="Red"
a=fruits()
b=Flower()
print("Is a object of class fruits ?\n",isinstance(a,Flower))
