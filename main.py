import pygame

# custom imports
from functions import displayimage, displaytext, drawrect, loadimage, scaleimage
from initialtroopco import initialtroopco_ordinates
from customfuntions import chess

pygame.init()  # initializing the window

# declaring all the constant variables
width = 750
height = 600
display = pygame.display.set_mode((width, height))
squaresize = 70
nooftroops = 16




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


homeimg = scaleimage(loadimage("assets/charac.png"),450,350)
icon = loadimage("assets/icon.webp")
playbutton = scaleimage(loadimage("assets/play.png"),120,120)
homebutton = scaleimage(loadimage("assets/homebutton.png"),120,120)
gameoverimg = loadimage("assets/gameover.png")

pygame.display.set_caption("Chess :- A Game For Champions")
pygame.display.set_icon(icon)


# declaring the colors
black = (71, 71, 71)
white = (255, 255, 255)
di = (159, 225, 245)

# creating or settling the co_ordinates for the chess box or chess design
# stored in the varible named boxco
x = 20
y = 20
boxco = []
color = "white"
for i in range(8):
    x = 20
    if not i == 0:
        y += squaresize
        color = white if color == black else black
    for j in range(8):
        obj = {
            "x": x,
            "y": y,
            "color": color,
        }
        x += squaresize
        boxco.append(obj)
        color = white if color == black else black




