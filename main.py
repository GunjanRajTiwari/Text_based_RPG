from classes.game import bcolors, Person
from classes.magic import spell
from classes.inventory import Item
import random
import sys


#Create black magic
fire = spell("Fire", 25, 600, "black")
thunder = spell("Thunder", 25, 600, "black")
blizzard = spell("Blizzard", 25, 600, "black")
meteor = spell("Meteor", 40, 1200, "black")
quake = spell("Quake", 14, 140, "black")

#Create white magic
cure = spell("Cure", 25, 620, "white")
cura = spell("Cura",32,1500, "white")
curaga = spell("Curaga",50,6000, "white")

#Create some items
potion = Item("Potion","potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member.", 9999)
hielixer = Item("Mega elixer", "elixer", "Fully restores party's HP/MP.", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage.", 500)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item":potion,"quantity":15},
                {"item":hipotion,"quantity":5},
                {"item":superpotion,"quantity":5},
                {"item":elixer,"quantity":5},
                {"item":hielixer,"quantity":2},
                {"item":grenade,"quantity":5}]
#Instantiate people
player1 = Person("Valos:",3260,132,300,34,player_spells,player_items)
player2 = Person("Nick :",4160,188,311,34,player_spells,player_items)
player3 = Person("Robot:",3089,174,288,34,player_spells,player_items)

enemy1 = Person("Imp",  1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Magus",18200,701,525,25,enemy_spells,[])
enemy3 = Person("Imp",  1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]  

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "!!! A Text Based Role Play Game !!!" + bcolors.ENDC)

while running:
    print("=========================")

    print("\n\n")
    print("NAME\t\t\t\tHP\t\t\tMP")
    for player in players: 
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("\tChoose your action: ")
        index = int(choice)-1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked "+enemies[enemy].name.replace(" ","")+" for",dmg,"points.")

            if enemies[enemy].get_hp() == 0:
                print(bcolors.OKGREEN + enemies[enemy].name.replace(" ","") + " has died !!" + bcolors.ENDC)
                del enemies[enemy]
                if len(enemies) == 0:
                    print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                    sys.exit(0)
        
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("\tChoose a magic: ")) -1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL+"\nNot enough MP\n"+ bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for ",str(magic_dmg),"HP" + bcolors.ENDC)
                
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to "+enemies[enemy].name.replace(" ","") + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name.replace(" ","") + " has died !!" + bcolors.ENDC)
                    del enemies[enemy]
                    if len(enemies) == 0:
                         print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                         sys.exit(0)

        elif index == 2:
            player.choose_items()
            item_choice = int(input("\tChoose an item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if player.items[item_choice]["quantity"] < 0:
                print("\n"+bcolors.FAIL + "No "+ item.name + " remaining." + bcolors.ENDC)
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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to "+ enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name.replace(" ","") + " has died !!" + bcolors.ENDC)
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
                target = random.randrange(0,3)
                enemy_dmg = enemy.generate_damage()

                players[target].take_damage(enemy_dmg)
                print(enemy.name.replace(" ","") + " attacked "+players[target].name.replace(" ","")+" for",enemy_dmg)
                a = False
                if players[target].get_hp() == 0:
                    print(bcolors.FAIL + players[target].name.replace(" ","") + " has died !!" + bcolors.ENDC)
                    del players[target]
                    if len(players) == 0:
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
                        target = random.randrange(0,3)
                        players[target].take_damage(magic_dmg)
                        print(bcolors.OKBLUE + enemy.name.replace(' ', '') + "'s "+spell.name + " deals", str(magic_dmg), "points of damage to "+players[target].name.replace(" ","") + bcolors.ENDC)
                    
                        if players[target].get_hp() == 0:
                            print(bcolors.FAIL + players[target].name.replace(" ","") + " has died !!" + bcolors.ENDC)
                            del players[target]
                            if len(players) == 0:
                                print(bcolors.FAIL +bcolors.BOLD + "You Lose!!!\n You have been defeated by your enemies!!!" + bcolors.ENDC)
                                sys.exit(0)
                    a = False    