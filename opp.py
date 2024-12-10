class Animal:
    alive = True
    def __init__(self):
        self.eat

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
        
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
 #polymorphism - dervived classes can behave diffrenetlu for the same method inherited from the base
 #with polymorphism a method name can mean different thing across mutiple classes
 #eg the different animals can swim, run or fly
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)

