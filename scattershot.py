'''
Created on Jun 4, 2016

@author: Patrick Hahn
'''
from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton
from prey import Prey
import math
import random



class Special(Black_Hole, Prey):
    def __init__(self,x , y):
        self.radius = 4
        self._x = x
        self._y = y
        Prey.__init__(self, x, y, 8, 8, 2*math.pi*random.random(), 15.0)
        Black_Hole.__init__(self, x, y)
        
    def update(self, model):
        prey_set = []

        for x in model.objects:
            if isinstance(x, Prey) and self.contains(x.get_location()) and type(x) != Special:
                prey_set.append(x)
        self.move()
        self.wall_bounce()
                
        return prey_set
    
    
    
    def display(self, canvas):
        canvas.create_oval(self._x-(self.get_dimension()[0]/2), self._y-(self.get_dimension()[1]/2),
                           self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[1]/2), fill='yellow')