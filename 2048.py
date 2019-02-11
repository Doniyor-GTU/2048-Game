import pygame
import time
import copy
from random import choice, randint
pygame.init()

pygame.display.set_caption('2048')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color_2 = (211,211,211)
grey2 = (145,138,127)
color_0 = (210,192,231)
color_4 = (229,208,172)

box_size = 60
display_x = 350
display_y = 600
n_x_n = 4

FPS = 30


x_axes = [40,105,170,235]
y_axes = [260,325,390,455]


num_img = pygame.image.load('num_2.png')

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_x,display_y))


class Boxes:


    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.img = 'num_'+str(i)+'.png'
        self.value = i

    def zero(self):
        self.value = 0


def canMove(boxes):
    boxes_transpose = [[row[col] for row in boxes] for col in range(4)]

    for row in boxes:
        for j in range(3):
            if row[j].value == row[j+1].value:
                return True

    for row in boxes_transpose:
        for j in range(3):
            if row[j].value == row[j+1].value:
                return True

    return False


def isGameOver(boxes):
    k = 0
    for row in boxes:
        for j in row:
            if j.value != 0:
                k += 1
    if k == 16 and not canMove(boxes):
        return True

    return False




def left(boxes,backstep):

    backstep = copy.deepcopy(boxes)
    m = 0
    l = 0
    k = 0
    change = False

    while k<4:
        for row in boxes:
            for j in range(3):
                if (row[j].value == 0) and (row[j+1].value != 0) :
                    row[j].value = row[j+1].value
                    row[j+1].value = 0
                    row[j].img = row[j+1].img
                    row[j+1].img = 'num_0.png'
                    l += 1
        k += 1

    for row in boxes:
        for j in range(3):
            if (row[j].value != 0) and (row[j].value == row[j+1].value):
                row[j].value += row[j+1].value
                row[j+1].value = 0
                row[j].img = 'num_'+str(row[j].value)+'.png'
                row[j+1].img = 'num_0.png'
                m += 1

    k = 0

    while k<4:
        for row in boxes:
            for j in range(3):
                if (row[j].value == 0) and (row[j+1].value != 0) :
                    row[j].value = row[j+1].value
                    row[j+1].value = 0
                    row[j].img = row[j+1].img
                    row[j+1].img = 'num_0.png'
                    l += 1
        k += 1

    while  l>=1 or m>=1:
        row = choice([0,1,2,3])
        j = choice([0,1,2,3])
        value = choice([2,4])
        if boxes[row][j].value == 0:
            boxes[row][j].value = value
            boxes[row][j].img = 'num_'+str(value)+'.png'
            l = 0
            m = 0

    return boxes,backstep

def right(boxes,backstep):
    backstep = copy.deepcopy(boxes)



    m = 0
    l = 0
    k = 0

    while k<4:
        for row in boxes:
            for j in range(3,0,-1):
                if (row[j].value == 0) and (row[j-1].value != 0) :
                    row[j].value = row[j-1].value
                    row[j-1].value = 0
                    row[j].img = row[j-1].img
                    row[j-1].img = 'num_0.png'
                    l += 1
        k += 1

    for row in boxes:
        for j in range(3,0,-1):
            if (row[j].value != 0) and (row[j].value == row[j-1].value):
                row[j].value += row[j-1].value
                row[j-1].value = 0
                row[j].img = 'num_'+str(row[j].value)+'.png'
                row[j-1].img = 'num_0.png'
                m += 1
    k = 0

    while k<4:
        for row in boxes:
            for j in range(3,0,-1):
                if (row[j].value == 0) and (row[j-1].value != 0) :
                    row[j].value = row[j-1].value
                    row[j-1].value = 0
                    row[j].img = row[j-1].img
                    row[j-1].img = 'num_0.png'
                    l += 1
        k += 1

    while  l>=1 or m>=1:
        row = choice([0,1,2,3])
        j = choice([0,1,2,3])
        value = choice([2,4])
        if boxes[row][j].value == 0:
            boxes[row][j].value = value
            boxes[row][j].img = 'num_'+str(value)+'.png'
            l = 0
            m = 0


    return boxes,backstep

