# objective: define the MRU class

#next time: understand why the linter says "dog has no attribute derp"

# here's a toy program max made for me to study
class Dog():
    def __str__(self):
        qualities = [value + " " + property for property, value in self.__dict__.items()]
        if qualities:
          return "I'm a " + ", ".join(qualities) + " dog"
        else:
          return "I'm a featureless dog on a frictionless plane"
    def speak(self):
        print("Woof!")

lulu = Dog()
print(lulu)
lulu.size = "large"
lulu.derp = "medium"
lulu.fluff = "low"
print(lulu)

lulu.cute = "lots"
print(lulu)

class Cat:
    def speak(self):
        print("Meow!")
scruffles = Cat()

lulu.speak()
scruffles.speak()

rubesAndBlegs = []
class bleg():
    def __init__(self):
        rubesAndBlegs.append(self)

class rube():
    def __init__(self):
        rubesAndBlegs.append(self)

thing1 = bleg()
thing2 = bleg()
thing3 = rube()

print(rubesAndBlegs)
