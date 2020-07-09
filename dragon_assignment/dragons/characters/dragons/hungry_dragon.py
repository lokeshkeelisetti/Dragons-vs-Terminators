from .dragon import Dragon
from utils import random_or_none

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    food_cost=4
    time_to_digest=3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    implemented = True  # Change to True to view in the GUI

    # END 2.3

    def __init__(self, armor=1):
        # BEGIN 2.3
        self.digesting=0
        self.armor=armor
        "*** YOUR CODE HERE ***"
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        terminator.reduce_armor(terminator.armor)
        "*** YOUR CODE HERE ***"
        # END 2.3

    def action(self, colony):
        if self.digesting==0:
            terminator=random_or_none(self.place.terminators)
            if terminator is not None:
                self.eat_terminator(terminator)
                self.digesting=self.time_to_digest
        else:
            self.digesting-=1
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
