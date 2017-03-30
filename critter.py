#构造器方法

#Critter Caretaker
#一只需要细心呵护的虚拟动物

class Critter(object):
    """A virtual pet"""
    def _init_(self, name, hunger = 0, boredom =0):
        self.name = name
        self.hunger = hunger
        self.bordom = boredom

#_pass_time()方法
    def _pass_time(self):
          self.hunger += 1
          self.boredom += 1

#mood属性
    @property
    def mood(self):
          unhappines = self.hunger + self.boredom
          if unhappines <5:
              m = "happy"
          elif 5 <= unhappines <= 10:
              m = "okay"
          elif 11 <= unhappines <=15:
              m = "frustrated"
          else:
              m = "mad"
          return m

#talk()方法
    def talk(self):
            print("I'm", "and I feel", self.mood, "now.\n")
            self._pass_time()

#eat()方法
    def eat(self, food = 4):
                print("Brruppp. Thank you.")
                self.hunger -= food
                if self.hunger < 0:
                    self.hunger = 0
                self._pass_time()

#play()方法
    def play(self, food = 4):
                    print("Wheee!")
                    self.boredom -= fun
                    if self.boredom <0:
                        self.boredom = 0
                    self._pass_time()

#创建Critter
    def main():
                    crit_name = input("What do you want to nsme your critter?:")
                    crit = Critter(crit_name)

#创建菜单系统
    choice = None
    while choice != "0":
                    print\
                    ("""
                      Critter Caretaker

                      0 - Quit
                      1 - Listen to your ceitter
                      2 - Feed your critter
                      3 - Play with your critter
                      """)

                    choice = input("Choice:")
                    print()

                    #退出
                    if choice == "0":
                        print("Good_bye.")

                    #倾听宠物的心声
                    elif choice == "1":
                        crit.talk()
                    #给宠物喂食
                    elif choice == "2":
                        crit.eat()
                    #跟宠物玩耍
                    elif choice == "3":
                        crit.play()
                    #未知选项
                    else:
                        print("\nSorry, but", choice, "isn't a valid choice.")

#启动程序
main()
("\n\nPress the enter key to exit.")
                    
            
