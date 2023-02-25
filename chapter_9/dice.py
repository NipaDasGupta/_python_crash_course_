"""A class that can be used to represent a dice game."""
from random import randint


class Die:
    """A simple attempt to represent a die."""

    def __init__(self, sides=6):
        """Initialize attributes to describe a dice game."""
        self.sides = sides

    def type_of_dice(self, dice):
        """Choose a 6, 10 or 20 sided dice before rolling over."""
        self.sides = dice
        print(f"You have choosen a {dice}-sided dice!")

    def roll_die(self):
        """Prints a statement showing which sides the dice rolled over."""
        dice_rolled = randint(1, self.sides)

        # Change the ordinals of the rolled dice
        if dice_rolled == 1:
            side = 'st'
        elif dice_rolled == 2:
            side = 'nd'
        elif dice_rolled == 3:
            side = 'rd'
        else:
            side = 'th'

        print(f"Dice rolled over on {dice_rolled}{side} side.")
