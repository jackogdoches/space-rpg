import sys
import time
import random

# Slowprint
def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)

# Line break (no pause)
def sbr():
    print("")

# Line break (pause)
def br():
    print("")
    bent = input("[Press enter to continue...]")
    print("")

# Load save file
def loadGame(filename):
    with open(f"{filename}.csv") as saveGame:
        readList = []

        cLine = 0
        for line in saveGame:
            if cLine != 0:
                readList.append(line)
            cLine += 1

        readDict = {}
        cItem = 0
        for item in readList:
            cidx = item.find(',')
            bc = item[:cidx]
            ac = item[cidx + 1:]
            if cItem != 8:
                pidx = ac.find('\n')
                ac = ac[:pidx]
            if cItem < 2:
                readDict[bc] = ac
            if cItem > 1:
                readDict[bc] = int(ac)
            cItem += 1

        return readDict

#Create new save file (character creation)
def saveChar(localDict, localName):
    with open(f"{localName}.csv", "w") as newSaveFile:
        newSaveFile.write(f"KEY,VALUE\nName,{localDict['Name']}\nClass,{localDict['Class']}\nHealth,100\nWealth,500\nPhysical,{localDict['Physical']}\nMental,{localDict['Mental']}\nSocial,{localDict['Social']}\nTechnical,{localDict['Technical']}\ngameStage,1")

#Update save file
def saveGame(localDict, localName):
    with open(f"{localName}.csv", "w") as saveFile:
        saveFile.write("KEY,VALUE\n")
        dEnd = len(localDict) - 1
        dCount = 0
        for key in localDict:
            if dCount != dEnd:
                saveFile.write(f"{key},{localDict[key]}\n")
            else:
                saveFile.write(f"{key},{localDict[key]}")
            dCount += 1

#Set attribute points (character creation)
def setAttributes():
    while True:
        attrDict = {}
        attrPoints = 25

        while True:
            sprint(f"[You have {attrPoints} attribute points remaining.]")
            sprint("[Physical: Determines your aptitude for challenges of strength and endurance.]")
            physInput = int(input("[Enter your Physical] "))
            if physInput > 10 or physInput < 0:
                sprint("[Invalid entry! Entries must be greater than 0 and less than 10.]")
            else:
                attrPoints -= physInput
                attrDict['Physical'] = physInput
            break
        
        print("")

        while True:
            sprint(f"[You have {attrPoints} attribute points remaining.]")
            sprint("[Mental: Determines your aptitude for challenges of intelligence and reasoning.]")
            mentInput = int(input("[Enter your Mental] "))
            if mentInput > 10 or mentInput < 0:
                sprint("[Invalid entry! Entries must be greater than 0 and less than 10.]")
            else:
                attrPoints -= mentInput
                attrDict['Mental'] = mentInput
            break

        print("")

        while True:
            sprint(f"[You have {attrPoints} attribute points remaining.]")
            sprint("[Social: Determines your aptitude for challenges of coercian and persuasion.]")
            sociInput = int(input("[Enter your Social] "))
            if sociInput > 10 or sociInput < 0:
                sprint("[Invalid entry! Entries must be greater than 0 and less than 10.]")
            else:
                attrPoints -= sociInput
                attrDict['Social'] = sociInput
            break
        
        print("")

        while True:
            sprint(f"[You have {attrPoints} attribute points remaining.]")
            sprint("[Technical: Determines your aptitude for challenges of computer and machine usage.]")
            techInput = int(input("[Enter your Technical] "))
            if techInput > 10 or techInput < 0:
                sprint("[Invalid entry! Entries must be greater than 0 and less than 10.]")
            else:
                attrPoints -= techInput
                attrDict['Technical'] = techInput
            break
    
        if attrPoints < 0:
            print("")
            sprint("[Your total attribute points cannot exceed 25! You must restart points assignment.]")
            print("")
            continue
        else:
            break
    return attrDict

# Dice roll
def roll(Attribute, pcAttributeValue):
    dice = random.randint(1, 100)
    diceRoll = dice + (2 * pcAttributeValue)
    if diceRoll > 50:
        sprint(f"[{Attribute} check passed: {diceRoll}/100]")
        return True
    else:
        sprint(f"[{Attribute} check failed: {diceRoll}/100]")
        return False

# Setting initial game conditions
gameState = True
gameStage = 0
menuState = True

