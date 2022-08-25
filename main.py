import pygame
import sys # to exit the game
# custom imports
from functions import displayimage, drawrect,loadimage
from initialtroopco import initialtroopco_ordinates
# from customfuntions import getobj,junction
from customfuntions import chess

pygame.init() # initializing the window

# declaring all the constant variables
width = 600
height = 600
display = pygame.display.set_mode((width,height))
squaresize = 70


# loading all the images
blackcamel = loadimage("assets/bB.png")
blackking = loadimage("assets/bK.png")
blackhorse = loadimage("assets/bN.png")
blacksoldier = loadimage("assets/bp.png")
blackqueen = loadimage("assets/bQ.png")
blackelephant = loadimage("assets/bR.png")

whitecamel = loadimage("assets/wB.png")
whiteking = loadimage("assets/wK.png")
whitehorse = loadimage("assets/wN.png")
whitesoldier = loadimage("assets/wp.png")
whitequeen = loadimage("assets/wQ.png")
whiteelephant = loadimage("assets/wR.png")


# declaring the colors
black = (71,71,71)
white = (255,255,255)

# creating or settling the co_ordinates for the chess box or chess design
# stored in the varible named boxco
x = 20
y = 20
boxco = []
color = "white"
for i in range(8):
    x = 20
    if not i==0:
        y +=squaresize
        color = white if color==black else black
    for j in range(8):
        obj = {
            "x":x,
            "y":y,
            "color":color,
        }
        x+=squaresize
        boxco.append(obj)
        color = white if color==black else black

# setting the troops line
blackline = [blackelephant,blackhorse,blackcamel,blackqueen,blackking,blackcamel,blackhorse,blackelephant]
x = 20
y = 20
blacktroops = initialtroopco_ordinates(blackline,x,y,squaresize,True,blacksoldier,"black")

whiteline = [whiteelephant,whitehorse,whitecamel,whitequeen,whiteking,whitecamel,whitehorse,whiteelephant]
x = 20
y = 20+squaresize*7
whitetroops = initialtroopco_ordinates(whiteline,x,y,squaresize,False,whitesoldier,"white")


# bringing all the troops together in one array                             :-  above two array i.e. blacktroops and whitetroops are used in further scenario 
alltrops = []
for index,data in enumerate([blacktroops,whitetroops]):
    for i in range(len(data)):
        alltrops.append(data[i])

# iniboxco = boxco
# first turn will be of the white player :- as in the usual scanerio
turn = "whiteplayer"

# alltrops.remove(alltrops[31])


def gameloop():

    global boxco
    global alltrops
    global turn

    targetareas = []
    targettroop = None
    customs = chess()

    while True:
        # try:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    moux,mouy = pygame.mouse.get_pos()
                    running = False
                    for index,data in enumerate(targetareas):
                        if abs(data["x"]+squaresize/2-moux)<squaresize/2 and abs(data["y"]+squaresize/2-mouy)<squaresize/2:
                            alltrops[targettroop].update({
                                "x":data["x"],
                                "y":data["y"]
                            })
                            running = True
                            break
                    targetareas.clear()
                    if not running:
                        for index,data in enumerate(alltrops):
                            if abs(data["x"]+squaresize/2-moux)<squaresize/2 and abs(data["y"]+squaresize/2-mouy)<squaresize/2:
                                # setting the target troop
                                targettroop = index
                                # print(index)

                                # boxco is nothing but the all the boxes present on the screen and there color is changed on every click and the movement is alse done with the help of the boxco variable only 🆘
                                for index2,data2 in enumerate(boxco):

                                    if abs(data2["x"]+squaresize/2-moux)<squaresize/2 and abs(data2["y"]+squaresize/2-mouy)<squaresize/2:

                                        # if white troops player turn then it will be executed
                                        if turn == "whiteplayer": 

                                            if data["name"]==whitesoldier:
                                                color = "orange"
                                                targetareas = customs.junction(index,boxco,alltrops,True,False,3,0,0,0,True,1,"white","soldier","up")
                                            if data["name"]==blacksoldier:
                                                targetareas = customs.junction(index,boxco,alltrops,True,False,0,3,0,0,True,1,"black","soldier","down")
                                            if data["name"]==whiteelephant:
                                                targetareas = customs.junction(index,boxco,alltrops,True,True,8,8,8,8,True,1,"white","elephant","up")
                                            if data["name"]==whitequeen:
                                                targetareas = customs.junction(index,boxco,alltrops,True,True,8,8,8,8,True,1,"white","elephant","up")
                                            if data["name"]==whiteking:
                                                targetareas = customs.junction(index,boxco,alltrops,True,True,2,2,2,2,True,1,"white","elephant","up")

                                                


            display.fill("white")

            # drawing the chess board
            drawrect(display,"black",17,17,width-34,height-34,3)
            for index,data in enumerate(boxco):
                drawrect(display,data["color"],data["x"],data["y"],squaresize,squaresize)
            # displaying the target areas                               :- displayed over the chess board and below the troops
            for index,data in enumerate(targetareas):
                drawrect(display,data["color"],data["x"],data["y"],squaresize,squaresize)


            # displaying all the troops
            for index,data in enumerate(alltrops):
                displayimage(display,data["name"],data["x"],data["y"])


            drawrect(display,"red",10,600-50,10,10,0)
            pygame.display.update()
        # except Exception as e:
        #     print(e)

gameloop()

