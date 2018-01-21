# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey 
from simulton import Simulton


class Pulsator(Black_Hole):
    def __init__(self, x, y):
        self.radius = 10
        Black_Hole.__init__(self,x,y)
        self.counter = 0

    
    def update(self, model):
        prey_set = []

        for x in model.objects:
            if isinstance(x, Prey) and self.contains(x.get_location()):
                prey_set.append(x)
        for x in prey_set:
            self.change_dimension(1, 1)
            self.radius = self.get_dimension()[0]/2
        if not prey_set:
            self.counter+=1
        elif prey_set:
            self.counter = 0
        if self.counter ==30:
            self.change_dimension(-1, -1)
            self.get_dimension()[0]/2
            self.counter = 0
            if self.get_dimension() == (0,0):
                return([self])
                #model.remove(self)
               
        return prey_set
        
        
        