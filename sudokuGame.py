# import pygame library
import pygame
from samurai import *
# initialise the pygame font
pygame.font.init()
 
# Total window
screen = pygame.display.set_mode((770, 770))

# Title and Icon
pygame.display.set_caption("SAMURAI SUDOKU SOLVER")
 
x = 0
y = 0
dif = 330 / 9
val = 0
# Default Sudoku Board

f = open(r"C:\Users\icell\Desktop\Programlama\Python\SamuraiSudokuSolver\tests\easy1.txt", 'r')
grid=changeTextFileFormat(f)
print(grid)
 
# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 10)
font2 = pygame.font.SysFont("comicsans", 10)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 
# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
 
# Function to draw required lines for making Sudoku grid        
def draw():
    
    # Draw the lines
    for i in range (21):
        for j in range (21):
            if grid[i][j]!= "0" and grid[i][j]!= ".":
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (j * dif, i * dif, dif + 1, dif + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (j * dif + 15, i * dif + 15))
            
    # Draw lines horizontally and verticallyto form grid          
    for i in range(25):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (1050, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 1050), thick) 
    
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:
     
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
            if event.key == pygame.K_RETURN:
                flag2 = 1    
    draw() 
    # Update window
    pygame.display.update() 
 
# Quit pygame window   
pygame.quit()    