import pygame
import sys # to exit the game
# custom imports
from functions import displayimage, drawrect,loadimage
from initialtroopco import initialtroopco_ordinates

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
blacktroops = initialtroopco_ordinates(blackline,x,y,squaresize,True,blacksoldier)

whiteline = [whiteelephant,whitehorse,whitecamel,whitequeen,whiteking,whitecamel,whitehorse,whiteelephant]
x = 20
y = 20+squaresize*7
whitetroops = initialtroopco_ordinates(whiteline,x,y,squaresize,False,whitesoldier)


# bringing all the troops together in one array                             :-  above two array i.e. blacktroops and whitetroops are used in further scenario 
alltrops = []
for index,data in enumerate([blacktroops,whitetroops]):
    for i in range(len(data)):
        alltrops.append(data[i])



def gameloop():

    global boxco
    global alltrops
    iniboxco = boxco

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                moux,mouy = pygame.mouse.get_pos()
                for index,data in enumerate(alltrops):
                    if abs(data["x"]+squaresize/2-moux)<squaresize/2 and abs(data["y"]+squaresize/2-mouy)<squaresize/2:
                        print(index)
                        for index2,data2 in enumerate(boxco):
                            if abs(data2["x"]+squaresize/2-moux)<squaresize/2 and abs(data2["y"]+squaresize/2-mouy)<squaresize/2:
                                boxco[index2].update({
                                    "color":"red"
                                })


        display.fill("white")

        # drawing the chess board
        drawrect(display,"black",17,17,width-34,height-34,3)
        for index,data in enumerate(boxco):
            drawrect(display,data["color"],data["x"],data["y"],squaresize,squaresize)

        # displaying all the troops
        for index,data in enumerate(alltrops):
            displayimage(display,data["name"],data["x"],data["y"])

        pygame.display.update()

gameloop()