from utils.player import Player
from typing import List
from utils.card import Deck, Card, UnoCard
from random import shuffle, choice

class Board:
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
            self.players[index].hand.cards = decks[str(index)]

        self.history_cards = decks["deck"]

        while len(self.players[0].hand.cards) > 0:
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


class UnoBoard(Board):
    def __init__(self, players: List[Player]):
        self.active_card = None
        self.order = 1
        self.deck = Deck()


        self.deck.cards = [
            UnoCard(card.card_type, card.value)
            for card in Deck.create_deck(
                ["red", "green", "yellow", "blue"],
                [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "+2",
                    "Reverse turn order",
                    "Skip turn",
                ],
                [Card("Special", "+4"), Card("Special", "Change color")],
            )
        ]
        super().__init__(players, deck)

    def start_game(self):

        decks = self.deck.distribute(len(self.players), 7)
        shuffle(self.players)
        active_player = 0

        for index in range(len(self.players)):
            self.players[index].hand.cards = decks[str(index)]

        while True:
            player = self.players[active_player]
            legal_plays = [card for card in player.hand.cards if card.is_legal_play(self.active_card)]
            if player.is_ai and legal_plays != []:
                self.active_card = player.play(choice(legal_plays))

        while len(self.players[0].hand.cards) > 0:
            self.history_cards += self.active_cards
            self.active_cards = []
            self.turn_count += 1

            for current_player in self.players:
                self.active_cards.append(current_player.play())

            print(self)


