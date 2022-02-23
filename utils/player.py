from utils.card import Card, Deck
from typing import List
from random import choice, shuffle
from itertools import islice


class Player:
    """
    Class that describes a Player
    """

    def __init__(self, name: str, hand: Deck, is_ai=True):
        """
        Function that will initialise a new instance of Person

        :param name: The name of our Player
        :param hand: The Deck of Cards our Player has access to
        """

        self.name = name
        self.hand = hand
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.is_ai = is_ai

    def play(self, card: Card = None) -> Card:
        """
        Function that will play a random card from cards. This will also remove
        this card from cards while adding it to history and print a small
        descriptive text detailing what happened to the console

        :return: The card that was just played
        """

        if card is None or card not in self.hand.cards:
            card = self.hand.draw()
        else:
            self.hand.cards.remove(card)

        self.history.append(card)
        self.turn_count += 1

        print(f"{self.name} {self.turn_count} played {card}")
        return card

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Player.

        :return: A str that will represent our Player. Displaying their name,
                    amount of cards in their hand, and amount of cards played so far.
        """

        return f"{self.name} with {len(self.hand.cards)} cards in hand and {len(self.history)} cards played"
