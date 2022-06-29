from gc import get_stats
import random

class dungeon:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.player_start = []
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

class character:
    def __init__(self):
        self.inte = 0
        self.dext = 0
        self.stre = 0
        self.acc = 0
        self.health = 100
        self.block = 1
        self.spells = {}
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

class key:
    def __init__(self, rusty, size):
        self.rusty = rusty
        self.size = size

class enemy:
    def __init__(self, health, attack, speed, x, y):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.x = x
        self.y = y
    def get_stats(self):
        print("health: " + str(self.health))
        print("attack: " + str(self.attack))
        print("speed: " + str(self.speed))

class skeleton(enemy):
    def __init__(self, health, attack, speed, x, y):
        super().__init__(health, attack, speed, x, y)
        
    def special_attack(self, player):
        if random.randint(0,10) > 7:
            self.attack += 1
            print("The skeleton sharpened it's blade. It's attack has increased.")
    def strike(self, player):
        player.health -= self.attack * player.block
        print("The skeleton damaged you for " + str(self.attack * player.block) + " health.")
    def battle_start(self):
        print("A skeleton has appeared to attack you.")

class leech(enemy):
    def __init__(self, health, attack, speed,x,y):
        super().__init__(health, attack, speed,x,y)
        
    def special_attack(self, player):
        pass
    
    def strike(self, player):
            self.health += self.attack * player.block
            player.health -= self.attack * player.block
            print("The leech lunges at you, dealing "+ str(self.attack* player.block) + " damage to you and healing for the same amount")
    def batte_start(self):
        print("A leech has appeared to attack you.")


