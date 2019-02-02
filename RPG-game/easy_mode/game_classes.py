import random


class Person:
    def __init__(self, name, hp, mp, atk):
        self.maxhp = hp  # HP of character when it's full
        self.hp = hp    # HP during the game will change, but the max HP should stay the same
        self.maxmp = mp  # Same like HP
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.action = ["Attack"]
        self.name = name


    def generate_atk_damage(self):

        """
         Generate the amount of damage randomly in range of highest attack and lowest attack
        """

        dmg = random.randrange(self.atkl, self.atkh)
        return dmg



    def take_damage(self, dmg):
        """
        When player takes damage, HP will be decreased
        """

        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def choose_action(self):
        """
        This method will just print to terminal something like this:

            ACTION:
                1. Attack
                2. Magic
                and so on
        In easy mode, your action list has just "Attack" so it only print
        "1. Attack"
        """

        number = 1
        print("\t\tACTION: ")
        for element in self.action:
            print(f"\t\t\t{number}: {element}")
            number = number + 1



    def get_stats(self):
        """
        This method will print out the current stats of all player and enenmy
        NAME:
            HP/MaxHP
            MP/MaxMP
        """

        print(f"\t\t {self.name.upper()}")
        print(f"\t\t\t {self.hp}/{self.maxhp}")
        print(f"\t\t\t {self.mp}/{self.maxmp}")