def gameloop(timing=60):

    global boxco

    # setting the troops line
    # bringing all the troops together in one array                             :-  above two array i.e. blacktroops and whitetroops are used in further scenario
    blackline = [blackelephant, blackhorse, blackcamel, blackqueen,
             blackking, blackcamel, blackhorse, blackelephant]
    x = 20
    y = 20
    blacktroops = initialtroopco_ordinates(
        blackline, x, y, squaresize, True, blacksoldier, "black")

    whiteline = [whiteelephant, whitehorse, whitecamel, whitequeen,
                whiteking, whitecamel, whitehorse, whiteelephant]
    x = 20
    y = 20+squaresize*7
    whitetroops = initialtroopco_ordinates(
        whiteline, x, y, squaresize, False, whitesoldier, "white")

    alltrops = []
    for index, data in enumerate([blacktroops, whitetroops]):
        for i in range(len(data)):
            alltrops.append(data[i])


            
    # first turn will be of the white player :- as in the usual scanerio
    turn = "whiteplayer"


    targetareas = []
    targettroop = None


    # initializing the chess class and creating a attribute
    customs = chess()

    blackkilled = []
    whitekilled = []

    regensoliders = [[whitecamel,whiteelephant,whitehorse,whitequeen],[blackcamel,blackelephant,blackhorse,blackqueen]]
    regensoildersco = customs.getregensoldierlist()


    player1time,player2time = timing,timing
    isnewtroopsselectionwindowopen = False

    which_troop_reached_end = None
    
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:
        try:


            # checking for the game over
            loseplayer1 = True
            loseplayer2 = True
            if len(blackkilled)==nooftroops or len(whitekilled)==nooftroops:
                gameover("Player2" if len(whitekilled)==nooftroops else "Player1")
            
            if player1time<1 or player2time<1:
                gameover("Player2" if player1time<1 else "Player1")

            for index,data in enumerate(alltrops):
                if data["name"]==whiteking:
                    loseplayer1=False
                elif data["name"]==blackking:
                    loseplayer2=False
                
            if loseplayer1 or loseplayer2:
                gameover("Player1" if loseplayer2 else "Player2")


            
            
            for e in pygame.event.get():
                heldkeys = pygame.key.get_pressed()
                # press ctrl+q to leave the running chess match
                if heldkeys[pygame.K_LCTRL] and heldkeys[pygame.K_q] or heldkeys[pygame.K_RCTRL] and heldkeys[pygame.K_q] :
                    homescreen()

                if e.type == pygame.USEREVENT:
                    if not isnewtroopsselectionwindowopen:
                        if turn == "whiteplayer":
                            player1time -= 1
                        else:
                            player2time -= 1
                if e.type == pygame.QUIT:
                    quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    moux, mouy = pygame.mouse.get_pos()
                    if isnewtroopsselectionwindowopen:
                        for reindex,redata in enumerate(regensoildersco):

                            if moux>redata[0] and moux<redata[0]+squaresize and mouy>redata[1] and mouy<redata[1]+squaresize:
                                for reindex2,redata2 in enumerate(alltrops):
                                    if redata2["x"]==which_troop_reached_end["x"] and redata2["y"]==which_troop_reached_end["y"]:
                                        num = 1 if turn=="whiteplayer" else 0
                                        alltrops[reindex2].update({
                                            "name":regensoliders[num][reindex]
                                        })
                                        isnewtroopsselectionwindowopen = False




                    running = False
                    for index, data in enumerate(targetareas):
                        if abs(data["x"]+squaresize/2-moux) < squaresize/2 and abs(data["y"]+squaresize/2-mouy) < squaresize/2:

                            if not data["x"] == alltrops[targettroop]["x"] or not data["y"] == alltrops[targettroop]["y"]:
                            
                                alltrops[targettroop].update({
                                    "x": data["x"],
                                    "y": data["y"]
                                })

                                if alltrops[targettroop]["y"]==20 or alltrops[targettroop]["y"]==510:

                                    if alltrops[targettroop]["name"]==whitesoldier or alltrops[targettroop]["name"]==blacksoldier:
                                        isnewtroopsselectionwindowopen = True
                                        which_troop_reached_end = {"x":alltrops[targettroop]["x"],"y":alltrops[targettroop]["y"]}


                                if alltrops[targettroop]["firstmove"]:
                                    alltrops[targettroop].update(
                                        {"firstmove": False})
                                        
                                turn = "whiteplayer" if turn == "blackplayer" else "blackplayer"
                                running = True
                                removalinex = customs.checkcollision(
                                    targettroop, alltrops)
                                if not removalinex == None:
                                    alltrops[removalinex]["type"] == "black" and blackkilled.append(
                                        alltrops[removalinex])
                                    alltrops[removalinex]["type"] == "white" and whitekilled.append(
                                        alltrops[removalinex])

                                not removalinex == None and alltrops.remove(
                                    alltrops[removalinex])
                                break
                    targetareas.clear()
                    if not running:
                        for index, data in enumerate(alltrops):
                            if abs(data["x"]+squaresize/2-moux) < squaresize/2 and abs(data["y"]+squaresize/2-mouy) < squaresize/2:
                                # setting the target troop
                                targettroop = index

                                # boxco is nothing but the all the boxes present on the screen and there color is changed on every click and the movement is alse done with the help of the boxco variable only 🆘
                                for index2, data2 in enumerate(boxco):

                                    if abs(data2["x"]+squaresize/2-moux) < squaresize/2 and abs(data2["y"]+squaresize/2-mouy) < squaresize/2:

                                        # this will only be executed only when the newtroopselection window is closed
                                        if not isnewtroopsselectionwindowopen:

                                            # to get the target areas of the troop when they are pressed
                                            if turn == "whiteplayer":

                                                if data["name"] == whitesoldier:
                                                    cross1, cross2 = customs.issoldiercrossavai(
                                                        alltrops, "black", data["x"], data["y"], 2, 2, "up")
                                                    targetareas = customs.junction(index, boxco, alltrops, True, False, 3 if data["firstmove"] else 2, 0, 0, 0, True, [
                                                                                cross1, cross2, 0, 0], "white", "soldier", "up")

                                                elif data["name"] == whiteelephant:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 8, 8, 8, 8, True, [
                                                                                0, 0, 0, 0], "white", "elephant", "up")
                                                elif data["name"] == whitequeen:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 8, 8, 8, 8, True, [
                                                                                8, 8, 8, 8], "white", "elephant", "up")
                                                elif data["name"] == whiteking:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 2, 2, 2, 2, True, [
                                                                                2, 2, 2, 2], "white", "elephant", "up")
                                                elif data["name"] == whitecamel:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 0, 0, 0, 0, True, [
                                                                                8, 8, 8, 8], "white", "elephant", "up")

                                                elif data["name"] == whitehorse:
                                                    targetareas = customs.horsetargetarea(
                                                        alltrops, index, "black")

                                            if turn == "blackplayer":
                                                if data["name"] == blacksoldier:
                                                    cross1, cross2 = customs.issoldiercrossavai(
                                                        alltrops, "white", data["x"], data["y"], 2, 2, "down")
                                                    targetareas = customs.junction(index, boxco, alltrops, True, False, 0, 3 if data["firstmove"] else 2, 0, 0, True, [
                                                                                0, 0, cross1, cross2], "black", "soldier", "down")

                                                elif data["name"] == blackelephant:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 8, 8, 8, 8, True, [
                                                                                0, 0, 0, 0], "black", "elephant", "up")
                                                elif data["name"] == blackqueen:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 8, 8, 8, 8, True, [
                                                                                8, 8, 8, 8], "black", "elephant", "up")
                                                elif data["name"] == blackking:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 2, 2, 2, 2, True, [
                                                                                2, 2, 2, 2], "black", "elephant", "up")
                                                elif data["name"] == blackcamel:
                                                    targetareas = customs.junction(index, boxco, alltrops, True, True, 0, 0, 0, 0, True, [
                                                                                8, 8, 8, 8], "black", "elephant", "up")
                                                elif data["name"] == blackhorse:
                                                    targetareas = customs.horsetargetarea(
                                                        alltrops, index, "white")
                            
                        

            display.fill((196, 147, 143))

            # drawing the chess board
            drawrect(display, "black", 17, 17, width-34, height-34, 3)
            for index, data in enumerate(boxco):
                drawrect(display, data["color"], data["x"],
                        data["y"], squaresize, squaresize)

                        
            # displaying the target areas                               :- displayed over the chess board and below the troops
            for index, data in enumerate(targetareas):
                drawrect(display, data["color"], data["x"],
                        data["y"], squaresize, squaresize)

            # displaying all the troops
            for index, data in enumerate(alltrops):
                displayimage(display, data["name"], data["x"], data["y"])

            # some other stuffs
            displaytext(display, "Player 1", width-150,
                        height-50, 30, black, True, True)
            displaytext(display, "Player 2", width-150, 30, 30, black, True, True)

            # displaying the player timing and the killed troops
            a = width-170
            b = height-240
            for index, data in enumerate(blackkilled):
                if (index+1) % 4 == 0:
                    a = width-170
                    b += 35
                img = scaleimage(data["name"], 40, 40)
                displayimage(display, img, a, b)
                a += 35

            a = width-170
            b = 50
            for index, data in enumerate(whitekilled):
                if (index+1) % 4 == 0:
                    a = width-170
                    b += 35
                img = scaleimage(data["name"], 40, 40)
                displayimage(display, img, a, b)
                a += 35

            displaytext(display, f"{player1time}", width -
                        114, height-295, 40, "black", True, True)
            displaytext(display, f"{player2time}", width -
                        114, 250, 40, "black", True, True)


            if isnewtroopsselectionwindowopen:
                size = 60
                num = 1 if turn=="whiteplayer" else 0
                li = regensoliders[num]
                drawrect(display,"purple",100,100,400,400,0)
                for index,data in enumerate(regensoildersco):
                    img = scaleimage(li[index],size,size)
                    displayimage(display,img,data[0],data[1])




            pygame.display.update()
        except Exception as e:
            print("Hey some error occurred....!")


