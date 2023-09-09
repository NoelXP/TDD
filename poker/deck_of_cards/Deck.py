class Deck:
    def __init__(self):
        """
        Initializes a deck of 52 cards.
        """
        self.deck = []
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(rank + ' of ' + suit)


    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.deck)
      
    def deal_card(self):
        """
        Deals a single card from the deck.
        Returns:
            str: The top card from the deck.
        """
        if len(self.deck) == 0:
            return "No cards left in the deck."
        return self.deck.pop()
      
    def reset(self):
        """
        Resets the deck by recreating it.
        """
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(rank + ' of ' + suits)