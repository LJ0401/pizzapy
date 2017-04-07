#引入cards和games模块
#Blackiack
#From 1 to 7 players compete against a dealer

import cards, games

#BJ_Card类
class BJ_Card(cards.Card):
    """A Blackjack Card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v
#BJ_Deck类
class BJ_Deck(cards.Deck):
    """A Blackjack Deck."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_CARD.RANKS:
                self.cards.append(BJ_Card(rank, suit))

#BJ_Hand类
class BJ_Hand(cards.Hand):
    """A Blackjack Hand."""
    def _init_(self, name):
        super(BJ_Hand, self)._init_()
        self.name = name
    #显示牌的总点数
    def _str_(self):
        rep = self.name + ":\t" + super(BJ_Hand, self)._str_()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    #创建total的属性
    @property
    def total(self):
        #如果当前这手牌中有一张牌的value为None,则total为None.
        for card in self.cards:
            if not card.value:
                return None

        #把牌的点数加起来，A的点数记为1
        t = 0
        for card in self.cards:
            t += card.value

        #判断当前这手牌中有没有A
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        #如果有A且total够小，则将A记为1
        if contains_ace and t <= 11:
            #因为已经为这张A加了1，所以这里只加10
            t += 10
        return t

#BJ_Player类
class BJ_Player(BJ_Hand):
    """A Blackjack Player."""
    def  is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N):")
        return response == "y"
    def bust(self):
        print(self.name, "busts.")
        self.lose()
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")

#BJ_Dealer类
class BJ_Dealer(BJ_Hand):
    """A Blackjack Dealer."""
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

#BJ_Game类
#_init_()方法
class BJ_Game(object):
    """A Blackjack Game."""
    def _init_(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
#still_playing属性
    @property
    def still_playing(self):
         sp = []
         for player in self.players:
             if not player._is_busted():
                 sp.append(player)
         return sp
#_additional_cards()方法
    def _additional_cards(self, player):
        while not player.is_busted() and player.is__hitting():
         self.deck.deal([player])
         print(player)
         if player.is_busted():
            player.bust()
#play()方法
    def play(self):
         #给每个人发两张牌
         self.deck.deal(self.players + [self.dealer], per_hand = 2)
         self.dealer.flip_first_card()
         for player in self.players:
             print(player)
         print(self.dealer)

         #给所有的玩家加牌
         for player in self.players:
             self._additional_cards(player)

         self.dealer.flip_first_card() #翻开庄家的第一张牌
         if not self.still_playing:
            #由于所有玩家都爆牌了，因此可直接亮出庄家手中的牌
            print(self.dealer)
         else:
              #给庄家加牌
              print(self.dealer)
              self._additional_cards(self.dealer)

              if self.dealer.is_busted():
                 #所有还在玩的玩家获胜
                 for player in self.still_playing:
                     player.win()
         else:
              #每位还在玩的玩家跟庄家比点数
              for player in self.still_playing:
                  if player.total > self.dealer.total:
                      player.win()
                  elif player.total < self.dealer.total:
                      player.lose()
                  else:
                       player.push()
         #清空所有人手中的牌
         for player in self.players:
             player.clear()
         self.dealer.clear(）
#main()函数
def main():
    print("\t\tWelcome to Blackjack!\n")
    name = []
    number = games.ask_number("How many players? (1 - 7):", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name:")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again !="n":
         game.play()
         again = games.ask_yes_no("\nDo you want to play again?:")

main()
input("\n\nPress the enter key to exit.")
         
        
