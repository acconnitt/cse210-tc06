class Console:
    
    def print_blank_line(self):
        #Print blank line
        print("--------------------")

    def print_player(self, player): 
        #Print player's name and the start guess and hint string
        print(f"Player {player.get_name()}: {player.get_guess()}, {player.get_hint()}")

    def print_turn(self,player):
        print(f"{player.get_name}'s turn: ")

    