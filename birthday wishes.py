#Birthday Wishes
#演示关键字参数和默认参数值

#位置参数
def birthday1(name,age):
    print("Happy birthday,", name, "!", "I hear you're", age, "today.\n")

#带默认值的参数
def birthday2(name = "liujie", age =1):
     print("Happy birthday,", name, "!", "I hear you're", age, "today.\n")


birthday1("liujie",1)
birthday1(1, "liujie")
birthday1(name = "liujie", age = 1)
birthday1(age = 1, name = "liujie")

birthday2()
birthday2(name = "jj")
birthday2(age = 23)
birthday2(name = "jj", age = 23)
birthday2("jj", 23)

input("\n\nPress the enter key to exit.")
