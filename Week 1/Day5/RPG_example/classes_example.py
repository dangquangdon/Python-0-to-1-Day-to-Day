class Person:
    def __init__(self, name, hp, mp, atk):
        self.maxhp = hp  # HP of character when it's full
        self.hp = hp    # HP during the game will change, but the max HP should stay the same
        self.maxmp = mp  # Same like HP
        self.mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Attack"]
        self.name = name

    # Generate the amount of damage randomly in range of highest attack and lowest attack
    def generate_atk_damage(self):
        # This method should return a damage value
        # The value is a random number between atk_low and atk_high

    # When player takes damage, HP will be decreased
    def take_damage(self, dmg):
        # This method should return a new hp value after taken damage
        # new hp value is the current hp minus the dmg

    def get_stats(self):
        # This method should print out the current stats
        # Name
        # Hp/MaxHP
        # Mp/MaxMP
