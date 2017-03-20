#Trust Fund Buddy - Good
#演示类型转换

print(
    """
        Trust Fund Buddy
Totals your monthly spending so that  your trust  fund doesn't run out
(and you're forced to get a real job).
Please enter the requested,monthly costs, Since you're rich, ignore pennis
and use only doallr amounts.
"""
    )

car=input("Lamborgjini Tune-Ups:")
car= int(car)
rent =int(input("Manthattan Apartment:"))
jet = int(input("Private Jet Rental:"))
gifts = int(input("Gifts:"))
food = int(input("Dining Out:"))
staff = int(input("Staff (butlers, chef, driver, assistant:"))
guru = int(input("Personal Guru and Coach:"))
games = int(input("Computer Games:"))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

input("\nPress the enter key to exit.")
