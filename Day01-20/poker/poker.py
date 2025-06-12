from card import Card
from suite import Suite
import random


class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]

    def  shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        return self.cards.pop()


if __name__ == '__main__':
    porker = Poker()
    porker.shuffle()
    i = 1
    while len(porker.cards) > 0:
        print(f"{i} 张牌: {porker.deal()}")
        i += 1

