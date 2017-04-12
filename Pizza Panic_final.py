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
                            

