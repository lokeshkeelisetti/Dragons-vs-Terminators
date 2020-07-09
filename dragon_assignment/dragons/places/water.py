from . import Place


class Water(Place):
    """Water is a place that can only hold watersafe fighters."""

    def add_fighter(self, fighter):
        Place.add_fighter(self,fighter)
        if not fighter.is_watersafe:
            fighter.reduce_armor(fighter.armor)
        
        """Add a Fighter to this place. If the fighter is not watersafe, reduce
        its armor to 0."""
        # BEGIN 4.1
        "*** YOUR CODE HERE ***"
