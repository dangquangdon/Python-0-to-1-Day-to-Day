import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp  # HP of character when it's full
        self.hp = hp    # HP during the game will change, but the max HP should stay the same
        self.maxmp = mp  # Same like HP
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic  # This is and array of dictionaries, each dictionary will contain name, cost and dmg with different value
        self.action = ["Attack", "Magic", "Items"]
        self.items = items
        self.name = name

    # Generate the amount of damage randomly in range of highest attack and lowest attack
    def generate_atk_damage(self):
        return random.randrange(self.atkl, self.atkh)

    # When player takes damage, HP will be decreased

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_heal(self, dmg):
        self.hp += dmg
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
        elif self.hp > 0 and self.hp < self.maxhp:
            return self.hp
        else:
            self.hp = 0
        return self.hp

    # MP will be decreased after casting spell
    def reduce_mp(self, cost):
        self.mp -= cost

    # Utility method to get properties
    def get_hp(self):
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def choose_action(self):
        index = 1
        print("\t   {} {} ACTIONS {}".format(
            Bcolors.OKBLUE, Bcolors.BOLD, Bcolors.ENDC))
        for item in self.action:
            print(f"\t  {str(index)}: {item}")
            index += 1

    def choose_magic(self):
        index = 1
        print("\t   {} {} MAGIC {}".format(
            Bcolors.OKBLUE, Bcolors.BOLD, Bcolors.ENDC))
        for spell in self.magic:
            print("\t   {}: {} - Cost: {}".format(
                str(index), spell.name, spell.cost))
            index += 1

    def choose_item(self):
        index = 1
        print("\t   {} {} ITEMS {}".format(
            Bcolors.OKBLUE, Bcolors.BOLD, Bcolors.ENDC))
        for item in self.items:
            print("\t   {}: {} (x{}) - {}".format(str(index),
                                                  item.name, item.quantity, item.description))
            index += 1

    def get_stats(self, human):
        total_ticks = int((self.hp/self.maxhp)*25)
        total_ticks_mp = int((self.mp/self.maxmp)*25)
        white_space = int(25-total_ticks)
        white_space_mp = int(25-total_ticks_mp)
        stats_bar = "▓"
        space = " "
        mp_bar = "░"
        if human:
            print(f"{Bcolors.BOLD}{Bcolors.OKGREEN}{self.name}:{Bcolors.ENDC}")
            print("\t                 _________________________")
            print(f"\t{Bcolors.BOLD}HP   {self.hp}/{self.maxhp}\t|{Bcolors.OKGREEN}{stats_bar*total_ticks}{white_space*space}{Bcolors.ENDC}|")
            print("\t                 _________________________")
            print(f"\t{Bcolors.BOLD}MP   {self.mp}/{self.maxmp}\t|{Bcolors.OKBLUE}{mp_bar*total_ticks_mp}{white_space_mp*space}{Bcolors.ENDC}|")
        else:
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}{self.name}:{Bcolors.ENDC}")
            print("\t                 _________________________")
            print(f"\t{Bcolors.BOLD}HP   {self.hp}/{self.maxhp}\t|{Bcolors.FAIL}{stats_bar*total_ticks}{white_space*space}{Bcolors.ENDC}|")
            print("\t                 _________________________")
            print(f"\t{Bcolors.BOLD}MP   {self.mp}/{self.maxmp}\t|{Bcolors.OKBLUE}{mp_bar*total_ticks_mp}{white_space_mp*space}{Bcolors.ENDC}|")


