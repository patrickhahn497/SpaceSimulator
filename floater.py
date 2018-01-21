# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage

from prey import Prey
from random import random 
from random import uniform

import math


class Floater(Prey):
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 2*math.pi*random(), 5.0)
        self.radius = 5
    
    
    def update(self, model):
        rando = random()

        if rando<=0.3:
            
            rand_speed = uniform(-0.5, 0.5)
            rand_ang = 2*math.pi*uniform(-0.5, 0.5)
            self.set_speed(rand_speed)
            self.set_angle(rand_ang)             
        
        self.move()
        self.wall_bounce()

        
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius,
            self._x+self.radius, self._y+self.radius, fill='red')