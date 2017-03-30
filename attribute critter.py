#Attribute Critter
#演示创建和访问对象的特性

class Critter(object):
    """A virtual pet"""
    def _init_(self, name):
         print("A new critter has been born!")
         self.name = name

    def _str_(self):
        rep = "Critter object\n"
        rep += "name:" + self.name + "\n"
        return rep
    def talk(self):
        print("Hi. I'm", self.name, "\n")

#程序主体
crit1 = Critter("Poochie")   //运行显示TypeError: object() takes no parameters
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

input("\n\nPress the enter key to exit.")

