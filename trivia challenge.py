#Trivia Challenge
#可以读取纯文本文件的益智游戏

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

#next_line()函数
def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

#next_block()函数
def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.appened(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explantion = next_line(the_line)

    return category, question, answers, correct, explantion

#welcome（）函数
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

#游戏初始化
def main():
    trivia_file = open_file("trivia.txt.")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
#提出问题
#获取第一个块
category, question, answers, correct, explanation = next_block(trivia_file)
while category:
    #提问
    print(category)
    print(question)
    for i in range(4):
         print("\t", i+1, "-", answers[i])

#获取答案
answer = input("What's your answer?:")
#判断答案
if answer == correct:
    print("\nRight!", end="")
    score +=1
else:
    print("\nWorng.", end="")
print(explanation)
print("Score:", score, "\n\n")
#获取下一个问题块
category, question, answers, correct, explanation =next_block(trivia_file)
#结束游戏
trivia_file.close()

print("That was the last question!")
print("You're final score is", score)

#启动main()函数
main()
input("\n\nPress the enter key to exit.")
        
