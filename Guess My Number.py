#Craps Roller
#演示随机数的生成
import random
#生成1到6之间的随机数
die1 = random.randint(1, 6)
#调用randint（）
die2 = random.randrange(6) + 1
total = die1 + die2
print("You rolled a", die1, "and a", die2, "for a total of", total)
input("\nPress the enter key to exit.")


#设置初始值
the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

#猜测循环
while guess != the_number:
    if guess > the_number:
       print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess:")
    tries += 1
                