class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def team_list(self, team):
        ind = 1
        for mem in team:
            print(f"\t{ind}: {mem.name}")
            ind += 1

    def get_choice(self, index):
        try:
            choice = int(index)-1
            return choice
        except ValueError:
            print("Must be a number")

    def check_hp(self, team):
        for mem in team:
            if mem.hp == 0:
                team.remove(mem)
        return team

    def physical_attack(self, mem, enemy):
        dmg = mem.generate_atk_damage()
        enemy.take_damage(dmg)
        print("--------------------------------------------------")
        print("\t{} attacked {} for {} points of damage".format(
            mem.name, enemy.name, dmg))
        print("--------------------------------------------------")

    def magical_attack(self, mem, enemy, select):
        magic_choice = self.get_choice(select)
        spell = mem.magic[magic_choice]

        dmg = spell.generate_dmg()
        spellname = spell.name
        cost = spell.cost

        current_mp = mem.get_mp()

        if cost > current_mp:
            print("--------------------------------------------------")
            print("{} Not enough MP \n {}".format(
                Bcolors.FAIL, Bcolors.ENDC))
            self.physical_attack(mem, enemy)
            print("--------------------------------------------------")
        else:
            mem.reduce_mp(cost)

            if spell.type == 'light':
                if mem.get_hp() == mem.get_maxhp():
                    print("--------------------------------------------------")
                    print(f"{mem.name} HP is full")
                    print("--------------------------------------------------")
                else:
                    mem.get_heal(dmg)
                    print("--------------------------------------------------")
                    print("{} {} heals {} for {} HP {}".format(
                        Bcolors.OKBLUE, spellname, mem.name, dmg, Bcolors.ENDC))
                    print("--------------------------------------------------")
            else:
                enemy.take_damage(dmg)
                print("--------------------------------------------------")
                print("{} {} deals {} points of damage to {} {}".format(
                    Bcolors.OKBLUE, spellname, str(dmg), enemy.name, Bcolors.ENDC))
                print("--------------------------------------------------")

    def use_item(self, mem, enemy, select):
        item_choice = self.get_choice(select)
        item = mem.items[item_choice]
        if item.type == 'potion':
            if item.quantity > 0:
                mem.get_heal(item.prop)
                item.quantity -= 1
                print("--------------------------------------------------")
                print("{}{} heals {} for {} HP - current amount: {} {}".format(
                    Bcolors.OKGREEN, item.name, mem.name, str(item.prop), str(item.quantity), Bcolors.ENDC))
                print("--------------------------------------------------")
            else:
                print("--------------------------------------------------")
                print("Insufficient amount of this item")
                self.physical_attack(mem, enemy)
                print("--------------------------------------------------")
        if item.type == 'elixer':
            if item.quantity > 0:
                mem.hp = mem.maxhp
                mem.mp = mem.maxmp
                item.quantity -= 1
                print("--------------------------------------------------")
                print("{}{} fully restores HP & MP- current amount: {} {}".format(
                    Bcolors.OKGREEN, item.name, str(item.quantity), Bcolors.ENDC))
                print("--------------------------------------------------")
            else:
                print("--------------------------------------------------")
                print("Insufficient amount of this item")
                self.physical_attack(mem, enemy)

        if item.type == 'attack':
            if item.quantity > 0:
                enemy.take_damage(item.prop)
                item.quantity -= 1
                print("--------------------------------------------------")
                print("{} {} deals {} points of damage to {}- current amount: {} {}".format(
                    Bcolors.OKBLUE, item.name, str(item.prop), enemy.name, str(item.quantity), Bcolors.ENDC))
                print("--------------------------------------------------")
            else:
                print("--------------------------------------------------")
                print("Insufficient amount of this item")
                self.physical_attack(mem, enemy)

    def turn(self, mem, enemy, select, human_turn):
        if human_turn:
            print("--------------------------------------------------")
            print("\t{}{}{}".format(Bcolors.BOLD, mem.name, Bcolors.ENDC))
            mem.choose_action()
            print("--------------------------------------------------")
        try:
            choice = self.get_choice(select)
            print("\t{} chose {}".format(mem.name, mem.action[choice]))
        except (IndexError, TypeError):
            print("Wrong number")

        # Physical Attack
        if choice == 0:
            self.physical_attack(mem, enemy)

        # Magical Attack
        elif choice == 1:
            if human_turn:
                # Print out options
                mem.choose_magic()

                # convert the choice to index number
                magic_choice = input("\tChoose your magic: ")
            else:
                magic_choice = random.randrange(1, len(mem.magic))

            self.magical_attack(mem, enemy, magic_choice)
        # USE ITEMS
        elif choice == 2:
            if human_turn:
                mem.choose_item()
                item_select = input("\tChoose item: ")
            else:
                item_select = random.randrange(1, len(mem.items))
            self.use_item(mem, enemy, item_select)
        else:
            print(
                "Wrong choice, there is no such option. You're forced to use physical attack !")
            self.physical_attack(mem, enemy)
