from .thrower_dragon import ThrowerDragon
from utils import apply_effect,make_scare

class ScaryThrower(ThrowerDragon):
    """ThrowerDragon that intimidates Terminators, making them back away instead of advancing."""

    name = 'Scary'
    # BEGIN 4.4
    food_cost=6
    implemented = True  # Change to True to view in the GUI

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self,armor)
    # END 4.4

    def throw_at(self, target):
        if target is not None:
            if not target.is_scared:
                target.is_scared=True
                target.is_backward=2
                apply_effect(make_scare,target,2)
        # BEGIN 4.4
        "*** YOUR CODE HERE ***"
        # END 4.4
