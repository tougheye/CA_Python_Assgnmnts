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
print(f'Cat is a {bob.life} object which is a inherited attribute from single parent')      # inherit from parent class
print(f'Cats are {bob.food_habit()}, which comes form its own method')    # own method


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
print(f'Horse is {Horse.save_env()} which is its own method. Horse is a multi-inheritance object')
print(f'Horse is a {Horse.life} mode of transport. That is a parent1 attribute from Animal class.')           #parent 1 attr
print(f'Horse can {Horse.carry_mode()} which is a parent2 method from Carrier class ')     #parent 2 method


#Multilevel inheritance from Cat class
class Tiger(Cat):
    def __init__(self):
        super().__init__()
        self.body_color = 'striped'

    def living_space(self):
        return 'Mostly live in the jungle'


RBT = Tiger()
print(f'Royal Bengal Tiger is {RBT.life} animal, which was inherited from the grand parent Animal class.')        # inheritance from grand parent
print(f"Bengal Tiger's food habit is {RBT.food_habit()} which comes from the parent class Cat.")       #inheritance from parent class
print(f'Bengal Tigers {RBT.living_space()} that is its own attribute')        # self attribute



