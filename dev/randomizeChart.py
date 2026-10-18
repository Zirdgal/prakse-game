import os
import random

root = os.getcwd()

SONG_ID_SELECTED = 2
song = open(root + "/client/charts/" + str(SONG_ID_SELECTED) + "/song.txt", "r")
songContent = song.readlines()
songMaxLines = 1
songMaxLines = len(songContent)

copyOfSongContent = []

song.close()

for lane in songContent:
    itemCounter = 0
    for item in lane:
        if (itemCounter == 0 and item == "0"):
            noteCount = 0
            newLane = ""

            # will it be a double or single note:
            if (random.randint(1,10) > 3):
                #single note 70% chance
                noteCount = 1
                notePlace = random.randint(0,3)
                print("single")
                for i in range(4):
                    print(i, notePlace)
                    if(i == notePlace):
                        newLane += "0"
                    else: 
                        newLane += "."
            else:
                #double note 30% chance
                noteCount = 2
                notePos = random.sample(range(4), 2) # this returns a list e.g. [0, 1] or [2, 3] 
                print("double")
                for i in range(4):
                    if(i==notePos[0] or i == notePos[1]):
                        newLane += "0"
                    else:
                        newLane += "."
            copyOfSongContent.append(newLane)

            print(newLane)
        elif (itemCounter == 0):
            copyOfSongContent.append("....")
        else:
            break

        itemCounter+= 1
    
        

# save to file
with open(root + "/client/charts/" + str(SONG_ID_SELECTED) + "/song.txt", "w") as song:
    for line in copyOfSongContent:
        song.write(line + "\n")

song.close()
