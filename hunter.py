# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
import math
import random


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self, x, y):
        self.sight = 200
        self.radius = 10
        Mobile_Simulton.__init__(self, x,y, 20, 20, (2*math.pi*random.random()), 5.0)
        Pulsator.__init__(self, x, y)
        
        self.counter = 0
    
    def update(self, model):
        prey_set = []
        gooby = []
        
        
        for x in model.objects:
            if isinstance(x, Prey) and self.distance(x.get_location())<self.sight:
                gooby.append(x)    
            if isinstance(x, Prey) and self.contains(x.get_location()):
                prey_set.append(x)
        if gooby:
            dedman = sorted(gooby, key = lambda x: self.distance(x.get_location()))
            dedman = dedman[0]
            mathers =   atan2((dedman.get_location()[1]-self.get_location()[1]), (dedman.get_location()[0]-self.get_location()[0]))
            self.set_angle(mathers)   
     
        for x in prey_set:
            self.change_dimension(1, 1)
        if not prey_set:
            self.counter+=1
        elif prey_set:
            self.counter = 0
        if self.counter ==30:
            self.change_dimension(-1, -1)
            self.counter = 0
            if self.get_dimension() == (0,0):
                return([self])
        self.move()
        
        
        
        return prey_set
    #Pulsator.update(self, model)
        
