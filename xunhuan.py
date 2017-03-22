#Losing Battle
#演示可怕的无限循环
print("Your lone herois surrounded by a massive army of trolls.")
print("They decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")
health = 10
trolls = 0
damage = 3
while health !=0:
    trolls += 1
    health -= damage
    print("Your hero swings and defeats an evil troll, "\
          "but takes", damage, "damage points.\n")
    print("Your hero fought valiantly and defeated", trolls, "trolls.")
    print("But alas,your hero is no more.")
    input("\nPress the enter key to exit.")


#Finicky Counter
#演示break 和 continue 语句

count = 0
while True:
    count += 1
    #如果count大于10，就结束循环
    if count > 10:
        break
    #跳过5
    if count == 5:
        continue
    print(count)
input("\nPress the enter key to exit.")

