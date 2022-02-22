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

    @classmethod
    def create_deck(cls, first_card_attribute: List[str], second_card_attribute:
                    List[str], additionally: List[Card] = []) -> 'Deck':
        """
        Class method that creates a deck of cards from 2 lists of attributes
        and adds any additional cards specified, either to generate duplicates
        or to be able to use custom cards that can't be built from the basic
        attributes.

        :param first_card_attribute: The first attribute of the card, usually a
        color or icon.
        :param second_card_attribute: The second attribute of the card usually
        a number or similar.
        :param additionally: A list of additional cards to also be added to the
        deck, allowing the usage of custom cards, or adding duplicates as the
        base deck creation will generate 1 card per possible combination of
        first_card_attribute and second_card_attribute.

        :return: The resulting deck created by combining both attributes and
        adding the additional cards.
        """

        deck = Deck()
        deck.cards = [Card(icon, value) for icon in first_card_attribute
                                        for value in second_card_attribute]
        deck.cards += additionally

        return deck





    def fill_deck(self):
        """
        Function that will fill the current deck with a standard list of Cards.
        """

        self.cards = [Card(color, icon, value) for (color, icon) in [("black","♣"), ("black", "♠"), ("red", "♥"), ("red", "♦")] for value in["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self):
        """
        Function that will shuffle the Cards of the current Deck.
        """

        shuffle(self.cards)

    def distribute(self, amount_of_players: int, max_cards_per_player: int =
                   -1) -> dict[str, List[Card]]:
        """
        Function that will distribute the current Deck of Cards among a
        specified amount of players. Either dividing equally untill the deck
        runs out or untill the specified max amount of cards is reached per
        player. Any spare cards are stored in Deck.

        :param amount_of_players: The number of players we need to distribute
        cards to.
        :param max_cards_per_player: The max amount of cards to ditribute to a
        player, if negative, the entire deck will be dealt to the players.

        :return: A dictionary containing the different lists of cards and an
        index, allowing looping using a range, with any spare cards being stored in deck
        """

        if max_cards_per_player < 0:
            max_cards_per_player = len(self.cards) // amount_of_players

        divided = {str(player): list(islice(self.cards,
                                       player * max_cards_per_player,
                                       (player+1) * max_cards_per_player))
                   for player in range(amount_of_players)}

        divided["deck"] = list(islice(self.cards,
                                      len(self.cards) - max_cards_per_player * amount_of_players
                                      ))

        return divided

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Deck.

        :return: A str representing our Deck. Displaying the amount of cards in
        the Deck
        """

        return f"A deck of {len(self.cards)} cards"
