#Hero's Inventory3.0
#演示列表

#创建一个带有元素的列表，然后用for 循环将它们显示出来
inventory = ("sword","armor","shield","healing potion")
print("\nYour items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
#获取列表的长度
print("You have", len(inventory), "item in your possession.")

input("\nPress the enter key to continue.")
#用in测试成员关系
if "healing potion" in inventory:
    print("You will live to fight another day.")
#通过索引显示列表项
index = int(input("\nEnter the index number for an item in inventory:"))
print("At index", index, "is", inventory[index])
#显示切片
start = int(input("\nEnter the index number tobegin a slice:"))
finish = int(input("Enter the index number to the end the slice:"))
print("inventory[", start, ":", finish, "] is", end="")
print(inventory[start:finish])
input("\nPress the enter key to continue.")
#连接两个列表
chest = ("gold", "gems")
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")
#通过索引进行赋值
print("You trade your sword for a crossbow.")
inventory [0]= "crossbow"
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

#进行切片赋值
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

#删除一个元素
print("In a great battle, your shield is destoryed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

#删除一个切片
print("Your crossbow and armor are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\n\nPress the enter key to exit.")




