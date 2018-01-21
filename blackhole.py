# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    def __init__(self,x, y):
        self.radius = 10
        Simulton.__init__(self,x,y,20,20)
        

    def contains(self, cy):
        return self.distance(cy) < self.radius
        
        
    def update(self, model):


        prey_set = []

        for x in model.objects:
            if isinstance(x, Prey) and self.contains(x.get_location()):
                prey_set.append(x)
                

        
        return prey_set
    
    def display(self, canvas):
        canvas.create_oval(self._x-(self.get_dimension()[0]/2), self._y-(self.get_dimension()[1]/2),
                           self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[1]/2), fill='black')
           
        
        
        
    
