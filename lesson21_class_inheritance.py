#class inheritance

#slicing lists and diitnonnaries

#here we have a class
class Fish:
    def init(self):

#now we add an inheritor by adding a paramater class
#and adding super in

class Fish(Animal):
    def init(self):
        super().init()
        #basically says initiliaze everything from Animal class in our fish class
        #  

#############################################################################################
class Animal:
    def __init__(self):
        self.num_eyes = 2


    def breathe(self):
        print('inhale, exhale')

class Fish(Animal):
    #If we want fish to do everything animal can do, we do this
    def __init__(self):
        super().__init__()


    def swim(self):
        print('moving in water')

    #say we want to edit a previous classes method
    def breathe():
        super().breathe()
        print('doing this underwater..')


nemo = Fish()
nemo.swim()
#now we have access in fish to animal class things
nemo.breathe()

#SLICING a list
piano_keys = [a,b,c,d,e,f,g]
piano_keys[2:5]
#we can also incrementthe slice
piano_keys[2:5:2]
#we want everything, but every second item
piano_keys[::2] # == beginning to end, but every other item.


