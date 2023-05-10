'''Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle'''

class Rectangle:
    length=0
    width=0

    def calarea(self):
        self.length=int(input("Enter length :"))
        self.width=int(input("Enter width :"))
        print("Area of a rectangle =",self.length*self.width)
 
a=Rectangle()
a.calarea()
        