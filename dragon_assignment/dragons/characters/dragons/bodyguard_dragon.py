from .dragon import Dragon


class BodyguardDragon(Dragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    food_cost=4
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.2
    implemented = True
    is_container=True
    damage=0
    # Change to True to view in the GUI

    def __init__(self, armor=2):
        Dragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard

    def can_contain(self, other):
        # BEGIN 3.2
        if self.contained_dragon==None:
            if not other.is_container:
                return True
            else:
                return False
        return False
                
        "*** YOUR CODE HERE ***"
        # END 3.2

    def contain_dragon(self, dragon):
        # BEGIN 3.2
        self.contained_dragon=dragon
        "*** YOUR CODE HERE ***"
        # END 3.2

    def action(self, colony):
        # BEGIN 3.2
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
        "*** YOUR CODE HERE ***"
        # END 3.2
