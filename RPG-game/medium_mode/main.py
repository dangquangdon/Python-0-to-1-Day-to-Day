#####################################
# Imports

from classes.game import Person
from classes.magic import Magic
import random





#####################################
# Instantiate objects

# Magic
# At this medium level, let's start with all dark magic
fire = Magic("Fire", 10, 100, "dark")
thunder = Magic("Thunder", 12, 120, "dark")
meteor = Magic("Meteor", 40, 200, "dark")

magic_list = [fire, thunder, meteor]


#Players
main_player = Person("Superman", 500, 100, 50, magic_list)

enemy = Person("Bad guy", 800, 70, 35, magic_list)




#####################################
# Main game

# 1. Welcome speech and print the current stats of player and enemy

print("=======================================")
print("\t Welcome to the game !")
print("\t Let's kill the bad guys")
main_player.get_stats()
enemy.get_stats()
print("=======================================")

# 2. Start the loop
running = True
while running:
    # 2.a Main player starts first
    print("=======================================")
    print(f"\t {main_player.name.upper()}")
    main_player.choose_action()
    choice_input = input("\t\t\tChoose a number: ")
    index = int(choice_input) - 1
    print(f"\t You chose {main_player.action[index]}")

    # 2.b Physical attack
    if index == 0:
        dmg = main_player.generate_atk_damage()
        enemy.take_damage(dmg)
        print("=======================================")
        print(f"\t You attacked and dealt to {enemy.name} {dmg} points of damage")
    elif index ==  1:
        main_player.choose_magic()
        magic_choice = int(input("Choose your magic: "))
        magic_index = magic_choice - 1

        magic = main_player.magic[magic_index]

        # Generate magical damage
        magic_damage = magic.generate_damage()
        magic_name = magic.name
        magic_cost = magic.mp_cost

        # Check if player has enough MP to use
        if magic_cost > main_player.mp:
            print("Not enough MP")
            continue
        else:
            main_player.reduce_mp(magic_cost)
            enemy.take_damage(magic_damage)
            print("=======================================")
            print(f"\t You attacked with {magic_name}and dealt to {enemy.name} {magic_damage} points of damage")

        # For now, we  only have dark magic,
        # so we can skip checking magic type

    else:
        print("This is easy mode, you cannot choose other option for now")
        continue

    # 2.c. Enemy's turn
    print("=======================================")
    print(f"\t {enemy.name.upper()}")
    # enemy_choice = random.randrange(0, len(enemy.action))
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_dmg = enemy.generate_atk_damage()
        main_player.take_damage(enemy_dmg)
        print(f"\t {enemy.name.capitalize()} attacked and dealt to you {enemy_dmg} points of damage")

    # 2.d Round Summary
    print("=======================================")
    main_player.get_stats()
    enemy.get_stats()

    if main_player.hp == 0:
        print("\t\t YOU LOST !")
        running = False
    elif enemy.hp == 0:
        print("\t\t YOU WIN !")
        running = False



