#Hero's Inventory
#演示元组

#创建一个带有内容的元组，然后用一个for 循环将它们显示出来
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print("\nYour items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
#获取元组的长度
print("You have", len(inventory), "item in your possession.")

input("\nPress the enter key to continue.")
#用in测试成员关系
if "healing potion" in inventory:
    print("You will live to fight another day.")
#通过索引显示元素
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])
#显示切片
start = int(input("\nEnter the index number tobegin a slice:"))
finish = int(input("Enter the index number to the end the slice:"))
print("inventory[", start, ":", finish, "] is", end="")
print(inventory[start:finish])


input("\nPress the enter key to continue.")
#连接两个元组
chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\n\nPress the enter key to exit.")
