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
    
        