# Main code line
while gameState == True:
    while menuState == True:
        menuChoice = int(input("[Type 1 to start a new game or type 2 to load a saved game] "))
        print("")
        if menuChoice == 1:
            localPCD = {}
            menuState = False
        if menuChoice == 2:
            loadName = input("[Type in your character's name--CASE SENSITIVE!] ")
            print("")
            localPCD = loadGame(loadName)
            sprint(f"Welcome back, {localPCD['Name']}!")
            print("")
            print("")
            gameStage = localPCD['gameStage']
            menuState = False
    
    if gameStage == 0:
        print("")
        print("")
        sprint("Your dreams make little sense to you. There is a thundrous, booming noise before deafening silence. The feeling of extreme cold seizes you instantly. Your view fades to black...")
        br()
        sprint("Your eyes open to a medium-sized, white-walled room lined with beds. You are lying in one of them. It appears you are inside of a clinic or hospital.")
        br()
        sprint("A tall man in a white coat approaches your bedside. He has pale white skin and hair almost as pigmentless. His gaunt face and red eyes move with surprise as he sees you awake for the first time.")
        br()
        sprint("[Doctor]: 'Oh! You're awake! To tell you the truth, I didn't think you would wake up. Explosive decompression is usually quite the killer. I suppose your arriving comatose was a sign that you might make it though.'")
        br()
        sprint("You understand the man's words, but you don't know why. You probe your lips with your tongue; everything is still there, but you don't seem able to bring any of your own words out. You look frantically around at your immediate surroundings, but find nothing capable of hindering your speech.")
        br()
        sprint("[Doctor]: 'Hey, hey... take it easy! You might be suffering from acute amnesia, so why don't we start with something simple. Can you try and tell me your name?'")
        print("")
        while True:
            nameEntry = input("After some struggling, you manage to say... [Type in your name] ")
            if len(nameEntry) > 0:
                localPCD['Name'] = nameEntry
                break
            else:
                print("")
                print("[Your name cannot be blank!]")
                print("")
        print("")
        sprint(f"[Doctor]: '{localPCD['Name']}, you say? Okay, this is good, you haven't totally lost your ability to speak. Let's try something else. Do you remember the job you had before the accident?'")
        print("")
        while True:
            classEntry = input("After thinking it over, you remember you were a... [Type in your class] ")
            if len(classEntry) > 0:
                localPCD['Class'] = classEntry
                break
            else:
                print("")
                print("[Your class cannot be blank!]")
                print("")
        localPCD['Health'] = 100
        localPCD['Wealth'] = 500
        print("")
        sprint("[Doctor]: 'Interesting. Try and tell me about your job. What kind of skills did you have?'")
        print("")
        sprint("[You will now assign your attribute points. There are four attributes: Physical, Mental, Social, and Technical.]")
        br()
        sprint("[You have a total of 25 points to assign to your attributes. Each attribute influences your success chances for attribute-based dice rolls.]")
        sprint("[Your individual attributes cannot exceed 10 points each. You will get another opportunity to assign them before the first stage is over.]")
        br()
        readAttrDict1 = setAttributes()
        localPCD['Physical'] = readAttrDict1['Physical']
        localPCD['Mental'] = readAttrDict1['Mental']
        localPCD['Social'] = readAttrDict1['Social']
        localPCD['Technical'] = readAttrDict1['Technical']
        br()
        sprint("[Doctor]: 'You're doing great! Now, you should rest for a bit longer and I need to confirm these scans, so let's review the information you provided me...'")
        br()

        finalizeReview = 9
        while finalizeReview != 0:
            sprint(f"Name: {localPCD['Name']}")
            sprint(f"Class: {localPCD['Class']}")
            sprint(f"Attributes: ")
            sprint(f" *Physical: {localPCD['Physical']}")
            sprint(f" *Mental: {localPCD['Mental']}")
            sprint(f" *Social: {localPCD['Social']}")
            sprint(f" *Technical: {localPCD['Technical']}")
            print("")
            finalizeReview = int(input("[Type 0 to confirm character or 1 to edit] "))
            if finalizeReview != 0:
                reviewCmd = 9
                while reviewCmd != 0:
                    print("")
                    reviewCmd = int(input("[Type 1 to edit Name, 2 to edit Class, 3 to revise Attributes, or 0 to refresh review.] "))
                    if reviewCmd == 1:
                        newName = input("[Type in your new name] ")
                        localPCD['Name'] = newName
                    if reviewCmd == 2:
                        newClass = input("[Type in your new class] ")
                        localPCD['Class'] = newClass
                    if reviewCmd == 3:
                        readAttrDict2 = setAttributes()
                        localPCD['Physical'] = readAttrDict2['Physical']
                        localPCD['Mental'] = readAttrDict2['Mental']
                        localPCD['Social'] = readAttrDict2['Social']
                        localPCD['Technical'] = readAttrDict2['Technical']

        br()
        sprint(f"[Doctor]: 'Okay then, {localPCD['Name']}, your scans look good, but I need to keep you for at least one more night for observation--just in case anything changes...'")
        br()
        sprint("[You have completed character creation! You are about to see the first checkpoint: you can save your character by pressing 1 or continue until the next checkpoint without saving by pressing 0.]")
        print("")

        while True:
            checkPoint1 = int(input("[Checkpoint: type 1 to save or 0 to continue without saving] "))
            localPCD['gameStage'] = 1
            if checkPoint1 == 1:
                saveChar(localPCD, localPCD['Name'])
                sbr()
                break
            if checkPoint1 == 0:
                sbr()
                break
            else:
                sbr()
                print("[Invalid input!]")
                sbr()
                
        
        gameStage = 1

    if gameStage == 1:
        sprint("The rest of the day passes slowly, leaving you to your thoughts. Your dreams are much more interesting than your waking thoughts. You find yourself walking through the halls of a large space ship.")
        br()
        sprint("The corridor curves endlessly upwards in front of you, a necessary feature of the cabin compartment's pseudo-gravity. Your ears tingle slightly as you think about your body's proper motion and you rub at the tiny scar on the back of your ear where the stabilizing implant was inserted.")
        br()
        sprint("You feel like you are going somewhere important on this ship, but you can't remember why you're there. Before you can conjure up an image of your goal, you are thrust back into the waking world...")
        br()
        sprint("You are back in your clinic bed, but noone is in the room with you. After a moment, you hear a familiar voice coming from an intercom by the door.")
        br()
        sprint(f"[Doctor's voice]: 'Ah, good morning {localPCD['Name']}! So, it turns out you have quite the warrant for your arrest! Unfortunately, I'm going to have to keep you locked in there until the Guards come get you. So sorry about the straps! Anyways, good luck in court!'")
        br()
        sprint("The intercom goes silent, and you suddenly notice there are restraints strapping you to the bed that weren't there yesterday. You move your arms and legs, but mere wiggling won't get these off.")
        br()
        sprint("[You are about to make your first choice! To select a choice, type in the number specificed next to action when prompted. Each choice you make takes your story in a certain direction, even if you fail the roll, so choose wisely!]")
        br()

        sprint("You surveil the room you're in. After some thought you decide to...")
        sbr()
        sprint("[1] Attempt to force your way out of the restraints [Physical]")
        sprint("[2] Plead with the Doctor via the intercom [Social]")
        sprint("[3] Patiently await the arrival of the Guards")
        sbr()

        while True:
            c000 = int(input("[Enter choice number] "))
            if c000 == 1:
                break
            if c000 == 2:
                break
            if c000 == 3:
                break
            else:
                sbr()
                print("[Invalid entry! Try again] ")
                sbr()
        
        if c000 == 1:
            sbr()
            r000 = roll('Physical', localPCD['Physical'])
            sbr()
            if r000 == True:
                sprint("You force your way through the restraints!")
            else:
                sprint("You fail to break out of the restraints!")
        
        if c000 == 2:
            sbr()
            r000 = roll('Social', localPCD['Social'])
            sbr()
            if r000 == True:
                sprint("After a moment, you hear a tired sigh from the intercom and the Doctor enters the room!")
            else:
                sprint("There is no response from the intercom!")
        
        if c000 == 3:
            sbr()
            sprint("After several minutes pass, robot Guards enter the room!")
        br()

        if c000 == 1:
            if r000 == True:
                sprint("[Doctor's voice]: 'Hey! What are you doing! If you don't stop that right now I'll--'")
                sbr()
                sprint("Disregarding the Doctor's voice, you manage to disconnect yourself from the monitors and quickly scan the room for anything that might aide in your escape.")
                br()
                sprint("It's in this moment you realize you have no idea how you will manage to escape this clinic, less even where you are at all! And then, before another thought crosses your mind, you suddenly feel uncontrollably, violently nauseous!")
                br()
                sprint("Writhing on the floor of the clinic, it takes all of your might to stop yourself from vomiting. You feel the familiar sensation of g-force in your stomach, but the force is pressing you down and towards the back of the room. Before long, the Doctor enters your clinic room.")
                br()
                sprint("[Doctor]: 'I didn't WANT to do that, but you didn't really give me any choice!'")
            if r000 == False:
                continue
        
        if c000 == 2:
            if r000 == True:
                continue
            if r000 == False:
                continue
        
        if c000 == 3:
            continue

    break