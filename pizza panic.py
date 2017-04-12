#New Graphics Window
#演示创建图形窗口

from livewires import games

#初始化图形屏幕
games.init(screen_width = 640, screen_height = 480, fps = 50)

#启动主循环
games.screen.mainloop()

#Background Image
#演示设置图形屏幕的背景图片

from livewires import games
#屏幕的宽带度由传给screen_width的值决定，高度由传给screen_height的值决定，fps 表示的是屏幕每秒刷新的次数
games.init(screen_width = 640, screen_height = 480, fps = 50)
#加载图片，将保存在wall.jpg文件中的图片加载到内存里去
wall_image = games.load_image("wall.jpg", transparent = False)
#设置图片背景
games.screen.background = wall_image

games.screen.mainloop()

#Pizza Sprite
#演示创建sprite


from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg", transparent = False)
#设置图片背景
games.screen.background = wall_image
#将披萨图片加载到内存中创建一个图片对象
pizza_image = games.load_image("pizza.bmp")
#创建一个披萨sprite
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
#将sprite添加到图形屏幕
games.screen.add(pizza)

games.screen.mainloop()

#Big Score
#演示在图形屏幕上显示文本

#引入color模块
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg",transparent = False)
games.screen.background = wall_image

#创建Text对象
score = games.Text(value = 1756521,
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 30)
#向屏幕添加text对象
games.screen.add(score)

games.screen.mainloop()

#You Won
#演示显示消息

#引入color模块
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg",transparent = False)
games.screen.background = wall_image

#创建Message对象
won_message = games.Message(value = "you won!",
                            size = 100,
                            color = color.red,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 250,
                            after_death = games.screen.quit)
#把Message对象放到屏幕上去
games.screen.add(won_message)

games.screen.mainloop()

#Moving Pizza
#演示sprite的速度特性

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg",transparent = False)
games.screen.background = wall_image

pizza_image = gamess.load_image("pizza.bmp")
#设置sprite的速度值，让披萨动起来
the_pizza = games.Sprite(image = pizza_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx = 1,
                         dy = 1)
games.screen.add(the_pizza)

games.screen.mainloop()

#Bouncing Pizza
#演示如何处理屏幕边界

#下面两行代码是为了引入game模块并创建图形屏幕
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)
                            
#为了使sprite有非预设的弹跳行为，派生出一个新类

class Pizza(games.Sprite):
    """A bouncing pizza."""

#将单向移动的披萨变成活蹦乱跳的，重写update()方法
    def update(self):
       #首先判断sprite 是否快要越过屏幕边界（各个方向），如果是就反转相应的速度分量
       """Reverse a velocity component if edge of screen reached."""
       if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

       if self.bottom > games.screen.height or self.top <0:
            self.dy = -self.dy
            
#收尾工作
def main():
        wall_image = games.load_image("wall.jpg", transparent = False)
        games.screen.background = wall_image

        pizza_image = games.load_image("pizza.bmp")
        
        the_pizza = games.Sprite(image = pizza_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx = 1,
                         dy = 1)
        games.screen.add(the_pizza)

        games.screen.mainloop()

#走你
main()
                          
#Moving Pan
#演示鼠标输入

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

#读取鼠标的X和y坐标（创建表示平底锅的Pan类）
class Pan(games.Sprite):
    """A pan controlled by the mouse."""
    def update(self):
        """Move to mouse coordinates."""
        self.x = games.mouse.x
        self.y = games.mouse.y
#设置背景图片
    def main():
        wall_image = games.load_image("wall.jpg", transparent = False)
        games.screen.background = wall_image

        pan_image = games.load_image("pan.bmp")
        the_pan = pan(image = pan_image,
                      x = games.mouse.x,
                      y = games.mouse.y)
        games.screen.add(the_pan)

#设置鼠标光标的可见性
        games.mouse.is_visible = False

#捕获图形屏幕的输入
        games.screen.event_grab = True
#刷新屏幕上的所有东西
        games.screen.mainloop()

#开播
main()

#Slippery Pizza Program
#演示sprite的碰撞检测

from livewires import games
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

#添加检测碰撞的代码

class Pan(games.Sprite):
    """A pan controlled by the mouse."""
    def update(self):
        """Move to mouse position."""
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """Check for collision with pizza."""
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()
#碰撞处理
class Pan(pizza.Sprite):
    """A slippery pizza."""
    def handle_collide(self):
        """Move a random screen location."""
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)
#收尾工作
    def main():
        wall_image = games.load_image("wall.jpg", transparent = False)
        games.screen.background = wall_image

        pizza_image = games.load_image("pan.bmp")
        pizza_x= random.randrange(games.screen.width)
        pizza_y = random.randrange(games.screen.height)
        the_pizaa = Pizza(image = pizza_image, x = pizza_x, y = pizza_y)
        games.screen.add(the_pizza)

        pan_image = games.load_image("pan.bmg")
        the_pan = pan(image = pan_image,
                      x = games.mouse.x,
                      y = games.mouse.y)
        games.screen.add(the_pan)

        games.mouse.is_visible = False

        games.mouse.event_grab = True

        games.screen.mainloop()

#发轫之始
main()

        
