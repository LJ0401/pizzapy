#Games
#演示模块的创建

class Player(object):
    """A player for a game."""
    def _init_(self, name, score = 0):
        self.name = name
        self.score = score

        def _str_(self):
            rep = self.name + ":\t" + str(self.score)
            return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
    
if _name_ == "_main_": #NameError: name '_name_' is not defined??
    print("You ran this  module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
