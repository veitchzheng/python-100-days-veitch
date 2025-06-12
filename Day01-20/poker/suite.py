from enum import Enum


class Suite(Enum):
    """花色(枚举)   黑桃，红桃，草花，方块"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
