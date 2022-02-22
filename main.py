from utils.game import Board, UnoBoard
from utils.player import Player
from utils.card import Deck, Card

players = []
deck = Deck()
game = None

name = input("Please insert your name: ")
players.append(Player(name, Deck()))

answer = input("Would you like to add another player? (y/n)")[0]

while answer.lower() != "n":

    name = input("Please insert their name: ")
    players.append(Player(name, Deck()))

    answer = input("Would you like to add another player? (y/n)")[0]


game_input = input("Which game do you want to play? (standard or uno) ")

if game_input.lower() != "standard" and game_input.lower() != "uno":

    print("Game not recognised, picking standard game by default")

    deck.fill_deck_default()

    game = Board(players, deck)

else:

    game = UnoBoard(players)


game.start_game()
