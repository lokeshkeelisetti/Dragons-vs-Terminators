from . import ThrowerDragon
class ScubaThrower(ThrowerDragon):
    
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    is_watersafe=True
    food_cost=6
    name="Scuba"
    implemented=True

    def __init__(self,armor=1):
        ThrowerDragon.__init__(self,armor)

        
