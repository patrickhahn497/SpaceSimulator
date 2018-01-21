import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from simulton import Simulton
from scattershot import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running = False
cycle_count = 0
selected_ob = None
objects = set()
select_item = None
remover = False



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, objects
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    running     = False
    cycle_count = 0
    objects  = set()

#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 
  
#step just 1 update in the simulation
def step ():
    
    global cycle_count, running, objects
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    listo =[]
    cycle_count += 1
    for b in objects:      
        x = b.update(model)
        if x != None:
            listo.extend(x)
#         else:
#             b.update(model)
    for y in set(listo):
        objects.remove(y)
    if running:
        running = False

     
    
      
#     if running == True:
#         stop()



#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_ob
    selected_ob = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
   # print(x, y)
    global objects

    if selected_ob != None:
        if selected_ob =="Remove":
            new_set = set()
            for reb in objects:
                if reb.distance((x, y)) < (reb.get_dimension()[0]/2):
                    new_set.add(reb)
                   # objects.remove(reb)
            for top in new_set:
                objects.remove(top)
            
#             doop = find(lambda b: b.distance((x,y)) <x.radius)
#             for t in doop:
#                 remove(t)

#             remove(eval('({}, {})'.format(x, y)))
#         print(selected_ob)
        else:
            add( eval(selected_ob+'({}, {})'.format(x, y)))

    


#add simulton s to the simulation
def add(s):
    global objects
    objects.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global objects
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    objects.remove(s)

    for x in objects:
        x.display(controller.the_canvas)
    controller.the_progress.config(text=str(cycle_count)+" updates/"+str(len(objects))+" simultons")
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    newset = set()
    for x in objects:
        if p(x):
            newset.add(x)
    return newset

#call update for every simulton in the simulation
def update_all():
    global running
    if running:       
#         for o in controller.the_canvas.find_all():
#             controller.the_canvas.delete(o)
        step()
        running = True

        
#     for x in objects:
#         
#         x.update(model)



#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    for x in objects:
        x.display(controller.the_canvas)
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(objects))+" simultons")
