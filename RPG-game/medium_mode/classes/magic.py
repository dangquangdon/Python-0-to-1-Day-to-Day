import random

class Magic:
    def __init__(self, name, mp_cost, damage, magic_type ):
        self.name = name
        self.mp_cost = mp_cost
        self.damage = damage
        self.magic_type = magic_type

    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        damage = random.randint(low, high)
        return damage
