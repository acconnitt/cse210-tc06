# The guess class gets and stores the last guess of each player.
class Guess:
    
    def __init__(self, code, guess="____"):
        """The class constructor.  
        """
        self.__code = str(code)
        self.__guess = str(guess)
        self.hint = "OOOO"

    def check_guess(self):
        index = 0
        x = list(self.hint)
        for letter in self.__code:
            if letter == self.__guess[index]:
                x[index] = "X"
            index += 1
        self.hint = "".join(x)
        

    def get_code(self):
        
        return self.__code

    def get_guess(self):
        
        return self.__guess

