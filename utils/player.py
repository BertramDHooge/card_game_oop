from utils.card import Card, Deck


class Player:
    """
    Class that describes a Player
    """

    def __init__(self, name: str, hand: Deck):
        """
        Function that will initialise a new instance of Person

        :param name: The name of our Player
        :param hand: The Deck of Cards our Player has access to
        """

        self.name = name
        self.hand = hand
        self.legal_plays = Deck(hand.cards)
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

        card = self.legal_plays.draw()

        self.hand.cards.remove(card)

        self.history.append(card)
        self.turn_count += 1

        print(f"{self.name} on turn {self.turn_count} played {card}")
        return card

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Player.

        :return: A str that will represent our Player. Displaying their name,
                    amount of cards in their hand, and amount of cards played so far.
        """

        return f"{self.name} with {len(self.hand.cards)} cards in hand and {len(self.history)} cards played"


class ControlledPlayer(Player):
    def __init__(self, name: str, hand: Deck):
        super().__init__(name, hand)

    def play(self) -> Card:
        print("Your turn! Please select a legal card to play, otherwise, draw a card")
        print("Your hand: ")
        print([card.__str__() for card in self.hand.cards])
        print("Choose one of these cards to play:")
        for index in range(len(self.legal_plays.cards)):
            print(f"{index + 1}) {self.legal_plays.cards[index]}")

        # As seen on https://stackoverflow.com/questions/27993962/how-to-check-user-input-python
        while True:
            inp = input("Choose a card: ")
            try:
                choice = self.legal_plays.cards[int(inp) - 1]  # try cast to int
                self.hand.cards.remove(choice)
                return choice
            except:
                # if we get here user entered invalid input so print message and ask again
                print("{} is not a valid option".format(inp))
                continue
