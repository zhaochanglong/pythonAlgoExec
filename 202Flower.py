#! /usr/bin/env python
#import unittest

class Flower:
    """Flower"""
    def __init__(self, name, huaban_num, price):
        self._name = name
        self._huaban_num = huaban_num
        self._price = price

    def get_flower_info(self,name, huaban_num, price):
        self._name = name
        self._huaban_num = huaban_num
        self._price = price

    def update_flower_info(self,name, huaban_num, price):
        self._name = name
        self._huaban_num = huaban_num
        self._price = price

    def get_flower_name(self):
        return self._name

#if __name__ == '__main__':
peachflow = Flower("peach", 5, 0)
print(peachflow.get_flower_name())
    #unittest.main()
