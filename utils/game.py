from utils.player import Player
from typing import List
from utils.card import Deck

class Board():
    """
    Class that describes a (game)board upon which a game can be played.
    """

    def __init__(self, players: List[Player], deck: Deck = Deck()):
        """
        Function that will initialise a new instance of Board.

        :param players: a list of players that will be playing at our Board
        """

        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        self.deck = deck

    def start_game(self):
        """
        Function that will start the game that we will be playing at our Board.
        """

        if self.deck.cards == []:
            self.deck.fill_deck_default()

        decks = self.deck.distribute(len(self.players))

        for index in range(len(self.players)):
            self.players[index].cards = decks[str(index)]

        self.history_cards = decks["deck"]

        while len(self.players[0].cards) > 0:
            self.history_cards += self.active_cards
            self.active_cards = []
            self.turn_count += 1

            for current_player in self.players:
                self.active_cards.append(current_player.play())

            print(self)

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Board.

        :return: A str that will represent our current Board-state. Displaying
                    the current turn, what Cards are currently in play and how many Cards
                    have been played during the current game
        """

        return f"Turn {self.turn_count}: currently {[card.__str__() for card in self.active_cards]} are in the game and {len(self.history_cards)} cards have been played in earlier turns\n"
