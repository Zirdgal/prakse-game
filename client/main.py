import pygame
bsSpawnerTimer = 0
# pygame setup
pygame.init()
screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Untitled Rhythm Game")
clock = pygame.time.Clock()
running = True
delta_time = 0
NOTE_SIZE = 60
NOTE_SPEED = 475
INPUT_COOLDOWN = 20

lane1_input_cooldown = INPUT_COOLDOWN
lane2_input_cooldown = INPUT_COOLDOWN
lane3_input_cooldown = INPUT_COOLDOWN
lane4_input_cooldown = INPUT_COOLDOWN
lane1_input = pygame.Vector2(90, screen.get_height() / 1.2)
lane2_input = pygame.Vector2(242, screen.get_height() / 1.2)
lane3_input = pygame.Vector2(394, screen.get_height() / 1.2)
lane4_input = pygame.Vector2(546, screen.get_height() / 1.2)

player_score = 0
font = pygame.font.Font(None, 32)
text = font.render("Score: " + str(player_score), True, "white")

# note1 = pygame.Vector2(90, 0)
# note2 = pygame.Vector2(242, 0)
# note3 = pygame.Vector2(394, 0)
# note4 = pygame.Vector2(546, 0)

note_list = []
lane1_list = []
lane2_list = []
lane3_list = []
lane4_list = []

# class Notes:
#     def __init__ (self):
#         self.size = NOTE_SIZE
    
#     def create_note (self):
#         Note = pygame.Vector2(90, 0)
#         note_list.append(Note)
#         pygame.draw.circle(screen, "brown2", note, NOTE_SIZE)


#     def draw (self):
#         for note in note_list:
#             pygame.draw.circle(screen, "brown2", note, NOTE_SIZE)

class Note: 
    def __init__ (self, colour, x, y, lane):
        self.size = NOTE_SIZE
        self.colour = colour
        self.pos = pygame.Vector2(x, y)
        self.lane = lane

    def update (self):
        self.pos.y += NOTE_SPEED * delta_time

    def draw (self):
        pygame.draw.circle(screen, self.colour, self.pos, self.size)
    
    def create_note (self):
        Note = pygame.Vector2(self.x, self.y)
        
        pygame.draw.circle(screen, self.colour, Note, self.size)

# inherits from Note class
class Lane1_Note(Note):
    def __init__ (self):
        super().__init__("brown2", 90, 0, 1)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("mediumorchid4")

    pygame.draw.circle(screen, "brown2", lane1_input, NOTE_SIZE)
    pygame.draw.circle(screen, "lightgoldenrod", lane2_input, NOTE_SIZE)
    pygame.draw.circle(screen, "lightgreen", lane3_input, NOTE_SIZE)
    pygame.draw.circle(screen, "lightpink2", lane4_input, NOTE_SIZE)

    # if (note1):
    #     pygame.draw.circle(screen, "red", note1, NOTE_SIZE)
    # if (note2):
    #     pygame.draw.circle(screen, "yellow", note2, NOTE_SIZE)
    # if (note3):
    #     pygame.draw.circle(screen, "green", note3, NOTE_SIZE)
    # if (note4):
    #     pygame.draw.circle(screen, "pink", note4, NOTE_SIZE)

    screen.blit(text, (screen.get_width()/2.35, screen.get_height() /1.1))

    # note1.y += NOTE_SPEED * delta_time
    # note2.y += NOTE_SPEED * delta_time
    # note3.y += NOTE_SPEED * delta_time
    # note4.y += NOTE_SPEED * delta_time

    # if (note1.y > screen.get_height()):
    #     note1.y = 0
    
    # if (note2.y > screen.get_height()):
    #     note2.y = 0

    # if (note3.y > screen.get_height()):
    #     note3.y = 0

    # if (note4.y > screen.get_height()):
    #     note4.y = 0

    

    keys = pygame.key.get_pressed() # this will check every key and return a list of if each key is clicked or not in boolean form
    # 1st note
    if keys[pygame.K_a] == True and lane1_input_cooldown == 0: 
        if (note1.y < lane1_input.y + 100 and note1.y > lane1_input.y - 100):
            player_score += 1
            del note1
        else:
            player_score -= 1
        lane1_input_cooldown = INPUT_COOLDOWN

    # 2nd note
    # if keys[pygame.K_w] == True and lane2_input_cooldown == 0: 
    #     if (note2.y < lane2_input.y + 100 and note2.y > lane2_input.y - 100):
    #         player_score += 1
    #         del note2
    #     else:
    #         player_score -= 1
    #     lane2_input_cooldown = INPUT_COOLDOWN

    # # 3rd note
    # if keys[pygame.K_s] == True and lane3_input_cooldown == 0: 
    #     if (note3.y < lane3_input.y + 100 and note3.y > lane3_input.y - 100):
    #         player_score += 1
    #         del note3
    #     else:
    #         player_score -= 1
    #     lane3_input_cooldown = INPUT_COOLDOWN
    
    # # 4th note
    # if keys[pygame.K_d] == True and lane4_input_cooldown == 0: 
    #     if (note4.y < lane4_input.y + 100 and note4.y > lane4_input.y - 100):
    #         player_score += 1
    #         del note4
    #     else:
    #         player_score -= 1
    #     lane4_input_cooldown = INPUT_COOLDOWN


    if (lane1_input_cooldown > 0):
        lane1_input_cooldown -= 1
    
    # if (lane2_input_cooldown > 0):
    #     lane2_input_cooldown -= 1

    # if (lane3_input_cooldown > 0):
    #     lane3_input_cooldown -= 1

    # if (lane4_input_cooldown > 0):
    #     lane4_input_cooldown -= 1

    if bsSpawnerTimer > 60:
        new_note = Lane1_Note()
        note_list.append(new_note)
        if (new_note.lane == 1 ):
            lane1_list.append(new_note)
        elif (new_note.lane == 2):
            lane2_list.append(new_note)
        elif (new_note.lane == 3):
            lane3_list.append(new_note)
        elif (new_note.lane == 4):
            lane4_list.append(new_note)
        bsSpawnerTimer = 0
    
    bsSpawnerTimer += 1
    print(bsSpawnerTimer)
     
     # the [:] signifies that its a copy of the original list because this snippet of code will delete objects from the actual list - slice notation start:stop:step
    for note in note_list[:]:
        note.update()
        note.draw()

        if (note.pos.y > screen.get_height()):
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

pygame.quit()
