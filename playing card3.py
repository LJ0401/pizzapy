#Playing Cards 3.0
#演示继承--重写方法

class Card(object):
    """A playing card."""
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def _init_(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def _str_(self):
        rep = self.rank + self.suit
        return rep

#重写基类方法
class Unprintable_Card(Card):
    """A Card that wont't reveal its rank or suit when printed."""
    def _str_(slf):
        return "<unprintable>"

#调用基类方法
class Positionable_Card(Card):
    """A Card that can be face up or face down."""
    def _init_(self, rank, suit, face_up = True):
        super(Positionable_Card, self)._init_(rank, suit)
        self.is_face_up = face_up
#Positionable_Card()的下一个方法
    def _str_(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self)._str_()
        else:
            rep = "XX"
        return rep
#使用派生类
#程序主体
card1 = Card("A", "c")   #TypeError: object() takes no parameters
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")
print("Printing a Card object:")
print(card1)
#打印Unprintable_Card 的对象
print("\nPrinting an Unprintable_Card object:")
print(card2)
#打印Positionable_Card 的对象
print("\nPrinting a Postitionable_Card object:")
print(card3)

print("Flipping the Positionable_Card object:")
card3.flip()

print("Printing the Positionable_Card object:")
print(card3)

input("\n\nPress the enter key to exit.")
