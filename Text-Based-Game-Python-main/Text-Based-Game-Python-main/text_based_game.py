import random

bathroom=False
door1 = False
table1 = False
room1= True
room2= False
game = True
time_room2 =0
sofa_times = 0
backpack=['Red bull']
chair_times = 0
player_attack = 40
player_energy = 60
batoneta=False
room3 = False
entrance="1"
room4=False
monster_health=100
locked = True

class Items:
    def __init__(self,name,amount):
        self.name=name
        self.ammount=ammount
    
    def add_ammount(self):
        self.ammount += ammount


def fightmonster(player_energy,player_attack,backpack,monster_health):
    monster_attack= random.randrange(19, 39)
    player_damage = random.randrange(player_attack-10, player_attack+10)
    if monster_attack>=30:
        print("Monster had a critical shot with "+ str(monster_attack) +" damage")
    else:
        print("Monster hitted you with "+ str(monster_attack) + " damage!")
    player_energy -=  monster_attack
    if player_energy <= 0:
        player_energy=0
        print("\n\n\nThat shot killed you!\n\n GAME OVER \n\n Thanks for playing maybe an other time")
        exit()
    else:
        player_damage = random.randrange(player_attack-10, player_attack+10)
        monster_health -= player_damage
        if player_damage>=(player_attack+5):
            print("You hitted the monster in the head with a critical shot of "+str(player_damage)+" damage")
        else:
            print("You hitted the monster with "+str(player_damage)+" damage")

        if monster_health <= 0:
            monster_health=0
            print("\n\n\nYou killed that fcking wolf-hawk zombie  and you brought lith in the whole city!!\n\n Thanks for playing")
            exit()
    print("Your Health : "+ str(player_energy))
    print("Monster's Health : "+ str(monster_health))
    return monster_health,player_energy
    
    
    
    



















def displaybackpack(backpack,player_energy,player_attack):
    if len(backpack)==0:
        print('\nYour Backpack is empty')
    else:
        if len(backpack)>=15:
            print('\nThere is not space om your backpack')
        print("In your backpack there are " + str(len(backpack)) + " items :")
        for x in range(len(backpack)): 
            print ('> ' + backpack[x] + "("+ str(x+1) +")")
    print ('> Or press (15) to go back')    
    print ("\nYour backpack uasge is " + str(len(backpack)) + "/15.\n\n")
    item_index = input()
    if item_index == "15":
        print("Get out of here")
    else:
        print("> Use (1) or Destroy (2)")
        use = input()
        item = backpack[int(item_index)-1]
        if  use == "2":
            print(" "+ backpack[int(item_index)-1] +" destroyed")
            backpack.remove(item)
        elif use == "1":
            if item == "Red bull":
                player_energy = player_energy + 33
                print("Your energy increased by 33")
                print("Your energy :" + str(player_energy) )
                backpack.remove(item)
            elif item == "Knife":
                print("Now you can damage monsters")
                player_attack = 40
            else:
                print("You cant use that right now!")

        
          

def backpack_insert(item):
    backpack.append(item)
    print("\n1 " + item + " is obtained in your backpack\n\n") 



        
               









print('\n\nYou just woke up in the middle of nowhere after u were asleep for 2 days.\nYou are laying on a sofa and there is totaly darkness in the room.\nThe only thing you have in your hands is a torch and your backpack.\n\n')

print('> Turn on the torch (1)\t\t')
print('> Exit the game (2)')
answer = input("\n")

if answer=="2":
    print('\nThanks For your time hommie... Bye!\n\n')
    exit()


elif answer=="1": 
    print('\nTorch is turned on !!') 

