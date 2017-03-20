#Password
#演示if语句
print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")
password = input("Enter your password:")
if password == "secret":
    print("Access Granted")
input("\nPress the enter key to exit.")

#Granted or Denied
#演示else子句
print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")
password = input("Enter your password:")
if password == "secret":
    print("Access Granted")
else:
    print("Access Denied")
    
input("\nPress the enter key to exit.")


#Three Year-Old Simulator
#演示while 循环
print("Welcome to 'Three Year-Old Simulator'\n ")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")
response = ""
while response != "Because.":
    response = input("Why?\n")
print("Oh. Okay.")
input("\nPress the enter key to exit.")
