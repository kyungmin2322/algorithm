# -*- coding: utf-8 -*-
"""bidirectnode

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nvqQDPzTXKaFfKr6pymASfh1XYeJw2Dh
"""

class BidirectNode :
    def __init__(self, x, prevNode : 'BidirectNode', nextNode : 'BidirectNode') :
        self.item = x
        self.prev = prevNode
        self.next = nextNode