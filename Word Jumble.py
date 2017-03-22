#Loopy String
#演示用for循环操作字符串

word = input("Enter a word:")
print("\nHere's each letter in your word:")
for letter in word:
    print(letter)

input("\nPress the enter key to exit.")

#Counter 程序 如何利用 for循环和range()函数计数
#Counter
#演示range()函数

print("Counting:")
#前向计数
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fives:")
#以五为单位计数
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting backwards:")
#后向计数
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nPress the enter key to exit.\n")

#Message Analyzer 程序
#演示len()函数和in 运算符
message = input("Enter a message:")

print("\nThe length of your message is:", len(message))

print("\nThe most common letter in the English language, 'e',")
if "e" in message:
    print("is in your message.")
else:
    print("is not in your message.")
input("\n\nPress the enter key to exit.")


#Random Access
#演示字符串的索引

#引入random模块
import random

word = "index"
print("The word is:", word, "\n")
#创建端点
high = len(word)
low = -len(word)
#执行10次的for循环
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\nPress the enter key to exit.")
#序列的最后一个元素的位置编号是它的长度减一


