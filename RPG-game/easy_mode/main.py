#####################################
# Imports

from game_classes import Person
import random





#####################################
# Instantiate objects

main_player = Person("Superman", 500, 100, 50)

enemy = Person("Bad guy", 800, 70, 30)



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

        print(f"\t You attacked and dealt to {enemy.name} {dmg} points of damage")
    else:
        print("This is easy mode, you cannot choose other option for now")
        continue

    # 2.c. Enemy's turn
    print("=======================================")
    print(f"\t {enemy.name.upper()}")
    enemy_choice = random.randrange(0, len(enemy.action))
    if enemy_choice == 0:
        enemy_dmg = enemy.generate_atk_damage()
        main_player.take_damage(enemy_dmg)
        print(f"\t {enemy.name.capitalize()} attacked and dealt to you {enemy_dmg} points of damage")

    # 2.d Round Summary
    main_player.get_stats()
    enemy.get_stats()

    if main_player.hp == 0:
        print("\t\t YOU LOST !")
        running = False
    elif enemy.hp == 0:
        print("\t\t YOU WIN !")
        running = False



