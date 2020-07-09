from .thrower_dragon import ThrowerDragon
from utils import apply_effect, make_slow


class SlowThrower(ThrowerDragon):
    """ThrowerDragon that causes Slow on Terminators."""

    name = 'Slow'
    # BEGIN 4.4
    food_cost=4
    implemented = True  # Change to True to view in the GUI

    # END 4.4
    def __init__(self,armor=1):
        ThrowerDragon.__init__(self,armor)

    def throw_at(self, target):
        if target is not None:
            if(target.is_slow<=3):
                target.is_slow+=3
                apply_effect(make_slow, target, 3)
