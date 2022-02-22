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
        :param cards: A list of Cards our Player currently has acces to
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
