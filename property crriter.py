#Property Critter
#演示属性

class Critter(object):
    """A virtual pet"""
    def _init_(self, name):
         print("A new critter has been born!")
         self._name = name

         @property
         def name(self):
             return self._name
#访问属性
    def talk(self):
        print("\nHi, I'm", self.name)
#程序主体
crit = Critter("Poochie")
crit.talk()
#为小动物改个名字
print("\nAttempting to change my critter's name to Randoph...")
crit.name = "Randoph"

print("My critter's name is:", end=" ")
print(crit.name)

#将名字改成空格符
print("\nAttempting to change my critter's name to the empty string.")
crit.name =""

print("My critter's name is:", end=" ")
print(crit.name)

input("\n\nPress the enter key to exit.")
