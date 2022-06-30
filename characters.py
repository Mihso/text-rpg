import random

class dungeon:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.player_start = []
        self.exit_loc = []
        self.spaces = []
        empty = []

        for l in range(self.length):
            for w in range(self.width):
                if random.randint(0,10) > 4:
                    if len(self.spaces) == 0:
                        self.spaces.append([l,w])
                    else:
                        placed = False
                        for s in self.spaces:
                            if placed == False:
                                if s[0] + 1 == l or s[0] - 1 == l or s[1] + 1 == w or s[1]-1 == w:
                                    self.spaces.append([l,w])
                                    placed = True
                                else:
                                    pass
                else:
                    empty.append([l,w])
        for e in empty:
            if [e[0] + 1, e[1]+1] not in self.spaces and [e[0]-1, e[1]-1] not in self.spaces:
                self.spaces.append(e)
            elif [e[0] - 1, e[1] + 1] not in self.spaces and [e[0]+1, e[1]-1] not in self.spaces:
                self.spaces.append(e)

        player_placed = False
        for s in self.spaces:
            if player_placed == False:
                    if random.randint(1,10) < 2:
                        self.player_start = s
                        player_placed = True
        if player_placed == False:
            self.player_start = self.spaces[0]
            player_placed = True
        exit_placed = False
        for s in self.spaces:
            if exit_placed == False:
                if random.randint(1,100) < 2:
                    self.exit_loc = s
                    exit_placed = True
        if exit_placed == False:
                self.exit_loc = self.spaces[len(self.spaces)-1]
                exit_placed = True

class character:
    def __init__(self):
        self.inte = 0
        self.dext = 0
        self.stre = 0
        self.acc = 0
        self.health = 100
        self.block = 1
        self.spells = {}
        self.spells["heal"] = "yes"
        self.spells["cleanse"] = "yes"
        self.items = {}
        points = 40
        while points > 0:
            p = random.randint(1,4)
            if p == 1:
                self.inte += 1
            elif p == 2:
                self.dext += 1
            elif p == 3:
                self.stre += 1
            elif p == 4:
                self.acc += 1
            points -= 1
        self.baseint = self.inte
        self.basedext = self.dext
        self.basestre = self.stre
        self.baseacc = self.acc

    def get_stats(self):
        print("int: " + str(self.inte))
        print("dex: " + str(self.dext))
        print("str: " + str(self.stre))
        print("acc: " + str(self.acc))
        print("health: " + str(self.health))
        print("")
        print("You have access to these spells:")
        for s in self.spells:
            print(s)

    def spellcast(self, spell):
        if spell.lower() == "heal": 
            heal_amount = self.inte
            self.health += heal_amount
            print("")
            print("You healed youself for " + str(heal_amount) + " health.")
        elif spell.lower() == "cleanse":
            self.acc = self.baseacc
            self.stre = self.basestre
            self.dext = self.basedext
            print("")
            print("You have cleansed yourself of debuffs")

class exit_dun:
    def __init__(self,x,y):
        self.found = False
        self.x = x
        self.y = y

class trap:
    def __init__(self,x,y, name, damage):
        self.x = x
        self.y = y
        self.name = name
        self.damage = damage

class something:
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y


class key:
    def __init__(self, rusty, size):
        self.rusty = rusty
        self.size = size

class enemy:
    def __init__(self, health, name, attack, speed, x, y):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        self.x = x
        self.y = y
    def get_stats(self):
        print(self.name)
        print("health: " + str(self.health))
        print("attack: " + str(self.attack))
        print("speed: " + str(self.speed))

class skeleton(enemy):
    def __init__(self, health, attack, speed, x, y):
        super().__init__(health, "skeleton", attack, speed, x, y)
        
    def special_attack(self, player):
        if random.randint(0,10) > 7:
            self.attack += 1
            print("The skeleton sharpened it's blade. It's attack has increased.")
    def strike(self, player):
        player.health -= self.attack * player.block
        print("The skeleton damaged you for " + str(self.attack * player.block) + " health.")
    def battle_start(self):
        print("A skeleton has appeared to attack you.")
    def description(self):
        print("A spooky skeleton with a sword. Seems to have a bone to pick with you.")

class leech(enemy):
    def __init__(self, health, attack, speed,x,y):
        super().__init__(health, "leech", attack, speed,x,y)
        
    def special_attack(self, player):
        pass
    
    def strike(self, player):
            self.health += self.attack * player.block
            player.health -= self.attack * player.block
            print("The leech lunges at you, dealing "+ str(self.attack* player.block) + " damage to you and healing for the same amount")
    def battle_start(self):
        print("A leech has appeared to attack you.")
    def description(self):
        print("A giant leech with sharp teeth. At least it is not a vampire.")

class overlord(enemy):
    def __init__(self, health, attack, speed,x,y):
        super().__init__(health, "Overlord", attack, speed,x,y)
        
    def special_attack(self, player):
        if random.randint(0,10) > 7:
            player.stre = player.stre / 2
            player.acc = player.acc / 2
            player.dex = player.dex / 2
            print("")
            print("The Overlord has cast a curse on you, halving your strength, accuracy, and dexterity.")
        if random.randint(0,8) > 7:
            if self.speed > 1:
                self.speed -=1
            print("")
            print("The Overlord has cast a spell on itself, increasing it's speed.")
        
        if random.randint(0,5) > 5:
            player.health -= self.attack / 2
            print("")
            print("Some random minions take potshots at you, dealing " + str(self.attack/2) + " damage.")

    
    def strike(self, player):
            player.health -= self.attack * player.block
            print("The Overlord strikes, dealing "+ str(self.attack* player.block) + " damage to you.")
    def battle_start(self):
        print("The Overlord towers before you.")
        print("")
        print("'Who dares challenge me?'")
    def description(self):
        print("A demon lord proficient with all kinds of magics. Be wary.")


