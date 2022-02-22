from utils.card import Card
from typing import List
from random import choice, shuffle
from itertools import islice


class Player:
    """
    Class that describes a Player
    """

    def __init__(self, name: str, cards: List[Card]):
        """
        Function that will initialise a new instance of Person

        :param name: The name of our Player
        :param cards: A list of Cards our Player currently has access to
        """

        self.name = name
        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self) -> Card:
        """
        Function that will play a random card from cards. This will also remove
        this card from cards while adding it to history and print a small
        descriptive text detailing what happened to the console

        :return: The card that was just played
        """

        random_card = choice(self.cards)
        self.cards.remove(random_card)
        self.history.append(random_card)
        self.turn_count += 1

        print(f"{self.name} {self.turn_count} played {random_card}")
        return random_card

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Player.

        :return: A str that will represent our Player. Displaying their name,
                    amount of cards in their hand, and amount of cards played so far.
        """

        return f"{self.name} with {len(self.cards)} cards in hand and {len(self.history)} cards played"


class Deck:
    """
    Class that describes a Deck of Cards
    """

    def __init__(self):
        """
        Function that will initialise a new instance of Deck. A Deck will
        allways be initialised with an empty list of Cards
        """

        self.cards = []

    def fill_deck(self):
        """
        Function that will fill the current deck with a standard list of Cards.
        """

        self.cards = [
            Card(color, icon, value)
            for (color, icon) in [
                ("black", "♣"),
                ("black", "♠"),
                ("red", "♥"),
                ("red", "♦"),
            ]
            for value in [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]
        ]

    def shuffle(self):
        """
        Function that will shuffle the Cards of the current Deck.
        """

        shuffle(self.cards)

    def distribute(self, players: List[Player]):
        """
        Function that will distribute the current Deck of Cards over

        :param players: A list of Player to whom we need to ditribute the cards.
        """

        for index in range(len(players)):
            players[index].cards = list(
                islice(
                    self.cards,
                    index * (len(self.cards) // len(players)),
                    (index + 1) * (len(self.cards) // len(players)),
                )
            )

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Deck.

        :return: A str representing our Deck. Displaying the amount of cards in
        the Deck
        """

        return f"A deck of {len(self.cards)} cards"
