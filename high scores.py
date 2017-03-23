#High Scores
#演示列表方法

scores = []
choice = None

while choice != "0":
    print(
        """
       High Scores

       0 - Exit
       1 - Show Scores
       2 - And a Score
       3 - Remove a Score
       4 - Sort Scores
       """
        )
    choice = input("Choice:")
    print()

    #退出
    if choice == "0":
        print("Good-bye.")

    #列出最高分表
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

    #添加一个得分
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)
    #删除一个得分
    elif choice == "3":
        score = int(input("Remove which score?:"))
        if score in scores:
            scores.remove(score)
        else:
                print(score, "isn't in the high scores list.")
    #对分数排序
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
    input("\n\nPress the enter key to exit.")
