# python script to test the deck class
import unittest
from deck_of_cards import Deck
 
class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
 
    def test_deck_has_52_cards(self):
        self.assertEqual(len(self.deck.deck), 52)
 
    def test_deal_card(self):
        self.assertEqual(self.deck.deal_card(), 'King of Spades')
        self.assertEqual(len(self.deck.deck), 51)
 
    def test_reset(self):
        self.deck.reset()
        self.assertEqual(len(self.deck.deck), 52)
 
    def test_shuffle(self):
        self.deck.shuffle()
        self.assertEqual(len(self.deck.deck), 52)
        self.assertEqual(self.deck.deal_card(), 'King of Spades')

if __name__ == '__main__':
    unittest.main()
    