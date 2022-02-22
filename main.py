from utils.game import Board
from utils.player import Player
from utils.card import Deck

players = []

answer = input("Please insert your name: ")
players.append(Player(answer, []))

answer = input("Which game do you want to play? (standard or uno) ")

if answer.lower() != "standard" and answer.lower() != "uno":
    answer = "std"
    print("Game not recognised, picking standard game by default")

deck = Deck()
deck.fill_deck_default(answer)

answer = input("Would you like to add another player? (y/n)")[0]

while answer.lower() != "n":

    answer = input("Please insert their name: ")

    players.append(Player(answer, []))

    answer = input("Would you like to add another player? (y/n)")[0]

game = Board(players, deck)

game.start_game()