def up(boxes,backstep):

    backstep = copy.deepcopy(boxes)
    boxes_transpose = [[row[col] for row in boxes] for col in range(4)]
    m = 0
    l = 0
    k = 0
    change = False

    while k<4:
        for row in boxes_transpose:
            for j in range(3):
                if (row[j].value == 0) and (row[j+1].value != 0) :
                    row[j].value = row[j+1].value
                    row[j+1].value = 0
                    row[j].img = row[j+1].img
                    row[j+1].img = 'num_0.png'
                    l += 1
        k += 1

    for row in boxes_transpose:
        for j in range(3):
            if (row[j].value != 0) and (row[j].value == row[j+1].value):
                row[j].value += row[j+1].value
                row[j+1].value = 0
                row[j].img = 'num_'+str(row[j].value)+'.png'
                row[j+1].img = 'num_0.png'
                m += 1
    k = 0

    while k<4:
        for row in boxes_transpose:
            for j in range(3):
                if (row[j].value == 0) and (row[j+1].value != 0) :
                    row[j].value = row[j+1].value
                    row[j+1].value = 0
                    row[j].img = row[j+1].img
                    row[j+1].img = 'num_0.png'
                    l += 1
        k += 1

    while  l>=1 or m >= 1:
        row = choice([0,1,2,3])
        j = choice([0,1,2,3])
        value = choice([2,4])
        if boxes[row][j].value == 0:
            boxes[row][j].value = value
            boxes[row][j].img = 'num_'+str(value)+'.png'
            l = 0
            m = 0

    return boxes,backstep

def down(boxes,backstep):


    backstep = copy.deepcopy(boxes)

    boxes_transpose = [[row[col] for row in boxes] for col in range(4)]
    m = 0
    l = 0
    k = 0

    while k<4:
        for row in boxes_transpose:
            for j in range(3,0,-1):
                if (row[j].value == 0) and (row[j-1].value != 0) :
                    row[j].value = row[j-1].value
                    row[j-1].value = 0
                    row[j].img = row[j-1].img
                    row[j-1].img = 'num_0.png'
                    l += 1
        k += 1

    for row in boxes_transpose:
        for j in range(3,0,-1):
            if (row[j].value != 0) and (row[j].value == row[j-1].value):
                row[j].value += row[j-1].value
                row[j-1].value = 0
                row[j].img = 'num_'+str(row[j].value)+'.png'
                row[j-1].img = 'num_0.png'
                m += 1
    k = 0

    while k<4:
        for row in boxes_transpose:
            for j in range(3,0,-1):
                if (row[j].value == 0) and (row[j-1].value != 0) :
                    row[j].value = row[j-1].value
                    row[j-1].value = 0
                    row[j].img = row[j-1].img
                    row[j-1].img = 'num_0.png'
                    l += 1
        k += 1

    while  l>=1 or m >= 1:
        row = choice([0,1,2,3])
        j = choice([0,1,2,3])
        value = choice([2,4])
        if boxes[row][j].value == 0:
            boxes[row][j].value = value
            boxes[row][j].img = 'num_'+str(value)+'.png'
            l = 0
            m = 0
    return boxes,backstep


def main():

    gameExit = False
    gameOver = False
    x = 0
    y = 0
    add_x = 170
    add_y = 260


    a13 = Boxes(170,260,0)
    a11 = Boxes(40,260,0)
    a12 = Boxes(105,260,0)
    a14 = Boxes(235,260,0)
    a21 = Boxes(40,325,0)
    a22 = Boxes(105,325,0)
    a23 = Boxes(170,325,0)
    a24 = Boxes(235,325,0)
    a31 = Boxes(40,390,0)
    a32 = Boxes(105,390,0)
    a33 = Boxes(170,390,0)
    a34 = Boxes(235,390,0)
    a41 = Boxes(40,455,0)
    a42 = Boxes(105,455,0)
    a43 = Boxes(170,455,0)
    a44 = Boxes(235,455,0)




    boxes = [[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]]

    backstep = [[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]]


    i = 0
    while i<2:
        row = choice([0,1,2,3])
        j = choice([0,1,2,3])
        value = choice([2,4])
        if boxes[row][j].value == 0:
            boxes[row][j].value = value
            boxes[row][j].img = 'num_'+str(value)+'.png'
            i += 1



    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    boxes, backstep = right(boxes,backstep)

                if event.key == pygame.K_LEFT:
                    boxes, backstep = left(boxes,backstep)

                if event.key == pygame.K_UP:
                    boxes, backstep = up(boxes,backstep)

                if event.key == pygame.K_DOWN:
                    boxes, backstep = down(boxes,backstep)

                if event.key == pygame.K_r:
                    main()

                if event.key == pygame.K_b:
                    boxes = backstep




            if event.type == pygame.QUIT:
                gameExit = True



        clock.tick(FPS)

        if gameExit:
            gameOver = True
        else:
            gameOver = isGameOver(boxes)

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, grey2, [30,250,280,280])



        for row in boxes:
            for j in row:

                gameDisplay.blit(pygame.image.load(j.img),(j.x,j.y))


        pygame.display.update()
    pygame.quit()

    quit()

main()
