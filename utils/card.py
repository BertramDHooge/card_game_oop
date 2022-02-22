from itertools import islice
from typing import List
from random import shuffle


class Card:
    """
    Class that describes a Card.
    """

    def __init__(self, card_type: str, value: str):
        """
        Function that will initialise a new instance of a Card, which consists
        of a card type and a value.

        :param card_type: The icon for the Card, for example one of [♥, ♦, ♣, ♠] or a color
        :param value: The value of the Card, for example one of [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
        """

        self.value = value
        self.card_type = card_type

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Card.

        :return: A str representing our Card, printing both the card type and
        value of the Card.
        """
        return f"{self.value} of {self.card_type}"

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
                    List[str], additionally: List[Card] = []) -> List[Card]:
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

        :return: The resulting deck of cards created by combining both attributes and
        adding the additional cards represented as a list of cards.
        """

        deck = [Card(icon, value) for icon in first_card_attribute
                                        for value in second_card_attribute]
        deck += additionally

        return deck





    def fill_deck_default(self, decktype: str = ""):
        """
        Function that will fill the current deck with a standard list of Cards.

        :param decktype: The type of default deck you want to generate.
                            Currently supported:
                                - standard 52 card deck ('std', 'standard' or no value),
                                - Uno ('uno')
        """

        if decktype == "" or decktype.lower() == "std" or decktype.lower() == "standard":
            self.cards = Deck.create_deck(["♣", "♠", "♥", "♦"],
                                          ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

        elif decktype.lower() == "uno":
            self.cards = Deck.create_deck(["red", "green", "yellow", "blue"],
                                         ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "Reverse turn order", "Skip turn"],
                                         [Card("Special", "+4"), Card("Special", "Change color")])



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
        index, allowing looping using a range, with any spare cards being
        stored in 'deck'
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
