'''Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle'''

class Circle:
    radius=0
    pie=3.14
    def calarea(self): 
        self.radius=int(input("Enter radius :"))
        print("Area of a cricle =",self.pie*self.radius**2)
        

    def calperimeter(self):
        print("Perimeter of a circle :",2*self.pie*self.radius)

obj=Circle()
obj.calarea()
obj.calperimeter()
