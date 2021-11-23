from threading import Thread
import pygame
from samurai import *
from multiprocessing import Process
import win32api


pygame.font.init()

screen = pygame.display.set_mode((770, 770))

pygame.display.set_caption("SAMURAI SUDOKU SOLVER")

x = 0
y = 0
dif = 330 / 9
val = 0

f = open(r"C:\Users\z004d20z\Desktop\Programlama\Python\SamuraiSudoku\SamuraiSudokuSolver\tests\easy1.txt", 'r')
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
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_a_for_two_threads_first(values, sqr):
    count = 0
    for i in range(9):
        for j in range(9):
            if(i==4 and j==4):
                return
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_a_for_two_threads_second(values, sqr):
    count = 40
    k=4
    for i in range(4,9):
        if(i!=4):
            k=0
        for j in range(k,9):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_b(values, sqr):
    count = 0
    for i in range(9):
        for j in range(12, 21):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_b_for_two_threads_first(values, sqr):
    count = 0
    for i in range(9):
        for j in range(12, 21):
            if(i==4 and j==16):
                return
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_b_for_two_threads_second(values, sqr):
    count = 40
    k=16
    for i in range(4,9):
        if(i!=4):
            k=12
        for j in range(k, 21):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_c(values, sqr):
    count = 0
    for i in range(12, 21):
        for j in range(9):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_c_for_two_threads_first(values, sqr):
    count = 0
    for i in range(12, 21):
        for j in range(9):
            if(i==16 and j==4):
                return
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update()
            
def draw_c_for_two_threads_second(values, sqr):
    count = 40
    k=4
    for i in range(16, 21):
        if(i!=16):
            k=0
        for j in range(k,9):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_d(values, sqr):
    count = 0
    for i in range(12, 21):
        for j in range(12, 21):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_d_for_two_threads_first(values, sqr):
    count = 0
    for i in range(12, 21):
        for j in range(12, 21):
            if(i==16 and j==16):
                return
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update()

def draw_d_for_two_threads_second(values, sqr):
    count = 40
    k=16
    for i in range(16, 21):
        if(i!=16):
            k=12
        for j in range(k, 21):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update()

def draw_plus(values, sqr):
    count = 0
    for i in range(6, 15):
        for j in range(6, 15):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def draw_plus_for_two_threads_first(values, sqr):
    count = 0
    for i in range(6, 15):
        for j in range(6, 15):
            if(i==10 and j==10):
                return
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update()

def draw_plus_for_two_threads_second(values, sqr):
    count = 40
    k=10
    for i in range(10, 15):
        if(i!=10):
            k=6
        for j in range(k, 15):
            time.sleep(0.1)
            text = font2.render(values[sqr[count]], 10, (0, 255, 0))
            screen.blit(text, (j * dif + 15, i * dif + 15))
            count += 1
            pygame.display.update() 

def display_message(elapsed_time):
    elapsed_time=int(elapsed_time)
    elapsed_time=str(elapsed_time)
    win32api.MessageBox(0, 'GAME IS DONE! It tooks: '+elapsed_time+' seconds.','SUCCESSFULL!')
    time.sleep(3)


ans = solve(grid)
display_samurai(ans)
start_time = time.time()

while True:
    screen.fill((255, 255, 255))
    draw()

    t1=Thread(target=draw_a,args=(ans,square_a,))
    t2=Thread(target=draw_b,args=(ans,square_b,))
    t3=Thread(target=draw_c,args=(ans,square_c,))
    t4=Thread(target=draw_d,args=(ans,square_d,))
    t5=Thread(target=draw_plus,args=(ans,square_mid,))

    t1.start()    
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    pygame.display.update() 
    break

current_time = time.time()
elapsed_time_for_five_threads = current_time - start_time
display_message(elapsed_time_for_five_threads)


ans = solve(grid)
display_samurai(ans)
start_time = time.time()
while True:
    screen.fill((255, 255, 255))
    draw()

    t1=Thread(target=draw_a_for_two_threads_first,args=(ans,square_a,))
    t2=Thread(target=draw_b_for_two_threads_first,args=(ans,square_b,))
    t3=Thread(target=draw_c_for_two_threads_first,args=(ans,square_c,))
    t4=Thread(target=draw_d_for_two_threads_first,args=(ans,square_d,))
    t5=Thread(target=draw_plus_for_two_threads_first,args=(ans,square_mid,))
    t6=Thread(target=draw_a_for_two_threads_second,args=(ans,square_a,))
    t7=Thread(target=draw_b_for_two_threads_second,args=(ans,square_b,))
    t8=Thread(target=draw_c_for_two_threads_second,args=(ans,square_c,))
    t9=Thread(target=draw_d_for_two_threads_second,args=(ans,square_d,))
    t10=Thread(target=draw_plus_for_two_threads_second,args=(ans,square_mid,))

    t1.start()    
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()

    pygame.display.update() 
    break

current_time = time.time()
elapsed_time_for_ten_threads = current_time - start_time
display_message(elapsed_time_for_ten_threads)

pygame.quit()
