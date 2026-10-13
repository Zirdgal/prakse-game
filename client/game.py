import pygame
import os

# bsSpawnerTimer = 1
# pygame setup
pygame.init()
screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Untitled Rhythm Game")
clock = pygame.time.Clock()
running = True
songOver = False
delta_time = 0
NOTE_SIZE = 60
NOTE_SPEED = 475
INPUT_COOLDOWN = 20

player_score = 0
font = pygame.font.Font(None, 32)
text = font.render("Score: " + str(player_score), True, "white")

lane1_input_cooldown = INPUT_COOLDOWN
lane2_input_cooldown = INPUT_COOLDOWN
lane3_input_cooldown = INPUT_COOLDOWN
lane4_input_cooldown = INPUT_COOLDOWN
lane1_input = pygame.Vector2(90, screen.get_height() / 1.2)
lane2_input = pygame.Vector2(242, screen.get_height() / 1.2)
lane3_input = pygame.Vector2(394, screen.get_height() / 1.2)
lane4_input = pygame.Vector2(546, screen.get_height() / 1.2)
lane1_input_text = font.render("A", True, "white")
lane2_input_text = font.render("W", True, "white")
lane3_input_text = font.render("S", True, "white")
lane4_input_text = font.render("D", True, "white")


# files 
path = os.path.realpath(__file__)
direc = os.path.dirname(path)
song = open(direc + "/charts/song1.txt", "r")
content = song.readlines()

print(content)
print("2nd line")
print(content[1])


songSpeed = 10
songSpeedCounter = 1
songLineCounter = 1
songMaxLines = len(content)

# note1 = pygame.Vector2(90, 0)
# note2 = pygame.Vector2(242, 0)
# note3 = pygame.Vector2(394, 0)
# note4 = pygame.Vector2(546, 0)

note_list = []
lane1_list = []
lane2_list = []
lane3_list = []
lane4_list = []

