from .bodyguard_dragon import BodyguardDragon
from utils import random_or_none

class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    food_cost=6
    # OVERRIDE CLASS ATTRIBUTES HERE
    def __init__(self,armor=2):
        BodyguardDragon.__init__(self,armor)
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI

    # END 3.3

    def action(self, colony):
        k=(self.place.terminators).copy()
        for i in k:
            i.reduce_armor(self.damage)
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
