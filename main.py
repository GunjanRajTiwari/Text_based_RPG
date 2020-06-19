from classes.game import bcolors, Person
from classes.magic import spell
from classes.inventory import Item
import random
import sys

#Create black magic
fire = spell("Fire", 20, 600, "black")
thunder = spell("Thunder", 25, 900, "black")
blizzard = spell("Blizzard", 30, 1050, "black")
meteor = spell("Meteor", 40, 1200, "black")
quake = spell("Quake", 14, 250, "black")

#Create white magic
cure = spell("Cure", 25, 620, "white")
cura = spell("Cura",32,1500, "white")
curaga = spell("Curaga",50,6000, "white")

#Create some items
potion = Item("Potion","potion", "Heals 50 HP", 500)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 900)
superpotion = Item("Super-potion", "potion", "Heals 1000 HP", 2500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member.", 9999)
hielixer = Item("Mega elixer", "elixer", "Fully restores party's HP/MP.", 9999)

grenade = Item("Grenade", "attack", "Deals upto 5000 of splash damage.", 5000)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item":potion,"quantity":random.randrange(1,6)},
                {"item":hipotion,"quantity":random.randrange(0,4)},
                {"item":superpotion,"quantity":random.randrange(0,3)},
                {"item":elixer,"quantity":random.randrange(1,5)},
                {"item":hielixer,"quantity":random.randrange(0,3)},
                {"item":grenade,"quantity":random.randrange(2,4)}]


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "!!! A Text Based Role Play Game !!!" + bcolors.ENDC)
user = input(bcolors.OKGREEN + "Enter your name: " + bcolors.ENDC)
print(bcolors.BOLD + "Hello "+ str(user) + " Welcome to my text based Role play game. Hope you enjoy it." + bcolors.ENDC)
while True:
    instructions = input("Press I to get instructions and P to play: ")
    if instructions.upper() == "I":
        print("\n\nThis is a very firece war game. You can have upto 4 squad members to support you. When you die, the game is over.\nAll the players get chance to attack enemies first and then all the enemies will attack the players.\nYou can use"+bcolors.FAIL+ " ATTACK"+bcolors.ENDC+bcolors.OKBLUE+" MAGIC"+bcolors.ENDC+" and"+bcolors.OKGREEN+ " ITEMS"+bcolors.ENDC +"\nEach players have their own hitpoints, defensive abilities and magic points.\nThe items are shared by all the group members.\n\n"+bcolors.BOLD+bcolors.OKBLUE+"Use your war strategies\n"+bcolors.ENDC+bcolors.BOLD+bcolors.FAIL+"Defeat all enemies !!!"+ bcolors.ENDC+"\nChoose your options using the numbers as per listed." + bcolors.BOLD+bcolors.OKGREEN + "\nEnjoy !!!" + bcolors.ENDC + "\nEnter Q anytime to quit.")
        hold = input("Press Enter to continue: ")
        break
    elif instructions.upper() == "P":
        break
while True:
    player_squad = input("Choose the number of players in your squad(1 to 5): ")
    if player_squad.upper() == "Q":
        print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
        sys.exit(0)
    if player_squad.isdigit() and (int(player_squad) >= 1 and int(player_squad) <=5):
        break

#Instantiate people
player1 = Person(user,4160,215,311,34,player_spells,player_items)
player2 = Person("Squad1",3089,174,288,34,player_spells,player_items)
player3 = Person("Squad2",3089,174,288,34,player_spells,player_items)
player4 = Person("Squad3",3089,174,288,34,player_spells,player_items)
player5 = Person("Squad4",3089,174,288,34,player_spells,player_items)

#Instantiate enemies
general1 = Person("General1",  1250, 130, 560, 325, enemy_spells, [])
general2 = Person("General2",  1250, 130, 560, 325, enemy_spells, [])
general3 = Person("General3",  1250, 130, 560, 325, enemy_spells, [])
general4 = Person("General4",  1250, 130, 560, 325, enemy_spells, [])
general5 = Person("General5",  1250, 130, 560, 325, enemy_spells, [])

monster1 = Person("Monster1",18200,701,525,25,enemy_spells,[])
monster2 = Person("Monster2",18200,701,525,25,enemy_spells,[])
monster3 = Person("Monster3",18200,701,525,25,enemy_spells,[])
monster4 = Person("Monster4",18200,701,525,25,enemy_spells,[])
monster5 = Person("Monster5",18200,701,525,25,enemy_spells,[])


