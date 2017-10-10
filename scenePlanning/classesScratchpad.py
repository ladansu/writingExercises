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

# i want each dog room to have a dictionary with keys size, derp, and fluff,
# but values that aren't filled in yet.
class Dog:
    

lulu = Dog
lulu.size = "large"
lulu.derp = "medium"
lulu.fluff = "low"

print(lulu)

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
