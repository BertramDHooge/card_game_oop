from utils.game import Board
from utils.player import Player


amanda = Player("Amanda", [])
jeff = Player("Jeff", [])
nathan = Player("Nathan", [])
berkley = Player("Berkley", [])

game = Board([amanda, jeff, nathan, berkley])

game.start_game()
