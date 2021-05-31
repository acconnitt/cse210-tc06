# The director handles the playing of the game and calls the other classes together.
from game.code import Code
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:
    """The responsibility of this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        roster (Roster): An instance of the class of objects known as Roster.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue. 
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.roster = Roster() # Calls the Roster class
        self.console = Console() # Calls the Console Class
        self.keep_playing = True # Keep playing while is true
        self.win = False # Starts as false while player hasn't won

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self.prepare_game() # Calls the prepare_game method
        self.roster.next_player() # Calls next_player method from Roster class
        while self.keep_playing:
            print()
            self._get_inputs()
            self._do_updates()
            self.roster.next_player()

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Director): An instance of Director.
        """
        player = self.roster.get_current()
        self.console.print_blank_line()
        self.console.print_players(self.roster)
        self.console.print_blank_line()
        self.console.print_turn(player)

        valid_guess = False
        """Ask for player guess 
        Also checks if player imput is valid
        """
        while not valid_guess:
            guess = input("What is your guess? ")
            for i in guess:
                if i.isalpha():
                    print(
                        "Your guess was invalid because it contained letters, please try again. ")
                    break
            if len(guess) != 4:
                print(
                    "Your guess was invalid because it wasn't 4 characters long, please try again.")
            else:
                valid_guess = True

        player.guess.set_guess(guess)
        player.guess.check_guess()
        self.win = player.guess.check_win()

    def _do_updates(self):
        """Check if game is player won the game

        Args:
            self (Director): An instance of Director.
        """
        if self.win:
            self.console.print_win(self.roster.get_current())
            self.keep_playing = False
        elif not self.win:
            pass

    def prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director.
        """
        code = Code() #Calls the Code class
        the_code = code.get_code() #Calls the get_code method from Code class
        # Loop twice to get two players name, guess and code
        for n in range(2): 
            name = input(f"Enter a name for player {n + 1}: ")
            guess = Guess(the_code)
            player = Player(name, guess, code)
            self.roster.add_player(player)
