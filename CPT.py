#Level 1 (Tiffany): Plant tree
# Used pygame template
# TEMPLATE FOR ARROW KEYS FROM (Edited)
#https://www.geeksforgeeks.org/python-moving-an-object-in-pygame/

import pygame

pygame.init()
pygame.font.init()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

plants = [None, None, None, None, None, None]

apple_count = 0
wheat_count = 0

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

clouds = [(0, 100), (160, 100), (320, 100), (480, 100)]
cloud_y = 100
character_x = 30
character_y = 340
soil_width = 40
soil_colour = (53, 33, 0)
soil_y = 400
soil_x_1 = 128
soil_x_2 = 168
vel = 3

# Functions

def draw_text(message, font_size, cords, colour):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(message, True, colour)
    textRect = text.get_rect()
    textRect.center = cords
    screen.blit(text, textRect)


def main_menu():
    while True:
        screen.fill(0,0,0)
        draw_text("WHEAT GAME " + str(wheat_count), 20, (98, 55), (0, 0, 0))
    pygame.display.flip()
    clock.tick(30)
    















def draw_cloud(cloud_x_number):
    cloud_color = (240, 240, 240)
    pygame.draw.rect(screen, cloud_color, [cloud_x_number, cloud_y, 40, 40])
    pygame.draw.rect(screen, cloud_color, [cloud_x_number + 17, cloud_y - 20, 40, 40])
    pygame.draw.rect(screen, cloud_color, [cloud_x_number + 33, cloud_y, 40, 40])

def draw_ground():
    pygame.draw.rect(screen, (0, 158, 96), (0, HEIGHT - 160, WIDTH, 160))
    pygame.draw.rect(screen, (92, 64, 51), [0, 350, 800, 200])
    pygame.draw.rect(screen, (36, 37, 38), [0, 350, 800, 8])

def soil_spacing(n):
    result = n * 80
    return result

def draw_soil():
    for i in range(len(plants)):
        pygame.draw.rect(screen, soil_colour, [soil_x_1 + soil_spacing(i), soil_y, soil_width, soil_width])
        
def plant_seed(seed_type):
    global apple_count, wheat_count
    for i in range(len(plants)):
        if soil_x_1 - 5 + soil_spacing(i) <= character_x <= soil_x_2 + soil_spacing(i):
            if plants[i] == None:  
                if seed_type == "apple":
                    plants[i] = "A"
                    apple_count += 1
                if seed_type == "wheat":
                    plants[i] = "W"
                    wheat_count += 1

def update_clouds(clouds):
    new_clouds = []
    for cloud in clouds:
        cloud_x = cloud[0] + 1
        if cloud_x > WIDTH:
            cloud_x = -90
        new_clouds.append((cloud_x, cloud[1]))
    return new_clouds

def draw_clouds():
    for cloud in clouds:
        draw_cloud(cloud[0])

def draw_character():
    pygame.draw.rect(screen, (0, 62, 101), (character_x + 5, character_y + 25, 35, 60))
    pygame.draw.rect(screen, (0, 62, 101), (character_x, character_y, 45, 40))
    pygame.draw.rect(screen, (224, 172, 105), (character_x + 10, character_y + 12, 25, 20))
    pygame.draw.rect(screen, (0, 101, 62), (character_x + 15, character_y + 20, 5, 5))
    pygame.draw.rect(screen, (0, 101, 62), (character_x + 28, character_y + 20, 5, 5))
    pygame.draw.rect(screen, (198, 134, 66), (character_x + 15, character_y + 28, 15, 2))


level_1 = True
end_level_1 = False

# Track key states

game():
    level_1 = True
    end_level_1 = False
    left_key_pressed = False
    right_key_pressed = False
    a_key_pressed = False
    w_key_pressed = False
    running = True
    while running:
    
        # EVENT HANDLING
        
        pygame.time.delay(10) 
    
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                running = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_key_pressed = True
                elif event.key == pygame.K_RIGHT:
                    right_key_pressed = True
                elif event.key == pygame.K_a:
                    a_key_pressed = True
                elif event.key == pygame.K_w:
                    w_key_pressed = True
    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_key_pressed = False
                elif event.key == pygame.K_RIGHT:
                    right_key_pressed = False
                elif event.key == pygame.K_a:
                    a_key_pressed = False
                elif event.key == pygame.K_w:
                    w_key_pressed = False
    
        if level_1:
            plants_available = False
            for i in range(len(plants)):
                if plants[i] == None:
                    plants_available = True
    
            if not plants_available:
                level_1 = False
                end_level_1 = True
    
            if left_key_pressed and character_x > 0:
                character_x -= vel
    
            if right_key_pressed and character_x < 640 - 40:
                character_x += vel
    
            if a_key_pressed:
                plant_seed("apple")
                a_key_pressed = False  
    
            if w_key_pressed:
                plant_seed("wheat")
                w_key_pressed = False 
    
            clouds = update_clouds(clouds)  
    
            screen.fill((161, 220, 233))
            draw_ground()
            draw_clouds()
            draw_soil()
    
            for i in range(len(plants)):
                if plants[i] == "A":
                    pygame.draw.circle(screen, (255, 0, 0), (soil_x_1 + 20 + soil_spacing(i), soil_y + 20), 4)
    
                if plants[i] == "W":
                    pygame.draw.circle(screen, (255, 255, 0), (soil_x_1 + 20 + soil_spacing(i), soil_y + 20), 4)
    
            draw_character()
            draw_text("Wheat planted: " + str(wheat_count), 20, (98, 55), (0, 0, 0))
            draw_text("Apples planted: " + str(apple_count), 20, (100, 30), (0, 0, 0))
    
        elif end_level_1:
            screen.fill((161, 220, 233))
            clouds = update_clouds(clouds)  
            draw_ground()
            draw_clouds()
            draw_text("Congratulations!", 25, (WIDTH // 2, HEIGHT // 2 - 30), "white")
            draw_text("You have completed Level 1", 25, (WIDTH // 2, HEIGHT // 2), "white")
    
        pygame.display.flip()
        clock.tick(30)
    
pygame.quit()

if __name__ == "__Main__":
    main_menu()
