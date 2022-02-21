from utils.player import Player
from typing import List
from utils.player import Deck

class Board():

    def __init__(self, players: List[Player]):
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        deck = Deck()
        deck.fill_deck()
        deck.distribute(self.players)

        while len(self.players[0].cards) > 0:
            self.history_cards += self.active_cards
            self.active_cards = []
            self.turn_count += 1

            for current_player in self.players:
                self.active_cards.append(current_player.play())

            print(self)

    def __str__(self):
        return f"Turn {self.turn_count}: currently {[card.__str__() for card in self.active_cards]} are in the game and {len(self.history_cards)} cards have been played in earlier turns\n"
