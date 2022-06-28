import characters
import random

# events

current_dungeon = characters.dungeon(10,10)

coordinate_x = 0
coordinate_y = 0

def movement():
    print("You notice that there are 4 doors, one for each cardinal direction. Which one would you like to go through")
    response = input("North, South, East, West")
    if response.lower() == "north":
        coordinate_y += 1
    elif response.lower() == "south":
        coordinate_y -=1
    elif response.lower() == "east":
        coordinate_x += 1
    elif response.lower() == "west":
        coordinate_x -= 1

def battle(foe): # the entire code for the battle system
    turns = 0
    inBattle = True
    attack = player.stre * 1
    player_done = False
    while inBattle:
        player.block = 1
        player_done = False
        while player_done == False:
            if turns < 1:
                print("You have encountered an enemy, what will you do?")
            else:
                print("What will you do next?")
            action = input("Fight, Block, Magic, Run, Items, Analyze")
            if action.lower() == "fight":
                if random.randint(0,10) < player.acc: # accuracy determines if attack lands
                    foe.health -= player.stre
                    print("You damaged the enemy for " + str(attack) + " health.")
                else:
                    print("You missed")
                turns += 1
                player_done = True
            elif action.lower() == "block":
                player.block = 0.5
                print("You brace yourself, reducing damage by half")
                turns += 1
                player_done = True
            elif action.lower() == "magic":
                magic_resp = input("What spell do you want to cast")
                if magic_resp.lower() == "heal": # heal here
                    heal_amount = player.inte
                    player.health += heal_amount
                    print("You healed youself for " + str(heal_amount) + " health.")
                turns += 1
                player_done = True
            elif action.lower() == "run":
                if random.randint(int(player.dext), 100 * (1/foe.speed)) < player.dext:# chance of escape based on player dext and enemy speed
                    inBattle = False
                    print("You managed to run away")
                else: 
                    print("Oh no, you couldn't escape.")
                turns += 1
                player_done = True
            elif action.lower() == "items":
                if len(player.items) == 0:
                    print("You have no items to use.")
                else:
                    pass
            elif action.lower() == "analyze":
                if "crystal_ball" in player.items:
                    pass
                else:
                    print("your health:")
                    print(player.health)
                print("enemy stats:")
                foe.get_stats()
                turns += 1
                player_done = True
            else:
                print("That is not a recognized action, try again.")
        
        if foe.health <=0: #checks if someone is defeated.
            print("You have slain the enemy.")
            inBattle = False
        elif player.health <=0:
            print("You have been slain")
            inBattle = False
        else: # enemy turn
            if turns % foe.speed == 0:
                print("The enemy is attacking.")
                if player.dext < (random.randint(0,10) * foe.speed):
                    foe.strike(player)
                else:
                    print("You managed to gracefully dodge the attack.")
            else:
                print("The enemy is preparing to attack.")
            
            foe.special_attack(player)



player = characters.character()
player.get_stats()
print("You wake up, body soaked with water. You get yourself upon, realizing you had been laying in a puddle.")
print("You look around, various objects can be found throughout the room. You then look down at the puddle and see your reflection.")
response = input("What are you wearing?")
if response.lower() in "naked nude nothing nada":
    print("Quite the predicament, you find that you are nude.")
else:
    print("Too bad, you are actually wearing nothing at all.")

print("Shivering, you look around to see if there is anything you could wear")

response = ""

done = False

# while done == False:
#     response = input("Pick one to interact with: person, cloth, rat")
#     if response.lower() == "person":
#         if player.inte > 4:
#             print("'Hello there, my name is Maggie. I am just a frail old lady, I could croak at any moment. But, while I am still around, I can help you.'")
#             print("'I can use divination to tell you your physical condition. Would you like that?'")
#             response2 = input("yes or no")
#             if response2.lower() == "yes":
#                 player.get_stats()
#             elif response2.lower() == "no":
#                 print("'Very well, come by again if you change your mi-'. The woman collapsed to the ground.")
#                 print("However, you noticed her crystal ball fell to the ground. Would you like to pick it up?")
#                 response = input("yes or no")
#                 if response.lower() == "yes":
#                     player.items["crystal_ball"] = "mystical"
#                     print("You pick up the crystal ball. You could feel it's magic power. It might be useful.")
#                 elif response.lower() == "no":
#                     print("You leave the ball alone. It slowly rolls away into a crack in the wall.")
#         else:
#             print("You tried talking to person, but it turns out you lack intelligence. You made a bunch of grunts, and the person died waiting for a proper response.")
#         print("You leave the old lady, ready to look at all the other objects, but you have found the other objects have vanished.")
#         print("Sure hope you didn't need those.")
#         done = True
#     else:
#         print("not an appropriate answer, try again.")

skeleton_knight = characters.skeleton(health = 100, attack= 10, speed= 2, x = random.randint(0,2), y = random.randint(0,2))

battle(skeleton_knight)

print("You have defeated the skeleton, but oh no! A leech has approached you.")

leacher = characters.leech(health = 50, attack = 5, speed  = 3, x = random.randint(-2, 0), y = random.randint(-2,0))

battle(leacher)