def homescreen():
    time = 5
    while True:
        try:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    moux,mouy = pygame.mouse.get_pos()
                    if moux>400 and moux<440 and mouy>170 and mouy<210:
                        if time<60:
                            time+=1
                    elif moux>280 and moux<320 and mouy>170 and mouy<210:
                        if time>1:
                            time-=1
                    elif moux>width/2-75 and moux<width/2-75+playbutton.get_width() and mouy>260 and mouy<260+playbutton.get_height():
                        gameloop(time*60)

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        gameloop(time*60)

            
            display.fill(di)

            displaytext(display,"Alpha Chess",width/2-150,10,60,"black",False,True)
            displayimage(display,homeimg,width/2-homeimg.get_width()/2+150,height/2-100)
            drawrect(display,"red",420,100,100,60,0)
            displaytext(display,"Timing:-",250,120,50,"black",True,True)
            displaytext(display,f"{time}m",440,120,50,"black",True,True)
            displaytext(display,"+",400,170,80,"black",True,False)
            displaytext(display,"-",280,170,100,"black",True,False)
            
            displayimage(display,playbutton,width/2-75,260)

            pygame.display.update()
        except Exception as e:
            print("Hey some error occurred....!")





def gameover(name):
    while True:
        try:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()

                if e.type == pygame.MOUSEBUTTONUP:
                    moux,mouy = pygame.mouse.get_pos()
                    if moux>width/2-homebutton.get_width()/2 and moux<width/2-homebutton.get_width()/2+homebutton.get_width() and mouy>150 and mouy<150+homebutton.get_height():
                        homescreen()
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        homescreen()

            display.fill(di)
            displaytext(display,f"Congrats {name} Win",width/2-200,70,60,"black",False,False)
            displayimage(display,gameoverimg,100,200)
            displayimage(display,homebutton,width/2-homebutton.get_width()/2,150)
            pygame.display.update()
        except Exception as e:
            print("Hey some error occurred....!")




# Note press 👇
# Press ctrl+q to leave the running chess match






# all done
# Running the game
# Enjoy It,🎃
homescreen()

# If you find any kind of error please let us know we will definitely improve it.

# Copyright ©️ by AJTAs 

# Thanks