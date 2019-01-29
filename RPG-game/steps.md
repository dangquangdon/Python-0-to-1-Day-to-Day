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
    
## TO WRITTE:  
- Hard  
- Extreme
