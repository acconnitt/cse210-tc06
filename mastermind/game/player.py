# The player class gets the names of each player and stores them.
class Player:
    """
    """
    def __init__(self, name):
        """
        """
        self._name = name
        self._guess = None
        
    def get_guess(self):
        """
        """
        return self._guess

    def get_name(self):
        """
        """
        return self._name

    def set_guess(self, guess):
        """
        """
        self._guess = guess
