"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


from __future__ import print_function, division

from Card import Hand, Deck  # import classes and their methods


class PokerHand(Hand):  # Create sub class of hand (sub sub class of deck)
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}  # Create an empty dictionary
        for card in self.cards:  # For each card in the poker hand
            # add 1 to the number of cards in the suit
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}  # Create an empty dictionary
        for card in self.cards:  # For each card in the poker hand
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        # print(self.ranks)

    def classify(self):
        self.label = None
        if self.has_straight_flush():
            self.label = 8
        elif self.has_four_of_a_kind():
            self.label = 7
        elif self.has_full_house():
            self.label = 6
        elif self.has_flush():
            self.label = 5
        elif self.has_straight():
            self.label = 4
        elif self.has_three_of_a_kind():
            self.label = 3
        elif self.has_two_pair():
            self.label = 2
        elif self.has_pair():
            self.label = 1
        else:
            self.label = 0
        return self.label

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():  # for each suit
            if val >= 5:  # check if 5 cards are from the same suit
                return True
        return False

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise."""
        self.rank_hist()
        sorted_ranks = sorted(self.ranks.keys())
        for j in range(len(sorted_ranks) - 4):
            return (sorted_ranks[j + 4] == sorted_ranks[j] + 4
                    or sorted_ranks[0] == 1 and sorted_ranks[-4] == 10)  # Straight from 10 to Ace

    def has_straight_flush(self):
        """Returns True if the hand has a straight, False otherwise."""
        if self.has_flush() and self.has_straight():
            # create hands for each suit and check if there is a straight
            spades = PokerHand()
            clubs = PokerHand()
            hearts = PokerHand()
            diamonds = PokerHand()
            for card in self.cards:
                if card.suit == 0:
                    clubs.cards.append(card)
                elif card.suit == 1:
                    diamonds.cards.append(card)
                elif card.suit == 2:
                    hearts.cards.append(card)
                else:
                    spades.cards.append(card)
            if (clubs.has_straight()
                    or diamonds.has_straight()
                    or hearts.has_straight()
                    or spades.has_straight()):
                return True
        return False

    def has_pair(self):
        """Return True if the hand has at least one pair, False otherwise."""
        self.rank_hist()
        for val in self.ranks.values():  # for each rank
            if val >= 2:  # check if 2 cards are from the same rank
                return True
        return False

    def has_two_pair(self):
        """Return True if the hand has at least two pairs, False otherwise."""
        self.rank_hist()
        count_pairs = 0
        for val in self.ranks.values():  # for each rank
            if val >= 2:  # check if 2 cards are from the same rank
                count_pairs += 1
        return count_pairs >= 2

    def has_three_of_a_kind(self):
        """Return True if the hand has at least one pair, False otherwise."""
        self.rank_hist()
        for val in self.ranks.values():  # for each rank
            if val >= 3:  # check if 2 cards are from the same rank
                return True
        return False

    def has_four_of_a_kind(self):
        """Return True if the hand has at least one pair, False otherwise."""
        self.rank_hist()
        for val in self.ranks.values():  # for each rank
            if val >= 4:  # check if 2 cards are from the same rank
                return True
        return False

    def has_full_house(self):
        """Return True if the hand has at least one pair, False otherwise."""
        self.rank_hist()
        return self.has_two_pair() and self.has_three_of_a_kind()


def print_probabilities(d_hand_values, n):
    print('Probabilities of poker hands\n')
    row_format = "{:>15}" * 2
    print(row_format.format('Hands', '5 cards'))
    print('-' * 30)
    for item in d_hand_values:
        # print(item, d_hand_values[item][0], d_hand_values[item][1])
        print(row_format.format(d_hand_values[item][0],
                                d_hand_values[item][1] / n))


def create_hands(d_hand_values, n):
    for i in range(n):
        deck = Deck()  # Create a sorted deck
        deck.shuffle()  # shuffle the deckhand = PokerHand()
        hand = PokerHand()  # create a new hand
        deck.move_cards(hand, 5)  # give cards from the deck to the hand
        hand_value = hand.classify()
        d_hand_values[hand_value][1] += 1


def estimate_hands_probabilities():
    n = 100
    d_hand_values = dict()
    hand_values = [
        "high card",
        "pair",
        "two pair",
        "three-of-a-kind",
        "straight", "flush",
        "full house",
        "four-of-a-kind",
        "straight flush"]
    for i in range(len(hand_values)):
        d_hand_values[i] = [hand_values[i], 0]

    create_hands(d_hand_values, n)

    print_probabilities(d_hand_values, n)


if __name__ == '__main__':
    estimate_hands_probabilities()
