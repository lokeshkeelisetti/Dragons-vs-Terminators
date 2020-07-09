from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    food_cost=10
    damage=2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI

    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        fighters_and_distances=dict()
        k=self.place
        g=0
        while k!=skynet:
            for i in k.terminators:
                fighters_and_distances[i]=g
            if k.dragon!=self and k.dragon is not None:
                fighters_and_distances[k.dragon]=g
            if k.dragon!=None and k.dragon.is_container and k.dragon.contained_dragon is not None:
                if k.dragon.contained_dragon!=self:
                    fighters_and_distances[k.dragon.contained_dragon]=g
            k=k.entrance
            g+=1
                
        # BEGIN 4.5
        return  fighters_and_distances
        # END 4.5

    def calculate_damage(self, distance):
        damage=(self.damage-0.05*(self.fighters_shot))-0.2*distance
        if damage:
            return damage
        else:
            return 0
        # BEGIN 4.5
        return 0
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
