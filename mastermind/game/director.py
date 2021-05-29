# The director handles the playing of the game and calls the other classes together.
from game.code import Code
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:

    def __init__(self):
        self.roster = Roster()
        self.console = Console()
        self.keep_playing = True

    def start_game(self):
        self.prepare_game()
        while self.keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _get_inputs(self):
        player = self.roster.get_current()
        code = player.code.get_code()

        self.console.print_blank_line()
        self.console.print_players(self.roster)
        self.console.print_blank_line()

        
        self.console.print_turn(player)
        guess = input("What is your guess? ")
        player.guess.set_guess(guess)
        player.guess.check_guess()
        

    def _do_updates(self):
        pass

    def _do_outputs(self):
        self.roster.next_player()
        
        

    def prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

            Args:
                self (Director): An instance of Director.
        """

        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            code = Code()
            guess = Guess(code.get_code())
            player = Player(name, guess, code)
            self.roster.add_player(player)



