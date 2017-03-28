#Handle It
#演示异常处理

#try/except
try:
    num = float(input("Enter a number:"))
except:
    print("Smoething went wrong)

#指定异常类型
try:
    num = float(input("\nEnter a number:"))
except ValueError:
    print("That was not a number!")

#处理多种异常类型
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end="")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

#try/except/else
try:
    num = float(input("\nEnter a number:"))
except ValueError:
    print("That was not a numer!")
else:
    print("You entered the number", num)

input("\n\nPress teh enter key to exit.")


