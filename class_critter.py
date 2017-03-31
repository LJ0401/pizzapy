#Classy Critter
#演示类特性和静态方法

class Critter(object):
    """A virtual pet"""
    #创建类特性
    total = 0

    @staticmethod
 #创建静态方法
    def status():
        print("\nThe total nmber of critters is", Critter.total)

    def _init_(self, name):
        print("A critter has been born!")
        self.name = name
        Critter.total +=1

#程序主体
print("Accessing the class attribute Critter.total:", end="")
print(Critter.total)
print("\nCreating critters.")#TypeError: object() takes no parameters
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")
#调用静态方法
Critter.status()

print("\nAccessing the class attribute through an object:", end="")
#访问类特性
print(crit1.total)

input("\n\nPress the enter key to exit.")
