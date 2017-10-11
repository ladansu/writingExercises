# objective: define the MRU class

#next time: re-write the dog program so each quality is an attribute

# here's a toy program max made for me to study
#class Dog():
#    def __str__(self):
#        qualities = [muchness + " " + characteristic for characteristic, muchness in self.__dict__.items()]
#        if qualities:
#          return "I'm a " + ", ".join(qualities) + " dog"
#        else:
#          return "I'm a featureless dog on a frictionless plane"
#    def speak(self):
#        print("Woof!")

#lulu = Dog()
#print(lulu)
#lulu.size = "large"
#lulu.derp = "medium"
#lulu.fluff = "low"
#print(lulu)

#lulu.cute = "lots"
#print(lulu)

#when the constructor does it
class Dog():
    def __init__(self, size, fluff, derp):
        self.size = size
        self.fluff = fluff
        self.derp = derp

lulu = Dog("large", "low", "medium")
print(lulu.size, lulu.fluff, lulu.derp)

#class Dog(x,y,z)
#    size = x
#    fluff = y
#    derp = z
#lulu = Dog(large, low, medium)
#print(lulu)

class Cat:
    def speak(self):
        print("Meow!")
scruffles = Cat()

#lulu.speak()
scruffles.speak()

class bleg():
   pass
class rube():
   pass

listOfRubesAndBleg = [bleg(), rube(), rube()]
print(listOfRubesAndBleg)

# the kangaroo toy program max gave me to study
class Animal:
    def jump(self):
        print("Boing!")

    def is_marsupial(self):
        return False

class Kangaroo(Animal):
    def is_marsupial(self):
        return True

k = Kangaroo()
print(k.is_marsupial())
k.jump()