print("\nNow you stand up in front of the sofa and you can define few objects in the room.")
print("There is a door in the depth of the room and on your right hand")
print("there is a table.\n\n ")
while game == True:
    while room1==True:
        print("\n\n  First Room")
        print('> Go to the door (1)\t\t > Search the table (2)')
        print('> Search the sofa (3)\t\t> Open your backpack (4)')
        answer = input('')
        
        if answer=="2":
            if locked ==True:
                print('\nThere is box with a locket that receives a 3 digit combination in order to open!\n\n') 
                print('> Try 3 digit combination  (1)')
                print('> Back to room (2)')
                inner_answer = input("\n\n")
                if inner_answer == "1":
                    code=input('\n\nEnter the code : ')
                    if code == "666":
                        print("You found a Silver Key and a Knife")
                        backpack_insert("Knife")
                        backpack_insert("Silver Key")
                        locked=False
                    else:
                        print('Wrong password')
            else:
                print("The box is unlocked and empty")


        elif answer=="3":
            if sofa_times == 0:
                sofa_times = sofa_times +1
                print('\nThe sofa is covered with a blanket')
                print('> Take the blanket (1)')
                print('> Previous options (2)')
                inner_answer = input("\n\n")
                if inner_answer=="1":
                        backpack_insert("Blanket")
                else:
                    continue
            elif sofa_times == 1:
                print('\nUnder the blanket there are some old receipts')
                print('> Take the receipts (1)')
                print('> Back to room (2)')
                inner_answer = input("\n\n")
                if inner_answer=="1":
                        backpack_insert("Old receipts")
                        sofa_times = sofa_times + 1
                elif inner_answer=="2":
                    continue
                else:
                    print("Wrong input")

            else:
                print('\n Nigga there is nothing more to see\n')

                
                

        elif answer=="4":
            displaybackpack(backpack,player_energy,player_attack)
            continue

        elif answer == "1":
            print("The door was unlocked!!\n")
            print("\n\nSecond Room\n")
            room2 = True
            room1 = False
        else:
            print("Wrong input")







    while room2==True:
        if time_room2 == 0:
            print("This is a living room.\n\n The lights here are turned on. After a quick check you can see a TV, a chair and two doors.\nThe one is on your left hand and the other one on your right hand\n\n")
            time_room2 += 1
        print('> Go to the left door (1)\t\t> Go to the right door (2)')
        print('> Search the chair (3)\t\t        > Search the television area (4)')
        print('> Go back to first room (5)\t\t> Open your backpack (6)')
        answer = input()
        if answer=="2":
            if 'Silver Key' not in backpack:
                print('\nThe door is locked!!\nYou need a key to open that door\n\n')
            elif 'Silver Key' in backpack:
                bathroom=True
                while bathroom==True:
                    if entrance=="1":
                        print("You entered the bathroom\n\n")
                        print("Inside the bathroom there is a mirror, a sink and a bathub")
                        entrance="2"
                    print('> Check the bathtub (1)\t\t> Check the sink (2)')
                    print('> Check the mirror (3)\t\t>  Go back to the living room  (4)')
                    answer = input()
                    if answer == "1":
                        print("OGHGG!@ Black Blood")
                    elif answer == "2":
                        if 'battonete' not in backpack:
                            print("You can see something shiny stucked inside the sink hole, but you can't pull it out\n Maybe check for something sharp or long to help you")
                        elif 'battonete' in backpack:
                            print("You managed to pull it out, with your battonete!\n\n Its a Godlen Key")
                            backpack.remove("battonete")
                            backpack_insert("Golden Key")
                    elif answer == "3":
                        if batoneta==False:
                            print("Behind the mirror you found a batonete")
                            backpack_insert("battonete")
                            batoneta=True
                        else:
                            print("There is nothing more you can find near the mirror !")
                    elif answer == "4":
                        bathroom= False
                    else:
                        print("Wrong input")
                        continue

        elif answer=="3":
            print('\nUnder the chair you found a note\n')
            print("Read the note ?")
            print('> Yes (1)\t\t > No (2)')
            answer = input()
            if answer=="1":
                print('The note says :\n')
                print('   Monsters are bogus creatures. They have no existence.\n')
                print('   They are the only enigma of our mind. Once Laila rested\n')
                print('   for an hour on the veranda and saw the other village houses\n')
                print('   and many trees. Soon it was night in the hills. After that\n')
                print('   Laila went to sleep and she dreamed of a strange number\n')
                print('   That number was number 666.\n')
            elif answer=="2":
                continue
            else:
                print("Wrong input")
                

                    
                    

        elif answer=="4":
            print('There is nothing abnormal in the television area.\n')
                
        elif answer=="5":
            room1=True
            room2=False
                
                
                
        elif answer=="6":
            displaybackpack(backpack,player_energy,player_attack)


        elif answer == "1":
            if 'Golden Key' not in backpack:
                print('\nThe door is locked!!\nYou need a key to open that door\n\n')
            else:
                print("You can see some stairs going down\nIts a basement\nYou took the first 3 steps to go check if there is any light in that room\nYou heard some weird voices and immidiately tried to turn back..\nBut the door closed in front of your face and you are stucked there")
                print("A wild creature with wolf body and head like a hawk is aproaching you threw the stairs")
                room2=False
                room4=True
        else:
            print("Wrong input")
    while room4==True:
        print("What will you do ")
        print("> Fight (1)           > Open backpack (3)")
        print("> Give up (2)")
        answer = input()
        if answer=="2":
            print("\n\nAre you sure. This game will end with that option")
            answer2 = input("Y / N :")
            if answer2== "y" or answer2=="Y":
                print("Thanks for your time FAGGOT\n \t\t\t\t\tLOSER!!!!\n At least die with dignity.. NEVER SURRENDER")
                exit() 
            elif answer2=="n" or answer2=="N":
                print("Wise choice")
            else:
                print("You types something wrong go home you are drunk")
        elif answer=="1":
            monster_health,player_energy=fightmonster(player_energy,player_attack,backpack,monster_health)
        elif answer=="3":
            displaybackpack(backpack,player_energy, player_attack)
        else:
            print("Wrong input")
            

        
            



