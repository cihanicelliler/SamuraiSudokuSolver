from threading import Thread
import pygame
from samurai import *
from multiprocessing import Process

pygame.font.init()

screen = pygame.display.set_mode((770, 770))

pygame.display.set_caption("SAMURAI SUDOKU SOLVER")

x = 0
y = 0
dif = 330 / 9
val = 0

f = open(r"C:\Users\icell\Desktop\Programlama\Python\SamuraiSudokuSolver\tests\easy1.txt", 'r')
grid = changeTextFileFormat(f)

font1 = pygame.font.SysFont("comicsans", 10)
font2 = pygame.font.SysFont("comicsans", 10, True)


def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)
                                               * dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif,
                                               y * dif), ((x + i) * dif, y * dif + dif), 7)

def draw():
    
    for i in range(21):
        for j in range(21):

            if grid[i][j] == ".":
                pygame.draw.rect(screen, (20, 20, 31),
                                 (j * dif, i * dif, dif + 1, dif + 1))
            if grid[i][j] != "0" and grid[i][j] != ".":
                pygame.draw.rect(screen, (0, 153, 153),
                                 (j * dif, i * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (j * dif + 15, i * dif + 15))

    for i in range(25):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif),
                         (1050, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0),
                         (i * dif, 1050), thick)


def draw_a(values, sqr):
    count = 0
    for i in range(9):
        for j in range(9):
            time.sleep(1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            print("a")
            pygame.display.update() 


def draw_b(values, sqr):
    count = 0
    for i in range(9):
        for j in range(12, 21):
            time.sleep(1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            print("b")
            pygame.display.update() 


def draw_c(values, sqr):
    count = 0
    for i in range(12, 21):
        for j in range(9):
            time.sleep(1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            print("c")
            pygame.display.update() 


def draw_d(values, sqr):
    count = 0
    for i in range(12, 21):
        for j in range(12, 21):
            time.sleep(1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            print("d")
            pygame.display.update() 


def draw_plus(values, sqr):
    count = 0
    for i in range(6, 15):
        for j in range(6, 15):
            time.sleep(1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            print("plus")
            pygame.display.update() 

run = True
flag2 = 0
ans = solve(grid)
display_samurai(ans)

while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            if event.key == pygame.K_RETURN:
                flag2 = 1
    draw()
    t1=Thread(target=draw_a,args=(ans,square_a,)).start()
    t2=Thread(target=draw_b,args=(ans,square_b,)).start()
    t3=Thread(target=draw_c,args=(ans,square_c,)).start()
    t4=Thread(target=draw_d,args=(ans,square_d,)).start()
    t5=Thread(target=draw_plus,args=(ans,square_mid,)).start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    pygame.display.update() 

pygame.quit()