players = [player1, player2, player3, player4, player5]
enemies1 = [general1, general2, general3, general4, general5]
enemies2 = [monster1, monster2, monster3, monster4, monster5]  
enemies = [monster1]

for number in range((5 - int(player_squad))):
    players.pop(-1)

for number in range((int(player_squad)-1)//2):
    enemies.append(enemies2[number + 1]) 

for number in range(len(players)-len(enemies) + 1):
    enemies.append(enemies1[number])

while running:
    print("="*80)

    print("\n")
    print("NAME\t\t\t\tHP\t\t\t\tMP")
    for player in players: 
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        try:
            while True:
                index = input("\tChoose your action: ")
                if index.upper() == "Q":
                    print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                    sys.exit(0)
                index = int(index) - 1
                if index >=0 and index <=2:
                    break
                else:
                    print(bcolors.BOLD + bcolors.FAIL + "\tThere's no option such as "+ str(index + 1) + bcolors.ENDC)
        except ValueError:
            print(bcolors.FAIL + "You needed to choose a number. Chance missed !!"+ bcolors.ENDC)
            continue
        
        

        if index == 0:
            dmg = player.generate_damage()
            player.choose_target(enemies)
            try:
                while True:
                    enemy = input("\t\tYour choice: ")
                    if enemy.upper() == "Q":
                        print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                        sys.exit(0)        
                    enemy = int(enemy) - 1
                    if enemy >=0 and enemy < len(enemies):
                        break
                    else:
                        print(bcolors.BOLD + bcolors.FAIL + "\tThere's no enemy such as "+ str(enemy + 1) + bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL + "You needed to choose a number. Chance missed !!"+ bcolors.ENDC)
                continue
            defence = enemies[enemy].defence()
            enemies[enemy].take_damage(dmg- defence)
            print("You attacked "+enemies[enemy].name.replace(" ","")+" for",dmg- defence,"points.")

            if enemies[enemy].get_hp() == 0:
                print(bcolors.OKGREEN + enemies[enemy].name.replace(" ","") + " has died !!" + bcolors.ENDC)
                del enemies[enemy]
                if len(enemies) == 0:
                    print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                    sys.exit(0)
        
        elif index == 1:
            player.choose_magic()
            try:
                while True:
                    magic_choice = input("\tChoose a magic: ")
                    if magic_choice.upper() == "Q":
                        print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                        sys.exit(0)
                    magic_choice = int(magic_choice) -1
                    if magic_choice >=0 and magic_choice <=6:
                        spell = player.magic[magic_choice]
                        magic_dmg = spell.generate_damage()
                        if spell.cost <= player.get_mp():
                            break
                        else:
                            print(bcolors.FAIL+ bcolors.BOLD + "Not enough MP !!" + bcolors.ENDC)
                    else:
                        print(bcolors.BOLD + bcolors.FAIL + "\tThere's no option such as "+ str(magic_choice + 1) + bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL + "You needed to choose a number. Chance missed !!"+ bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for ",str(magic_dmg),"HP" + bcolors.ENDC)
                
            elif spell.type == "black":
                player.choose_target(enemies)
                try:
                    while True:
                        enemy = input("\t\tYour choice: ")  
                        if enemy.upper() == "Q":
                            print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                            sys.exit(0)      
                        enemy = int(enemy) -1
                        if enemy >=0 and enemy < len(enemies):
                            break
                        else:
                            print(bcolors.BOLD + bcolors.FAIL + "\tThere's no enemy such as "+ str(enemy + 1) + bcolors.ENDC)
                except ValueError:
                    print(bcolors.FAIL + "You needed to choose a number. Chance missed !!"+ bcolors.ENDC)
                    continue
                
                defence = enemies[enemy].defence()
                enemies[enemy].take_damage(magic_dmg-defence)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg- defence), "points of damage to "+enemies[enemy].name.replace(" ","") + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name.replace(" ","") + " has died !!" + bcolors.ENDC)
                    del enemies[enemy]
                    if len(enemies) == 0:
                         print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                         sys.exit(0)

        elif index == 2:
            player.choose_items()
            try:
                while True:
                    item_choice = input("\tChoose an item: ")
                    if item_choice.upper() == "Q":
                        print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                        sys.exit(0)
                    item_choice = int(item_choice) -1
                    if item_choice >=0 and item_choice <=5:
                        if player.items[item_choice]["quantity"] > 0:
                            item = player.items[item_choice]["item"]
                            player.items[item_choice]["quantity"] -= 1
                            break
                        else:
                            print("\n"+bcolors.FAIL + "\tNo "+ item.name + " remaining." + bcolors.ENDC)
                    else:
                        print(bcolors.BOLD + bcolors.FAIL + "\tThere's no option such as "+ str(item_choice + 1) + bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL + "You needed to choose a number. Chance missed !!"+ bcolors.ENDC)
                continue
        

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN+ "\n" + item.name + " heals for ", str(item.prop),"HP"+ bcolors.ENDC)

            elif item.type == "elixer":

                if item.name == "Mega elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)

            elif item.type == "attack":
                player.choose_target(enemies)
                
                try:
                    while True:
                        enemy = input("\t\tYour choice: ")
                        if enemy.upper() == "Q":
                            print(bcolors.FAIL+ bcolors.BOLD+ "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                            sys.exit(0)
                        enemy = int(enemy) -1
                        if enemy >=0 and enemy < len(enemies):
                            break
                        else:
                            print(bcolors.BOLD + bcolors.FAIL + "\tThere's no enemy such as "+ str(enemy + 1) + bcolors.ENDC)
                except ValueError:
                    print(bcolors.FAIL + "You needed to choose a number. Chance missed !!"+ bcolors.ENDC)
                    continue

                enemies[enemy].take_damage(item.prop - 2000)
                print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop - 2000), " points of damage to "+ enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy + 1]:
                    enemies[enemy+1].take_damage(item.prop- 3500)
                    print(bcolors.FAIL + item.name + " deals " + str(int(item.prop-4000)) + " damage to " + enemies[enemy+1].name + bcolors.ENDC)
                if enemies[enemy - 1]:
                    enemies[enemy -1].take_damage(item.prop- 4500)
                    print(bcolors.FAIL + item.name + " deals " + str(int(item.prop - 4000)) + " damage to " + enemies[enemy-1].name + bcolors.ENDC)

                
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name + " has died !!" + bcolors.ENDC)
                    del enemies[enemy]
                    if len(enemies) == 0:
                         print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                         sys.exit(0)

    print("\n")
    for enemy in enemies:
        a = True
        while a:
            enemy_choice = random.randrange(0,2)
            
            if enemy_choice == 0:   
                target = random.randrange(0,len(players))
                enemy_dmg = enemy.generate_damage()

                defence = players[target].defence()
                players[target].take_damage(enemy_dmg- defence)
                if players[target].name == user:
                    name = "You"
                else:
                    name = players[target].name
                print(enemy.name.replace(" ","") + " attacked "+name +" for",enemy_dmg - defence)
                a = False
                if players[target].get_hp() == 0:
                    if players[target].name == user:
                        name = "You"
                    else:
                        name = players[target].name
                    print(bcolors.FAIL + name + " died !!" + bcolors.ENDC)
                    del players[target]
                    if player1 not in players:
                        print(bcolors.FAIL +bcolors.BOLD + "You Lose!!!\n You have been defeated by your enemies!!!" + bcolors.ENDC)
                        sys.exit(0)

            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                if spell == "":
                    continue 
                else:
                    enemy.reduce_mp(spell.cost)

                    if spell.type == 'white':
                        enemy.heal(magic_dmg)
                        print(bcolors.OKBLUE + spell.name + " heals "+enemy.name.replace(" ","")+" for ",str(magic_dmg),"HP" + bcolors.ENDC)
                        
                    elif spell.type == "black":
                        target = random.randrange(0,len(players))
                        defence = players[target].defence()
                        players[target].take_damage(magic_dmg- defence)
                        if players[target].name == user:
                            name = "You"
                        else:
                            name = players[target].name
                        print(bcolors.OKBLUE + enemy.name.replace(' ', '') + "'s "+spell.name + " deals", str(magic_dmg- defence), "points of damage to "+name+ bcolors.ENDC)
                    
                        if players[target].get_hp() == 0:
                            print(bcolors.FAIL + name + " died !!" + bcolors.ENDC)
                            del players[target]
                            if player1 not in players:
                                print(bcolors.FAIL +bcolors.BOLD + "You Lose!!!\n You have been defeated by your enemies!!!" + bcolors.ENDC)
                                sys.exit(0)
                    a = False    