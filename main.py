import random
 
class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
 
    def display(self):
        return (f"Hello {self.name}! You will be playing as {self.marker}!")
    
class Human(Player):
    def __init__(self, name, marker, name2, marker2):
        super().__init__(name, marker)
        self.name2 = name2
        self.marker2 = marker2
 
    def inquiry(self, marker):
        name2 = input("What is your name, second player?; ")
        if self.marker == "X":
            print(f"Hello {name2}! You will be playing as O's")
            marker2 = "O"
            return name2, marker2
        elif self.marker == "O": 
            print(f"{name2}, you will be playing as X's")
            marker2 = "X"
            return name2, marker2
 
    def display(self):
        return (f"\nHello {self.name} and {self.name2}. {self.name} will play as \
{self.marker} and {self.name2} will play as {self.marker2}")
 
class Computer(Player):
    def __init__ (self, name, marker, name2, marker2):
        super().__init__ (name, marker)
        self.name2 = name2
        self.marker2 = marker2
    
    def inquiry(self, marker):
        robot_names = ["Joe", "Murr", "Sal", "Quinn", "Micheal", "Duncan", "Anfernee", "Larry"]
        name2 = (random.choice(robot_names))
        if self.marker == "X":
            print(f"Hello, I am {name2}, the computer. I'm going to beat you, Tic-Tac-Toe is my jam.")
            print("Sucker! I wanted to be O's anyways! I always win when I am O's")
            marker2 = "O"
            return name2, marker2
        elif self.marker == "O": 
            print(f"Hello, I am {name2}, the computer. I'm' going to beat you, Tic-Tac-Toe is my jam.")
            print("I guess ill take X's if I have to...")
            marker2 = "X"
            return name2, marker2
 
    def display(self):
        return (f"\nHello {self.name} and {self.name2}. {self.name} will play as \
{self.marker} and {self.name2} will play as {self.marker2}")
 
 
class Game:    
    def __init__(self):
        self.board = {
                1: "     ", 2: "     ", 3: "     ",
                4: "     ", 5: "     ", 6: "     ",
                7: "     ", 8: "     ", 9: "     "}
        self.name = name
        self.marker = marker
        self.name2 = name2
        self.marker2 = marker2
 
    @staticmethod
    def starting_spots():
        print('''Original Spot Call-on Legend:
 
      1  |  2  |  3 
    -----------------
      4  |  5  |  6
    -----------------
      7  |  8  |  9  \n''')
 
    def print_board(self):
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3] + "|")
        print("-" * 17)
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6] + "|")
        print("-" * 17)
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9] + "|")
 
    def first_player(self):
        names_list = [self.name, self.name2]
        first = (random.choice(names_list))
        if first == name:
            print(f"{name} gets to go first!")
            first = name
            return name, marker
        elif first == name2:
            print(f"{name2} gets to go first!")
            return name2, marker2
    
    def change_turn(self, player):
        """Changes the player turn.
        Receives a player and returns the other."""
        if player is self.name:
            return self.name2, self.marker2
        else:
            return self.name, self.marker
 
    def is_winner(self, player):
        """Returns True if the player won and False otherwise."""
        if self.board["1"] == player.type and self.board["2"] == player.type and self.board["3"] == player.type or \
        self.board["4"] == player.type and self.board["5"] == player.type and self.board["6"] == player.type or \
        self.board["7"] == player.type and self.board["8"] == player.type and self.board["9"] == player.type or \
        self.board["1"] == player.type and self.board["4"] == player.type and self.board["7"] == player.type or \
        self.board["2"] == player.type and self.board["5"] == player.type and self.board["8"] == player.type or \
        self.board["3"] == player.type and self.board["6"] == player.type and self.board["9"] == player.type or \
        self.board["1"] == player.type and self.board["5"] == player.type and self.board["9"] == player.type or \
        self.board["7"] == player.type and self.board["5"] == player.type and self.board["3"] == player.type:
            return True
        return False
 
    def won_game(self, player):
        """Returns True if the player won the game, False otherwise."""
        return self.is_winner(player)
 
    def test_move(self, position):
        if self.board[position] == "     ":
            return True
        return False
 
    def change_board(self, position, letter):
        """Receive a position and if the player is 'X' or 'O'.
        Checks if the position is valid, modifies the board and returns the modified board.
        Returns None if the move is not valid."""
        if self.test_move(position) == True:
            self.board[position] = letter
            return self.board
        return None
 
    def modify_board(self, position, letter):
        """Receives position and player type ('X' or 'O').
        Returns modified board if position was valid.
        Asks to player try a different position otherwise."""
        if self.change_board(position, letter) is not None:
            return self.change_board(position, letter)
        else:
            position = input("Not available position. Please, try again: ")
            return self.change_board(position, letter)
 
 
 
 
move_nums = [1,2,3,4,5,6,7,8,9]
 
print("WELCOME to Reece's Tic-tac-Toe Game!\n")
name = input("What is your name?; ")
marker = input("Would you like to play as X or O?; ")
player1 = Player(name, marker)
print(Player.display(player1))
game_option = input ("Would you like to play against someone or the computer? (Human, Comp); ").lower()
if game_option == "human" or game_option == "h" or game_option == "person":
    name2, marker2 = (Human.inquiry('player1', marker))
    player2 = Human(name, marker, name2, marker2)
    print(Human.display(player2))
    computer = False
elif game_option == "comp" or game_option =="c" or game_option == "computer":
    name2, marker2 = (Computer.inquiry(player1, marker))
    player2 = Computer(name, marker, name2, marker2)
    print(Computer.display(player2))
    computer = True
 
 
 
first, first_marker =(Game().first_player())
num = 0
player = first
letter = first_marker
while num < 9:
    num=+1
    Game.starting_spots()
    Game().print_board()
    if computer == False and first == name:
        position = input(f"{player}, what would you like your move to be? (1-9); ")
    elif computer == False and first == name2:
        position = (random.choice(move_nums))
        print(f"{player} has chosen {position}")
 
    elif computer == True and first == name:
        position = input(f"{player}, what would you like your move to be? (1-9); ")
    elif computer == True and first == name2:
        position = (random.choice(move_nums))
        print(f"{player} has chosen {position}")
 
    Game.modify_board(position, player, letter)
    if Game().won_game(player) == True:
            print(f"{player} is the Winner!")
            break
    else:
        player, letter = Game().change_turn(player)
if num == 9:
    print("Game over! It's a tie!")

