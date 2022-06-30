import characters
import random


class level_1:
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.enemy_list = []
        self.event_list = []

        def enemy_location(dunge):
            enemy_coordinate = []
            enemy_loc = False
            for s in dunge.spaces:
                if enemy_loc == False:
                    if random.randint(1,200) < 2:
                        enemy_coordinate = [s[0],s[1]]
                        enemy_loc = True
            if enemy_loc == False:
                enemy_coordinate = dunge.spaces[random.randint(0, len(dunge.spaces)-1)]
            return enemy_coordinate

        skeleton_loc = enemy_location(self.dungeon)
        skeleton_knight = characters.skeleton(health = 100, attack= 10, speed= 2, x = skeleton_loc[0], y = skeleton_loc[1])
        self.enemy_list.append(skeleton_knight)

        leacher_loc = enemy_location(self.dungeon)
        leacher = characters.leech(health = 50, attack = 25, speed = 3, x = leacher_loc[0], y = leacher_loc[1])
        self.enemy_list.append(leacher)

        leacher_loc = enemy_location(self.dungeon)
        leacher1 = characters.leech(health = 70, attack = 20, speed = 3, x = leacher_loc[0], y = leacher_loc[1])
        self.enemy_list.append(leacher1)

        skeleton_loc = enemy_location(self.dungeon)
        skeleton_knight1 = characters.skeleton(health = 120, attack= 13, speed= 2, x = skeleton_loc[0], y = skeleton_loc[1])
        self.enemy_list.append(skeleton_knight1)

        for i in range(0,10):
            if random.randint(1,10) > 5: 
                event_loc = enemy_location(self.dungeon)
                trap1 = characters.trap(event_loc[0],event_loc[1],"trap",random.randint(10,30))
                self.event_list.append(trap1)