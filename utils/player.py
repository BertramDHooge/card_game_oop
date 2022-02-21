from utils.card import Card
from typing import List
from random import choice, shuffle
from itertools import islice

class Player:

    def __init__(self, name: str, cards: List[Card]):
        self.name = name
        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self):
        random_card = choice(self.cards)
        self.cards.remove(random_card)
        self.history.append(random_card)
        self.turn_count += 1

        print(f"{self.name} {self.turn_count} played {random_card}")
        return random_card

    def __str__(self):
        return f"{self.name} with {len(self.cards)} cards in hand and {len(self.history)} cards played"

class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        self.cards = [Card(color, icon, value) for (color, icon) in [("black","♣"), ("black", "♠"), ("red", "♥"), ("red", "♦")] for value in["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
    def shuffle(self):
         shuffle(self.cards)

    def distribute(self, players: List[Player]):
        for index in range(len(players)):
            players[index].cards = list(islice(self.cards, index * (len(self.cards) // len(players)), (index + 1) * (len(self.cards) // len(players))))
    
    def __str__(self):
        return f"A deck of {len(self.cards)} cards"
