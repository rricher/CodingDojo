import random

class Card:
    def __init__(self, suit, val):
        self.suitVal = suit
        self.cardVal = val
        self.suits = {1 : "Club", 2 : "Diamond", 3 : "Heart", 4 : "Spade"}
        self.pip = {1 : "Ace", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6: "Six", 7 : "Seven", 8 : "Seven", 9 : "Nine", 10 : "Ten", 11 : "Jack", 12 : "Queen", 13 : "King"}

    def __str__(self):
        return f"{self.pip[self.cardVal]} of {self.suits[self.suitVal]}s"

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.cards.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.cards)
        return self
    
    def printDeck(self):
        for i in self.cards:
            print(i)

newdeck = Deck()
newdeck.shuffle()
newdeck.printDeck()