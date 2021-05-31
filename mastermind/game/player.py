
class Player:
    """ The player class gets the names of each player and stores them.
    """

    def __init__(self, name):
        self._name = name
        self._guess = "----"
        self._hint = "****"

    def get_guess(self):
        return self._guess # Returns guess

    def get_name(self):
        return self._name # Returns name

    def set_guess(self, guess):
        self._guess = guess # Set new guess

    def set_hint(self, hint):
        self._hint = hint # Set new hint

    def get_hint(self):
        return self._hint # Returns hint
