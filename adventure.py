import characters
import random

# events

def battle(foe):
    turns = 0
    inBattle = True
    attack = player.stre * 1
    while inBattle:
        if turns < 1:
            print("You have encountered an enemy, what will you do?")
        else:
            print("The enemy still stands, what will you do?")
        action = input("Fight, Magic, Run, Items, Analyze")
        if action.lower() == "fight":
            if random.randint(0,10) < player.acc:
                foe.health -= player.stre
                print("You damaged the enemy for " + str(attack) + " health.")
            else:
                print("You missed")
            turns += 1
        elif action.lower() == "magic":
            magic_resp = input("What spell do you want to cast")
            if magic_resp.lower() == "heal":
                heal_amount = player.inte
                player.health += heal_amount
                print("You healed youself for " + str(heal_amount) + " health.")
        elif action.lower() == "run":
            if random.randint(int(player.dext), 100 * foe.speed) < player.dext:
                inBattle = False
                print("You managed to run away")
            else: 
                print("Oh no, you couldn't escape.")
            turns += 1
        elif action.lower() == "analyze":
            print("your health:")
            print(player.health)
            print("enemy stats:")
            foe.get_stats()
            turns += 1
        else:
            print("That is not a recognized action, try again.")
        
        if foe.health <=0: #checks if someone is defeated.
            print("You slain the enemy.")
            inBattle = False
        elif player.health <=0:
            print("You have been slain")
            inBattle = False
        else: # enemy turn
            if turns % foe.speed == 0:
                print("The enemy is attacking.")
                if player.dext < (random.randint(0,10) * foe.speed):
                    player.health -= foe.attack
                    print("The enemy damaged you for " + str(foe.attack) + " health.")
                else:
                    print("You managed to gracefully dodge the attack.")
            else:
                print("The enemy is preparing to attack.")
            
            if random.randint(0,10) > 7:
                foe.special_attack()



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

# done = False

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

skeleton_knight = characters.skeleton(health = 100, attack= 10, speed= 2)

battle(skeleton_knight)