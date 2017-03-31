#Playing Card 2.0
#演示继承-类扩展

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

class Hand(object):
    """A hand of playing cards."""
    def _init_(self):
        self.cards = []

    def _str_(self):
        if self.cards:
            rep = ""
            for card in self.cards:
            rep += str(card) + "\t " 
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
#创建基类
class Deck(Hand):
#扩展派生类
    """A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in CARD.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't contiune deal. Out of cards!")
#使用派生类
#程序主体
                    print("Created a new deck.")
                    print("Deck:")
                    print(deck1)
                    deck1.populate()
                    print("\nPopulated the deck.")
                    print("Deck:")
                    print(deck1)
#洗牌
                    deck1.shuffle()
                    print("\nShuffle the deck.")
                    print("Deck:")
                    print(deck1)
#创建两个Hand对象
                    my_hand = Hand()
                    your_hand = Hand()
                    hands = [my_hand, your_hand]
#分别派发五张牌
                    deck1.deal(hands, per_hand = 5)

                    print("\nDeal 5 cards to my hand and your hand.")
                    print("My hand:")
                    print(my_hand)
                    print("Your hand:")
                    print(your_hand)
                    print("Deck:")
                    print(deck1)
#清空这副牌使其回到初始状态
                    deck1.clear()
                    print("\nClear the deck.")
#再打印一次
                    print("Deck:", deck1)
                    input("\n\nPress the enter key to exit.")
                          
