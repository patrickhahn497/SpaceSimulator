# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey
import random
from mobilesimulton import Mobile_Simulton
from pyexpat import model
import math

# class Prey(Mobile_Simulton):
#     def __init__(self,x,y,width,height,angle,speed):
#         Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)

class Ball(Prey):
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 2*math.pi*random.random(), 5.0)


        
    def update(self, model):
        self.move()
        self.wall_bounce()

        
    def display(self, canvas):
        canvas.create_oval(self._x-Ball.radius, self._y-Ball.radius,
            self._x+Ball.radius, self._y+Ball.radius, fill='blue')
