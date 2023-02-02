from abc import ABC, abstractmethod 
from math import pi


class Shape(ABC):
    '''this is an abstract class for defining shape'''
    @abstractmethod
    def area(self):
        ''' this method must be implemented in the base class ''' 
        
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width*self.height
    
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius*self.radius*pi 
    
    
a=Rectangle(12, 3)
c=Circle(10)

print(a.area())
