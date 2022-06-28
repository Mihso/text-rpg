import random

class character:
    def __init__(self):
        self.inte = 0
        self.dext = 0
        self.stre = 0
        self.acc = 0
        self.health = 100
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
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def get_stats(self):
        print("health: " + str(self.health))
        print("attack: " + str(self.attack))
        print("speed: " + str(self.speed))

class skeleton(enemy):
    def __init__(self, health, attack, speed):
        super().__init__(health, attack, speed)
        
    def special_attack(self):
        self.attack += 1
        print("The skeleton sharpened it's blade. It's attack has increased.")


