'''
Project Name: Potion Class
File Name: potion.py, test_potion.py
Author: Sharon Colson
Updated: 11/08/2023
Purpose: Build Class for Potions using UnitTest
'''

import random

class Potion:
    def __init__(self, ingredient1, ingredient2):
        self.__ingredient1 = ingredient1
        self.__ingredient2 = ingredient2

        # Uses internal method to get the potion name
        self.__name = self._get_potion_name()
        self.__name = self._get_potion_value()

    def get_name(self):
        return self.__name
    
    def get_value(self):
        return self.__value
    
    # Uses conditional to determine name of potion
    # Leading underscore indicates that this 
    # should be used as an internal method
    # It doesn't prohibit external use though
    def _get_potion_name(self):
        # if (self.__ingredient1 == self.__ingredient2):
        #     return "Failed Decoction"
        if(self.__ingredient1,self.__ingredient2) in [("Milk","Marinara Sauce"),("Marinara Sauce", "Milk")]:
            return "Potion of Regret"
        else:
            return "Failed Decoction"
    def _get_potion_value(self):
        return "Fix me"