# Requirements

## Easy:
- 1v1, Good guy vs Bad guy
- Create a class ```Person``` with attributes:
    - name - string
    - hp - int
    - max_hp - int( = hp)
    - mp - int
    - max_mp - int (= mp)
    - atk_high = atk + 10
    - atk_low = atk - 10
    - action - list of string: at this level, only ["Attack"]
- class ```Person``` has method:
    - get_stat() to print out name, HP/MaxHP, MP/MaxMP
    - generate_dmg() return a attack damage value, randomly between atk_high and atk_low
    - take_dmg() take into a damage value and calculate the HP loss and return new HP points
    - choose_action() print out all the action options in the action list, at this stage is to print out from ["Attack"]
- Game Play:
    - import class ```Person```
    - instantiate(create) new instance of ```Person```, one is player, one is enemy
    - The game starts with a instruction printed out, says "This game is ....."
    - After that is the stats of the player and enemy
    - Player plays first, start choosing action
    - At this point, only attack, after choose attack, call generate_dmg() method from player
    - Call take_dmg() from enenmy
    - Print out the result of this turn, how many damages has been caused by player to enemy
    - Enemy's turn
    - Call generate damage from enemy
    - Call take_dmg() from player
    - Print out the result of this turn, how many damages has been caused by enemy to player
    - Print out the new stats of player and enemy
    - Check hp of player and enemy, whose hp == 0, lost
    - If hp != 0, start the loop again

## Medium:
- Create a new class called ```Magic```:
    - this class will have some attributes below:
        - name - string
        - mp_cost - int
        - dmg - int
        - type - string (dark or light)
    - this class has a method called generate_magic_dmg() which will return a random value between dmg + 15 and dmg - 15

- Attribute action is now ["Attack","Magic"]
- Add new attribute call magic - it will be a list of magic that contains all the instances of class ```Magic```
- Therefore, choose_action() should be adjusted to print out Magic as well as option to choose
- in class ```Person```:
    - Create new method called reduce_mp() to deduct current mp after using a magic, return new mp value
    - Create new method call choose_magic() acts the same as choose_action() because if player choose magic, it will show a list of magic option to chooose from
- Game Play:
    - import class Magic
    - create 3 - 4 instances of Magic and put it in a magic list
    - add this magic list to player and enemy instantiation
    - Modify/add game logic when player choose magic
    - For the enemy, let's just hard code the Attack option for it at this point. In other word, enemy only use Attack, even though it has Magic but it uses only Attack
    - After each round, check hp and mp, if mp is <= 0, set mp value to 0

## Hard:
- Instantiate 1 more magic, not dark one, but light one ("light")
- In the person class, create a new method call get_heal() that will return new hp of the player after being healed (hp = hp + damage).
However, you have to check, the hp cannot be bigger than maxhp.
    - If after healing, the hp is bigger than maxhp, set the hp = maxhp.
    - Else if 0 < hp < maxhp, return hp
    - And if hp < 0, set hp = 0

- In the game loop, now you have to check if the magic that the player chooses it dark or light, if the light magic is chosen:
    - print a message "Your HP is full" if after healing, new hp is max
    - print a message, something like "The light magic heals ... points of hp" if HP is not full after healing
    - Since you're healing yourself, enemy will take 0 damage

- In this mode, you will give your enemy a "brain":
    - in Enemy's turn, enemy_choice will now be selected randomly between 0 and the length of action list
    - Write if statements to check the choices, if choice is 0, we already have that
    - If choice is 1, enemy now can choose magic, and the magic choice is also a random number in range of 0 and the length of magic list. In this case, the logic should be the same as when player chooses magic.

**Extra:**
- Create new class called Item, that has name, type, description, property, and quantity
- Instantiate a few more items from Item class:
    - potion - type potion, heals 50 hp and quantity of 20
    - high potion - heals 100 hp and quantity of 10
    - super potion - heals 300 hp and quantity of 5
    - elixer - type elixer, restore max HP and MP, quantity of 1
    - grenade - type attack, deal 300 damage, quantity of 2

- Put those items into list, maybe called items
- In Person class, add new field self.items. And in the instantiation of player and enemy, add items list in it.
- Add "Use Items" in the action list of Person class.
- So now, write extra logic in the game, to check if player choose to use items, and then what kind of item (type) and the items should do their job (healing or causing damage)



## TO WRITTE:

- Extreme
