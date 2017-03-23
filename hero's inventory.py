#Hero's Inventory
#演示元组的创建

#创建一个空的元组
inventory = ()
#把元组当作条件用
if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

#创建一个带有一些内容的元组
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

#打印元组
print("\The tuple inventory is :")
print(inventory)

#打印元组中的各个元素
print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")
