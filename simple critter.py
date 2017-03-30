#Simple Critter
#演示一个简单的类及其对象

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm an instance of class critter.")

#程序主体
crit = Critter()
crit.talk()

input("\n\nPress the enter key to exit.")


#Constructor Critter
#演示构造器

class Critter(object):
    """A virtual pet"""
    def _init_(self):
        print("A new critter has been born!")

    def talk(self):
        print("\nHi. I'm an instance of class Critter.")

#程序主体
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit.")
