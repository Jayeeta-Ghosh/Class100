class Circle:
    def __init__(self,radius):
        self.size=radius
    def area(self):
        print('Area:',3.14*self.size*self.size) 
    def circumference(self):
        print('Circumferance:',2*3.14*self.size)    

circle1=Circle(7)
circle1.area()
circle1.circumference()

circle2=Circle(14)
circle2.area()
circle2.circumference()
