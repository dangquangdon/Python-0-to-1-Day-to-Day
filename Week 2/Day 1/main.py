from game import Person
from magic import Magic

print("This is the instruction.......")

# Magic (Medium level)
fire = Magic("Fire", 10, 30, "dark")
wind = Magic("Wind", 15, 50, "dark")
ice = Magic("Ice", 20, 70, "dark")

magic_list = [fire, wind, ice]


player = Person("Daniel", 500, 100, 50, magic_list)
enemy = Person("Vampire", 1000, 100, 20, magic_list)




player.stats()
enemy.stats()
print("--------------------------------------")
running = True
while running:
    # PLAYER'S TURN
    print(player.name)
    print("Choose your action: ")
    player.choose_action()
    try:
        choice = int(input(">>>: "))
    except ValueError:
        print("Choose a number !")
        continue
    action_index = choice - 1
    if action_index == 0:
        damage = player.generate_atk_damage()
        enemy.take_damage(damage)

        print(" You attacked {} and dealt {} damage".format(enemy.name, damage))
    if action_index == 1:
        player.choose_magic()
        magic_choice = int(input(">>>: "))

    # You guys write the logics of the medium level here






    else:
        print(" Choose a correct number")
        continue

    # ENEMY'S TURN
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_damage = enemy.generate_atk_damage()
        player.take_damage(enemy_damage)

        print("{} attacked {} and dealt {} damage".format(enemy.name, player.name, enemy_damage))


    print("------------------------------------------")
    player.stats()
    enemy.stats()

    if player.hp == 0:
        print("You lost")
        running = False
    if enemy.hp == 0:
        print("You won")
        running = False
