# ===========================
#   IMPORT MODULES
# ===========================

from classes.game import Person, Bcolors, Game
from classes.magic import Spell
from classes.inventory import Item
import random
import time

# ========================================
#   INSTANTIATE SPELLS, PLAYERS, ITEMS
# ========================================

# Create Dark Magic
# ----------------------
fire = Spell("Fire", 10, 100, "dark")
thunder = Spell("Thunder", 10, 100, "dark")
blizzard = Spell("Blizzard", 10, 100, "dark")
meteor = Spell("Meteor", 20, 200, "dark")
quake = Spell("Quake", 12, 120, "dark")

# Create Light Magic
# ----------------------
cure = Spell("Cure", 12, 120, "light")
cura = Spell("Cura", 18, 200, "light")

# Create some items
# ----------------------
potion = Item("Potion", "potion", "Heal 50 HP", 50, 20)
hi_potion = Item("Hi-potion", "potion", "Heal 100 HP", 100, 10)
super_potion = Item("Super Potion", "potion", "Heal 500 HP", 500, 5)
elixer = Item("Elixer", "elixer",
              "Fully restores HP & MP of one party's member", 99999, 1)
mega_elixer = Item("Mega Elixer", "elixer",
                   "Fully restores HP & MP of all party's members", 99999, 1)
grenade = Item("Grenade", "attack", "Deal 500 damage", 500, 2)

# Instantiate Players & Teams
# -----------------------
magic = [fire, thunder, blizzard, meteor, cure, cura]
items = [potion, hi_potion, super_potion, elixer, mega_elixer, grenade]

print("""{}
This is a 3v3 RPG game, the rule is simple, just try to defeat your enemies.
Each player takes turn to choose an enemy to attack, then choose what kind of attack you want
or item you want to use and hit.
First, choose your team members' name{}
""".format(Bcolors.BOLD, Bcolors.ENDC))

player1_name = input(f"{Bcolors.BOLD}{Bcolors.OKBLUE}First Player Name: {Bcolors.ENDC}")
player2_name = input(f"{Bcolors.BOLD}{Bcolors.OKBLUE}Second Player Name: {Bcolors.ENDC}")
player3_name = input(f"{Bcolors.BOLD}{Bcolors.OKBLUE}Third Player Name: {Bcolors.ENDC}")

player1 = Person(player1_name.upper(), 500, 65, 60, 34, magic, items)
player2 = Person(player2_name.upper(), 460, 65, 60, 34, magic, items)
player3 = Person(player3_name.upper(), 460, 65, 60, 34, magic, items)
enemy1 = Person("GREMLIN", 1200, 65, 50, 25, magic, items)
enemy2 = Person("BANSHEE", 1200, 65, 50, 25, magic, items)
enemy3 = Person("VAMPIRE", 1200, 65, 50, 25, magic, items)

team = [player1, player2, player3]
team2 = [enemy1, enemy2, enemy3]

game = Game(team, team2)


print("===============================================\n")
print("{}{}PLAYERS' TEAM:{}\n".format(
    Bcolors.BOLD, Bcolors.OKGREEN, Bcolors.ENDC))
for pl in team:
    pl.get_stats(True)
print()
print("===============================================\n")
print("{}{}ENEMIES' TEAM:{}\n".format(Bcolors.BOLD, Bcolors.FAIL, Bcolors.ENDC))
for enm in team2:
    enm.get_stats(False)
print()
print("===============================================\n")
running = True


# ========================================
#   START GAME LOOP
# ========================================
player_dead = []
bot_dead = []
if __name__ == "__main__":
    while running:

        # Human's turn

        for mem in team:
            # Player name
            print("\t{}{}{}".format(Bcolors.BOLD, mem.name, Bcolors.ENDC))

            # Select Target
            print("\t Target an enemy now !")
            game.team_list(team2)
            target = game.get_choice(input("\t Choose target: "))
            try:
                enemy = team2[target]
            except (ValueError, IndexError, TypeError):
                print("Type the number only !")
                continue

            # Select action
            mem.choose_action()
            select = input("\t Choose action: ")

            # Start the fight
            game.turn(mem, enemy, select, True)
            game.check_hp(team2)
        # DELAY
        print("=================================")
        print("{0}ENEMIES'S TURNS{1}".format(Bcolors.BOLD, Bcolors.ENDC))
        time.sleep(2)

        for mem2 in team2:
            # Select action
            select2 = random.randrange(1, 4)
            # Select Target
            if len(team) > 0:
                target2 = random.randrange(len(team))
                bot_target = team[target2]

                # Start the fight
                game.turn(mem2, bot_target, select2, False)
                game.check_hp(team)
            else:
                print("{0}All Dead ! Enemies Win{1}".format(
                    Bcolors.BOLD, Bcolors.ENDC))
                running = False
            time.sleep(1)

        print("=================================")
        for pl in team:
            pl.get_stats(True)
        print()
        for enm in team2:
            enm.get_stats(False)
        print()
        print("=================================")

        if len(team) == 0:
            print("{} You lost! {}".format(Bcolors.FAIL, Bcolors.ENDC))
            running = False
        elif len(team2) == 0:
            print("{}{} You win! {}".format(
                Bcolors.BOLD, Bcolors.OKGREEN, Bcolors.ENDC))
            running = False
