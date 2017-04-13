#Pizza Panic
#玩家必须在披萨掉到地上之前把他们接住

#首先引入games,color模块并初始化图形屏幕
from livewires import games, color
#random模块可以让疯厨子做决定时更逼真
import random

#games的init()以便初始化屏幕并产生mouse对象
games.init(screen_width = 640, screen_height = 480, fps = 50)

#Pan类
#加载平底锅图片
class Pan(games.Sprite):
    """
    A pan controlled by player to catch falling pizzas.
    """
    image = games.load_image("pan.bmp")
#_init_()方法 用于初始化对象的构造器
    def _init_(self):
        """Initialize Pan object and creat Text object for score."""
        super(pan, self)._init_(image = Pan_image,
                                x = games.mouse.x,
                                bottom = games.screen.height)
#定义用于表示玩家分数的特性，初始值为0
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5,right = games.screen.width - 10)

        games.screen.add(self.score)
#update()方法，用于移动玩家的平底锅
    def update(self):
        #将鼠标的x坐标赋值给Pan对象的x坐标，这样玩家可以利用鼠标左右移动平底锅
        "Move to mouse x position."""
        self.x = games.mouse.x

       #该对象左沿是否小于0——平底锅的左沿越过了图形屏幕的左边界，如果是，将其设置为0
       if self.left < 0:
            self.left = 0

        #该对象右沿是否大于于games.screen.width——平底锅的右沿越过了图形屏幕的右边界，
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()
#check_catch()方法
    def check_catch(self):
        """Check if catch pizzas."""
       #每当有一个对象与这个平底锅重叠，玩家就加10分
       for pizza in self.overlpping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            #调用重叠对象
            pizza.handle_caught()

#Pizza类——用于表示掉落的披萨
#先定义两个类变量，表示图片的image和披萨掉落的速度
class Pizza(games.Sprite):
    """
    A pizza which falls to the ground.
    """
    image = games.load_image("pizza.bmp")
    speed = 1

#_init_()方法，用来初始化一个新的Pizza对象
    #注意将y的默认值设置成了90，是为了让每个新披萨刚好出现在厨子胸口
    def _init_(self, x, y = 90):
        """Initialize a Pizza object."""
        super(Pizza, self). _init_(image = Pizza.image,
                                   x = x, y = y,
                                   de = Pizza.speed)

#update()方法，用于处理屏幕边界判断
    def update(self):
        """Check if bottom edge has reached screen bottom."""
        if self.bottom > games.screen.height:
            #从屏幕上移除碰到屏幕底部的对象
            self.end_game()
            self.destory()
    
        
        
                            

