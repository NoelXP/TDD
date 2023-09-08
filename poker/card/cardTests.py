# cardTests.py python script to test the card class using 
# unittest module
import unittest
from Card import Card



# Test cases to test Card methods
# You always create a child class derived from unittest. TestCase 
class TestCard(unittest.TestCase):



# setUp method is overridden from the parent class TestCase 
    def setUp(self):
      self.card = Card()

# Each test method starts with the keyword test_
    def test_getSuit(self):
        self.assertEqual(self.card.getSuit(), 'Spades')
         
    def test_getRank(self):
        self.assertEqual(self.card.getRank(), 'Ace')
    
    def test_str(self):
        self.assertEqual(self.card.__str__(), 'Ace of Spades')

    def test_repr(self):
        self.assertEqual(self.card.__repr__(), 'Ace of Spades')

    def test_eq(self):
        self.assertEqual(self.card.__eq__(Card('Spades','Ace')), True)

    def test_lt(self):
        self.assertEqual(self.card.__lt__(Card('Spades','Ace')), False)

    def test_hash(self):
        self.assertEqual(self.card.__hash__(), 0)
