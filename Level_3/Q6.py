'''Create the custom Python classes which have methods and attributes
and implement single inheritance, multiple inheritance,
and multilevel inheritance
'''
# Base class
class Animal:
    def __init__(self):
        self.life = 'living'

    def mobility_mode(self):
        return 'can walk, run, swim'

# single inheritance of the Animal
class Cat(Animal):
    def __init__(self):
        super().__init__()              #initializing the parent class in order to add it's own attribute domesticated besides the parent attributes
        self.mammal = 'yes'

    def food_habit(self):
        return 'mostly carnivorous'


# Demonstrate single inheritance
bob = Cat()
print(f'Cat is a {bob.life} object')      # inherit from parent class
print(f'Cats are {bob.food_habit()}')    # own method


# Multiple inheritance
class Carrier:
    def __init__(self):
        self.carry_load = 'yes'

    def carry_mode(self):
        return 'Can carry people'

#Child class inherits from Animal and Carrier classes
class EnvFrndTrnsprt(Animal,Carrier):

    def save_env(self):
        return "Environment friendly mode of transport."

Horse = EnvFrndTrnsprt()
print(f'Horse is a {Horse.life} mode of transport')           #parent 1 attr
print(f'Horse can {Horse.carry_mode()}')     #parent 2 method
print(f'Horse is {Horse.save_env()}')     #self attr


#Multilevel inheritance from Cat class

class Tiger(Cat):
    def __init__(self):
        super().__init__()
        self.body_color = 'striped'

    def living_space(self):
        return 'Mostly live in the jungle'


RBT = Tiger()
print(f'Royal Bengal Tiger is {RBT.life} animal')        # inheritance from grand parent
print(f"Bengal Tiger's food habit is {RBT.food_habit()}")       #inheritance from parent class
print(f'Bengal Tigers {RBT.living_space()}')        # self attribute



