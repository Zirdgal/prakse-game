import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Untitled Rhythm Game")
clock = pygame.time.Clock()
running = True
delta_time = 0
NOTE_SIZE = 60
NOTE_SPEED = 400
player_score = 0

font = pygame.font.Font(None, 32)
text = font.render("Score: " + str(player_score), True, "white")

note1 = pygame.Vector2(90, 0)
note2 = pygame.Vector2(242, 0)
note3 = pygame.Vector2(394, 0)
note4 = pygame.Vector2(546, 0)

input1 = pygame.Vector2(90, screen.get_height() / 1.2)
input2 = pygame.Vector2(242, screen.get_height() / 1.2)
input3 = pygame.Vector2(394, screen.get_height() / 1.2)
input4 = pygame.Vector2(546, screen.get_height() / 1.2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("mediumorchid4")

    pygame.draw.circle(screen, "brown2", input1, NOTE_SIZE)
    pygame.draw.circle(screen, "lightgoldenrod", input2, NOTE_SIZE)
    pygame.draw.circle(screen, "lightgreen", input3, NOTE_SIZE)
    pygame.draw.circle(screen, "lightpink2", input4, NOTE_SIZE)

    pygame.draw.circle(screen, "red", note1, NOTE_SIZE)
    pygame.draw.circle(screen, "yellow", note2, NOTE_SIZE)
    pygame.draw.circle(screen, "green", note3, NOTE_SIZE)
    pygame.draw.circle(screen, "pink", note4, NOTE_SIZE)

    screen.blit(text, (screen.get_width()/2.35, screen.get_height() /1.1))

    


    note1.y += NOTE_SPEED * delta_time
    note2.y += NOTE_SPEED * delta_time
    note3.y += NOTE_SPEED * delta_time
    note4.y += NOTE_SPEED * delta_time

    if (note1.y > screen.get_height()):
        note1.y = 0
    
    if (note2.y > screen.get_height()):
        note2.y = 0

    if (note3.y > screen.get_height()):
        note3.y = 0

    if (note4.y > screen.get_height()):
        note4.y = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_score += 1
    if keys[pygame.K_s]:
        player_score += 1
    if keys[pygame.K_a]:
        player_score += 1
    if keys[pygame.K_d]:
        player_score += 1

    

    pygame.display.flip()
    delta_time = clock.tick(60) / 1000 # 60 tps

pygame.quit()
