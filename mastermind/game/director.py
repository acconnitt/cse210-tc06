# The director handles the playing of the game and calls the other classes together.
from game.code import Code
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:

    def __init__(self):
        self.code = Code()
        self.guess = Guess(self.code.get_code())
        self.roster = Roster()
        self.console = Console()
        self.keep_playing = True

    def start_game(self):
        self.prepare_game()
        self.roster.next_player()
        while self.keep_playing:
            self.process_round()
            self.console.print_turn(self.roster.get_current())
            self.get_player_guess()
            if self.roster.get_current().get_guess() == self.guess.get_code():
                print()
                self.console.print_win(self.roster.get_current())

    def process_round(self):
        print()
        self.console.print_blank_line()
        self.console.print_player(self.roster.get_current())
        self.roster.next_player()
        self.console.print_player(self.roster.get_current())
        self.console.print_blank_line()
        self.roster.next_player()

    def get_player_guess(self):
        self.roster.get_current().set_guess(input("What is your guess? "))
        self.guess.check_guess()

    def prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

            Args:
                self (Director): An instance of Director.
        """

        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self.roster.add_player(player)
