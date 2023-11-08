'''
Project Name: Potion Class
File Name: potion.py, test_potion.py
Author: Sharon Colson
Updated: 11/08/2023
Purpose: Build Class for Potions using UnitTest
'''

# Libraries
import random

# Create class of Potion
class Potion:
    # Initial attributes received
    def __init__(self, ingredient1, ingredient2):
        self.__ingredient1 = ingredient1
        self.__ingredient2 = ingredient2

        self.__name = self.set_name()
        self.__value = self.set_value()

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def set_name(self):
        if(self.__ingredient1,self.__ingredient2) in [("Milk","Marinara Sauce"),("Marinara Sauce", "Milk")]:
            return "Potion of Regret"
        elif(self.__ingredient1,self.__ingredient2) in [("Adder's Fork","Elephant's Proboscis"),("Elephant's Proboscis", "Adder's Fork")]:
            return "Draught of Eavesdropping"
        elif(self.__ingredient1,self.__ingredient2) in [("Vampire's Breath","Witch's Tongue"),("Witch's Tongue", "Vampire's Breath")]:
            return "Elixir of Halitosis"
        elif(self.__ingredient1,self.__ingredient2) in [("Toe of Frog","Eye of Newt"),("Eye of Newt", "Toe of Frog")]:
            return "Philter of Amphibiosity"
        elif(self.__ingredient1==self.__ingredient2):
            return "Failed Decoction"
        else:
            return "Failed Decoction"
    
    # Function to generate random value between (low amount, high amount)
    def set_value(self):
        if self.__name == "Elixir of Halitosis":
            return random.randint(10,50)
        elif self.__name == "Philter of Amphibiosity":
            return random.randint(750,1000)
        elif self.__name == "Draught of Eavesdropping":
            return random.randint(500,750)
        elif self.__name == "Potion of Regret":
            return random.randint(2,40)
        else:
            return 1