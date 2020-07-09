from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from utils import terminators_win

class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""
    
    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    food_cost=7
    implemented = True  # Change to True to view in the GUI
    instantiated=False
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        ScubaThrower.__init__(self,armor)
        if not DragonKing.instantiated:
            DragonKing.instantiated=True
            self.Trueking=True
        else:
            self.Trueking=False
        "*** YOUR CODE HERE ***"
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        if self.Trueking:
            ScubaThrower.action(self,colony)
            k=self.place.exit
            while k is not None:
                if k.dragon is not None:
                    if not k.dragon.buffed:
                        k.dragon.damage*=2
                        k.dragon.buffed=True
                    if k.dragon.is_container and k.dragon.contained_dragon is not None and not k.dragon.contained_dragon.buffed:
                        k.dragon.contained_dragon.damage*=2
                        #print(k.dragon.buffed)
                        k.dragon.contained_dragon.buffed=True
                k=k.exit
        else:
            self.reduce_armor(self.armor)
                        
        
        "*** YOUR CODE HERE ***"
        # END 4.3

    def reduce_armor(self, amount):
        ScubaThrower.reduce_armor(self,amount)
        if self.Trueking and self.armor<=0:
            terminators_win()
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
