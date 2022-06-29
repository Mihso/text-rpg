from re import L
import characters
import random
import level

# events

current_dungeon = characters.dungeon(15,15) # determine dungeon size

player_coordinate = [current_dungeon.player_start[0], current_dungeon.player_start[1]]

enemies = []

def movement(): # movement through the dungeon
    print("It is hard to see, but you can move around. Which way would you like to go?")
    previous = [player_coordinate[0], player_coordinate[1]]
    response = input("North, South, East, West")
    if response.lower() == "east":
        player_coordinate[1] += 1
    elif response.lower() == "west":
        player_coordinate[1] -=1
    elif response.lower() == "south":
        player_coordinate[0] += 1
    elif response.lower() == "north":
        player_coordinate[0] -= 1
    else:
        print("")
        print("Not a direction, so you don't move.")
    if player_coordinate not in current_dungeon.spaces:
        print("")
        print("You ran into a wall.")
        player_coordinate[0] = previous[0]
        player_coordinate[1] = previous[1]

    for e in enemies:
        en_prev = [e.x, e.y]
        n = random.randint(0,3)
        if n == 0:
            e.x += 1
        elif n == 1:
            e.x -= 1
        elif n == 2:
            e.y += 1
        elif n == 3:
            e.y -= 1
        if [e.x, e.y] not in current_dungeon.spaces:
            e.x = en_prev[0]
            e.y = en_prev[1]
    if "crystal_ball" in player.items:
        print("")
        print("The crystal ball shines, revealing the location of moving individuals within this dungeon.")
        print("")
        print("you")
        print(player_coordinate)
        for e in enemies:
            print("")
            print(e.name)
            print("["+str(e.x)+","+str(e.y)+"]")
    elif "rat" in player.items:
        print("")
        enemy_nearby = False
        for e in enemies:
            if abs(e.x - player_coordinate[0]) < 2 and abs(e.y-player_coordinate[1]) < 2:
                print("Careful, I smell a " + e.name + " nearby.")
                enemy_nearby = True
        if enemy_nearby == False:
            print("Rat speaks up.")
            print("'It's safe at the moment, nobody else is nearby'")
        
def map():
    for l in range(current_dungeon.length):
        row = ""
        for w in range(current_dungeon.width):
            if [l,w] in current_dungeon.spaces:
                if l == player_coordinate[0] and w == player_coordinate[1]:
                    row += "[o]"
                elif l == current_dungeon.exit_loc[0] and w == current_dungeon.exit_loc[1]:
                    row += "[x]"
                else:
                    en_found = False
                    for e in enemies:
                        if l == e.x and w == e.y:
                            en_found = True
                    if en_found == True:
                        row += "[I]"
                    else:
                        row += "[ ]"
            else:
                row += "[#]"
        print(row)


def battle(foe): # the entire code for the battle system
    turns = 0
    inBattle = True
    attack = player.stre * 1
    player_done = False
    while inBattle:
        player.block = 1
        player_done = False
        while player_done == False:
            print("")
            print("What will you do?")
            action = input("Fight, Block, Magic, Run, Items, Analyze")
            if action.lower() == "fight":
                if random.randint(0,10) < player.acc: # accuracy determines if attack lands
                    dam = player.stre
                    if "rat" in player.items:
                        print("")
                        print("Rat attacks along side you.")
                        dam += (player.stre)
                    else:
                        pass
                    foe.health -= dam    
                    print("")
                    print("You damaged the enemy for " + str(attack) + " health.")
                else:
                    print("")
                    print("You missed")
                turns += 1
                player_done = True
            elif action.lower() == "block":
                player.block = 0.5
                print("")
                print("You brace yourself, reducing damage by half")
                turns += 1
                player_done = True
            elif action.lower() == "magic":
                magic_resp = input("What spell do you want to cast")
                player.spellcast(magic_resp)
                turns += 1
                player_done = True
            elif action.lower() == "run":
                if random.randint(int(player.dext), 100 * (1/foe.speed)) < player.dext:# chance of escape based on player dext and enemy speed
                    inBattle = False
                    print("")
                    print("You managed to run away")
                else: 
                    print("")
                    print("Oh no, you couldn't escape.")
                turns += 1
                player_done = True
            elif action.lower() == "items":
                if len(player.items) == 0:
                    print("")
                    print("You have no items to use.")
                else:
                    pass
            elif action.lower() == "analyze":
                if "crystal_ball" in player.items:
                    print("")
                    print("You used the crystal ball to analyze the " + foe.name + ".")
                    print("")
                    print("your stats:")
                    print(player.get_stats())
                    print("")
                    print("enemy stats:")
                    foe.get_stats()
                elif "rat" in player.items:
                    print("")
                    print("Rat squicks into your ear.")
                    print("'Careful, my magically enhanced instincts tell me that " + foe.name + " takes " +str(foe.speed)+" turns to attack. Be on your guard")
                print("")
                foe.description()
                turns += 1
                player_done = True
            else:
                print("")
                print("That is not a recognized action, try again.")
        
        if foe.health <=0: #checks if someone is defeated.
            print("")
            print("You have slain the " + foe.name +".")
            inBattle = False
        elif player.health <=0:
            print("")
            print("You have been slain")
            inBattle = False
        else: # enemy turn
            if turns % foe.speed == 0:
                print("")
                print("The "+ foe.name +" is attacking.")
                if player.dext < (random.randint(0,10) * foe.speed):
                    foe.strike(player)
                else:
                    print("")
                    print("You managed to gracefully dodge the attack.")
            else:
                print("")
                print("The "+foe.name+" is preparing to attack.")
            
            foe.special_attack(player)