class Note: 
    def __init__ (self, colour, x, y, lane):
        self.size = NOTE_SIZE
        self.colour = colour
        self.x = x
        self.y = y
        self.lane = lane

    def update (self):
        self.y += NOTE_SPEED * delta_time

    def draw (self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
    
    def create_note (self):
        Note = pygame.Vector2(self.x, self.y)
        
        pygame.draw.circle(screen, self.colour, Note, self.size)

# inherits from Note class
class Lane1_Note(Note):
    def __init__ (self):
        super().__init__("red", 90, 0, 1)

class Lane2_Note(Note):
    def __init__ (self):
        super().__init__("yellow", 242, 0, 2)
    
class Lane3_Note(Note):
    def __init__ (self):
        super().__init__("green", 394, 0, 3)

class Lane4_Note(Note):
    def __init__ (self):
        super().__init__("pink", 546, 0, 4)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if songOver:
        endingText = font.render("You finished with a score of: " + str(player_score), True, "white")
        screen.blit(endingText, (screen.get_width()/4, screen.get_height()/2))
        pass
        
    else:
    
        screen.fill("mediumorchid4")

        pygame.draw.circle(screen, "brown2", lane1_input, NOTE_SIZE)
        pygame.draw.circle(screen, "lightgoldenrod", lane2_input, NOTE_SIZE)
        pygame.draw.circle(screen, "lightgreen", lane3_input, NOTE_SIZE)
        pygame.draw.circle(screen, "lightpink2", lane4_input, NOTE_SIZE)

        screen.blit(lane1_input_text, (90, screen.get_height() / 1.2))
        screen.blit(lane2_input_text, (242, screen.get_height() / 1.2))
        screen.blit(lane3_input_text, (394, screen.get_height() / 1.2))
        screen.blit(lane4_input_text, (546, screen.get_height() / 1.2))

        screen.blit(text, (screen.get_width()/2.35, screen.get_height() /1.1))

    keys = pygame.key.get_pressed() # this will check every key and return a list of if each key is clicked or not in boolean form
    # 1st note
    if keys[pygame.K_a] == True and lane1_input_cooldown == 0 and len(lane1_list) > 0: 
        lane_note = None
        highestY = -1
        for note in lane1_list:
            if (note.y > highestY):
                highestY = note.y
                lane_note = note

        if (lane_note and lane_note.y < lane1_input.y + 100 and lane_note.y > lane1_input.y - 100):
            player_score += 1
            
            lane1_list.remove(lane_note)
            note_list.remove(lane_note)
        else:
            player_score -= 1
        lane1_input_cooldown = INPUT_COOLDOWN

   # 2nd note
    if keys[pygame.K_w] == True and lane2_input_cooldown == 0: 
        lane_note = None
        highestY = -1
        for note in lane2_list:
            if (note.y > highestY):
                highestY = note.y
                lane_note = note

        if (lane_note and lane_note.y < lane2_input.y + 100 and lane_note.y > lane2_input.y - 100):
            player_score += 1
            
            lane2_list.remove(lane_note)
            note_list.remove(lane_note)
        else:
            player_score -= 1
        lane2_input_cooldown = INPUT_COOLDOWN

    # 3rd note
    if keys[pygame.K_s] == True and lane3_input_cooldown == 0: 
        lane_note = None
        highestY = -1
        for note in lane3_list:
            if (note.y > highestY):
                highestY = note.y
                lane_note = note

        if (lane_note and lane_note.y < lane3_input.y + 100 and lane_note.y > lane3_input.y - 100):
            player_score += 1
            
            lane3_list.remove(lane_note)
            note_list.remove(lane_note)
        else:
            player_score -= 1
        lane3_input_cooldown = INPUT_COOLDOWN
    
    # 4th note
    if keys[pygame.K_d] == True and lane4_input_cooldown == 0: 
        lane_note = None
        highestY = -1
        for note in lane4_list:
            if (note.y > highestY):
                highestY = note.y
                lane_note = note

        if (lane_note and lane_note.y < lane4_input.y + 100 and lane_note.y > lane4_input.y - 100):
            player_score += 1
            
            lane4_list.remove(lane_note)
            note_list.remove(lane_note)
        else:
            player_score -= 1
        lane4_input_cooldown = INPUT_COOLDOWN


    if (lane1_input_cooldown > 0):
        lane1_input_cooldown -= 1
    
    if (lane2_input_cooldown > 0):
        lane2_input_cooldown -= 1

    if (lane3_input_cooldown > 0):
        lane3_input_cooldown -= 1

    if (lane4_input_cooldown > 0):
        lane4_input_cooldown -= 1

    ###NOTE SPAWNING

    if songSpeedCounter > songSpeed:

        if (songLineCounter >= songMaxLines):
            if (len(note_list) > 0):
                pass
            else:
                songOver = True
        else:
            #print(content[songLineCounter])
            j = 0
            for i in content[songLineCounter]:

                if (i == "0"):
                    if (j == 0):
                        new_note = Lane1_Note()
                        note_list.append(new_note)
                        lane1_list.append(new_note)
                    elif (j == 1):
                        new_note = Lane2_Note()
                        note_list.append(new_note)
                        lane2_list.append(new_note)
                    elif (j == 2):
                        new_note = Lane3_Note()
                        note_list.append(new_note)
                        lane3_list.append(new_note)
                    elif (j == 3):
                        new_note = Lane4_Note()
                        note_list.append(new_note)
                        lane4_list.append(new_note)
                j += 1


            songLineCounter += 1
            songSpeedCounter = 0


    songSpeedCounter += 1

    # if bsSpawnerTimer % 60 == 0:
    #     new_note = Lane1_Note()
    #     note_list.append(new_note)
    #     if (new_note.lane == 1 ):
    #         lane1_list.append(new_note)
    #     elif (new_note.lane == 2):
    #         lane2_list.append(new_note)
    #     elif (new_note.lane == 3):
    #         lane3_list.append(new_note)
    #     elif (new_note.lane == 4):
    #         lane4_list.append(new_note)
    
    # if bsSpawnerTimer % 80 == 0:
    #     new_note = Lane2_Note()
    #     note_list.append(new_note)
    #     if (new_note.lane == 1 ):
    #         lane1_list.append(new_note)
    #     elif (new_note.lane == 2):
    #         lane2_list.append(new_note)
    #     elif (new_note.lane == 3):
    #         lane3_list.append(new_note)
    #     elif (new_note.lane == 4):
    #         lane4_list.append(new_note)
    
        
    # if bsSpawnerTimer % 100 == 0:
    #     new_note = Lane3_Note()
    #     note_list.append(new_note)
    #     if (new_note.lane == 1 ):
    #         lane1_list.append(new_note)
    #     elif (new_note.lane == 2):
    #         lane2_list.append(new_note)
    #     elif (new_note.lane == 3):
    #         lane3_list.append(new_note)
    #     elif (new_note.lane == 4):
    #         lane4_list.append(new_note)
    
        
    # if bsSpawnerTimer % 120 == 0:
    #     new_note = Lane4_Note()
    #     note_list.append(new_note)
    #     if (new_note.lane == 1 ):
    #         lane1_list.append(new_note)
    #     elif (new_note.lane == 2):
    #         lane2_list.append(new_note)
    #     elif (new_note.lane == 3):
    #         lane3_list.append(new_note)
    #     elif (new_note.lane == 4):
    #         lane4_list.append(new_note)
    

    # if bsSpawnerTimer > 1000:
    #     bsSpawnerTimer = 1
    # bsSpawnerTimer += 1

    

     
     # the [:] signifies that its a copy of the original list because this snippet of code will delete objects from the actual list - slice notation start:stop:step
    for note in note_list[:]:
        note.update()
        note.draw()

        if (note.y > screen.get_height()):
            player_score -= 1
            note_list.remove(note)
            if (note.lane == 1 ):
                lane1_list.remove(note)
            elif (note.lane == 2):
                lane2_list.remove(note)
            elif (note.lane == 3):
                lane3_list.remove(note)
            elif (note.lane == 4):
                lane4_list.remove(note)
    
    text = font.render("Score: " + str(player_score), True, "white")
    pygame.display.flip()
    
    delta_time = clock.tick(60) / 1000 # 60 tps

song.close()
pygame.quit()
