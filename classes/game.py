import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\03[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack","Magic", "Items"] 
        self.name = name


    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def heal(self,dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def defence(self):
        return random.randrange(0,self.df)
        
    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp <0:
            self.hp = 0
        return self.hp    

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self,cost):
        self.mp -= cost
    
    def choose_action(self):
        i = 1
        print("\n"+"\t"+ bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "\tACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("\t\t" + str(i)+'.',item)
            i += 1
    
    def choose_magic(self):
        print("\n"+bcolors.OKBLUE + bcolors.BOLD + "\t\tMAGIC:" + bcolors.ENDC)
        i = 1
        for spell in self.magic:
            print("\t\t"+str(i)+".",bcolors.BOLD +spell.name,bcolors.ENDC+ bcolors.FAIL +"{Cost:", str(spell.cost)+ bcolors.ENDC + '}',bcolors.OKGREEN+ "{Strength:",str(spell.dmg) + "}" + bcolors.ENDC)
            i += 1

    def choose_items(self):
        print("\n"+bcolors.OKGREEN + bcolors.BOLD + "\t\tITEMS:"+bcolors.ENDC)
        i = 1
        for item in self.items:
            print("\t\t"+str(i)+".",bcolors.BOLD +item["item"].name + bcolors.ENDC+ " : "+ item["item"].description,"(x"+ str(item["quantity"])+")")
            i += 1

    def choose_target(self,enemies):
        i = 1
        print("\n" + bcolors.FAIL+ bcolors.BOLD+ "\tTARGET:"+ bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp != 0:
                print("\t\t"+ str(i)+"."+ enemy.name)
                i+=1
        


    def get_enemy_stats(self):
        chp = str(self.hp)
        while  len(chp) < 5:
            chp += ' '

        cmhp = str(self.maxhp)
        while  len(cmhp) < 5:
            cmhp += ' '
        

        print("                         __________________________________________________")
        print(bcolors.BOLD+ self.name + " "*(13-len(self.name))
            + chp+"/"+ cmhp+ "|" + bcolors.FAIL + "█"*int(self.hp*50/self.maxhp) + " "*(50-int(self.hp*50/self.maxhp)) + bcolors.ENDC+ bcolors.BOLD+"|"+ bcolors.ENDC )


    def get_stats(self):
        chp = str(self.hp)
        while  len(chp) < 4:
            chp += ' '

        c_mp = str(self.mp)
        while  len(c_mp) < 3:
            c_mp += ' '
        print(" "*25+"_________________________            __________")
        print(bcolors.BOLD+ self.name+" "*(15-len(self.name))
            + chp+"/"+ str(self.maxhp)+ "|" + bcolors.OKGREEN + "█"*int(self.hp*25/self.maxhp) + " "*(25-int(self.hp*25/self.maxhp)) + bcolors.ENDC+ bcolors.BOLD+"|   " + 
            c_mp +"/" +str(self.maxmp)+"|" + bcolors.OKBLUE + "█"*int(self.mp*10/self.maxmp) + " "*(10-int(self.mp*10/self.maxmp)) +bcolors.ENDC+"|")

    def choose_enemy_spell(self):
        pct = (self.hp/self.maxhp) *100
        if pct < 50:
            magic_choice = random.randrange(0,3)
        else:
            magic_choice = random.randrange(0,2)

        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        if spell.cost > self.mp:
            spell = ""
            magic_dmg = 0

        return spell, magic_dmg
