from poker import Poker


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()


if __name__ == '__main__':

    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    # 将牌轮流发到每个玩家手上每人13张牌
    for _ in range(13):
        for player in players:
            player.get_one(poker.deal())
    # 玩家整理手上的牌输出名字和手牌
    for player in players:
        player.arrange()
        print(f'{player.name}: ', end='')
        print(player.cards)
