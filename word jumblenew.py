#word jumble
import random
#创建一组可供选择的单词
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
#从那个序列中随机挑一个单词
word = random.choice(WORDS)
correct = word
#创建乱序版的单词
jumble = ""
while word:
position = random.randrange(len(word))
jumble += word[position]
word = word[:position] + word[(position + 1):]

#开始游戏
print(
    """
     Welcome to Word Jumble!
    Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
    )
print("The jumble is:", jumble)
#获取玩家答案
guess = input("\nYour gues:")
while guess != correct and guess != "":
   print("Sorry, that's not it.")
   guess = input("Your guess:")
#向玩家表示恭喜
   if guess == correct:
       print("That's it! You guess it!\n")
print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