player = characters.character() #introduction
player.get_stats()
exitting = characters.exit_dun(current_dungeon.exit_loc[0], current_dungeon.exit_loc[1])
print("")
print("You wake up, body soaked with water. You get yourself upon, realizing you had been laying in a puddle.")
print("You look around, various objects can be found throughout the room. You then look down at the puddle and see your reflection.")
print("")
response = input("What are you wearing?")
if response.lower() in "naked nude nothing nada":
    print("")
    print("Quite the predicament, you find that you are nude.")
else:
    print("")
    print("Too bad, you are actually wearing nothing at all.")

print("")
print("Shivering, you look around to see if there is anything you could wear.")

response = ""

done = False

while done == False:
    print("")
    response = input("Pick one to interact with: person, cloth, rat")
    if response.lower() == "person":
        if player.inte > 3:
            print("")
            print("'Hello there, my name is Maggie. I am just a frail old lady, I could croak at any moment. But, while I am still around, I can help you.'")
            print("'I can use divination to tell you your physical condition. Would you like that?'")
            response2 = input("yes or no")
            if response2.lower() == "yes":
                player.get_stats()
                print("")
                print("Maggie smiles. 'I can't really do much more now, but hopefully this item helps you out'.")
                player.items["crystal_ball"] = "mystical"
                print("Maggie gives you a crystal ball")
                print("With that crystal ball, you'll be able to see the status of anything you come across.")
            elif response2.lower() == "no":
                print("")
                print("'Very well, come by again if you change your mi-'. The woman collapsed to the ground.")
                print("However, you noticed her crystal ball fell to the ground. Would you like to pick it up?")
                response = input("yes or no")
                if response.lower() == "yes":
                    player.items["crystal_ball"] = "mystical"
                    print("")
                    print("You pick up the crystal ball. You could feel it's magic power. It might be useful.")
                elif response.lower() == "no":
                    print("")
                    print("You leave the ball alone. It slowly rolls away into a crack in the wall.")
        else:
            print("")
            print("You tried talking to person, but it turns out you lack intelligence. You made a bunch of grunts, and the person died waiting for a proper response.")
        print("")
        print("You leave the old lady, ready to look at all the other objects, but you have found the other objects have vanished.")
        print("Sure hope you didn't need those.")
        done = True
    elif response.lower() == "rat":
        print("")
        print("Hello, stranger. My name is Rat. I am a magically modified hamster and would like to escape this place, would you let me join you.")
        response2 = input("yes or no")
        if response2.lower() == "yes":
            print("")
            player.items["rat"] = "friend"
            print("'Thank you. I will assist whenever I can.'")
            print("")
            print("Rat has joined the party.")
        elif response2.lower() == "no":
            print("")
            print("Well, best of luck to you then.")
        print("")
        print("You look around and notice the other objects have vanished, hope you made the right choice")
        done = True
    elif response.lower() == "cloth":
        print("You find a bunch of clothes. You grab them when a map falls out from inside. You grab the map")
        player.items["map"] = "magic"
        print("It turns out to be a magic map, with you being able to see youself on the map, among othe things.")
        print("")
        player.health += 50
        print("You put the clothes on. They feel oddly dense. Could make for some goood protection")
        done = True
    else:
        print("")
        print("not an appropriate answer, try again.")


game_state = True
# The actual game state

level1 = level.level_1(current_dungeon) # generates enemies based on dungeon input
enemies = level1.enemy_list
while game_state == True:
    if "map" in player.items:
        map()
    movement()

    for e in enemies:
        if player_coordinate == [e.x, e.y]:
            print("")
            e.battle_start()
            battle(e)
    if player_coordinate == [current_dungeon.exit_loc[0],current_dungeon.exit_loc[1]]: # end game if goal is reach
        print("")
        print("Congrats, you made it out of the dungeon.")
        print("")
        if "rat" in player.items:
            print("Rat walks to in front of you.")
            print("'Thank you for letting join you. I hope you the best.'")
        game_state = False