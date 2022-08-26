class chess:
    def __init__(self):
        self.squaresize = 70

    def getobj(self,x,y,color):
        obj = {
            "x":x,
            "y":y,
            "color":color
        }
        return obj
    # this function is used only in the case of the soldier
    def issoldiercrossavai(self,troopslist,oppenenttype,x,y,wscross1,wscross2,direction):
        cross1 = 0
        cross2 = 0
        ysquaresize = self.squaresize if direction == "up" else -self.squaresize
        for index4,data4 in enumerate(troopslist):
            if data4["x"]==x-ysquaresize and data4["y"]==y-ysquaresize and data4["type"]==oppenenttype:
                print("executed")
                cross1 = wscross1
            if data4["x"]==x+ysquaresize and data4["y"]==y-ysquaresize and data4["type"]==oppenenttype:
                print("executed")
                cross2 = wscross2
        
        return cross1,cross2



    def checkcollision(self,targetnum,troopslist):
        x = troopslist[targetnum]["x"]
        y = troopslist[targetnum]["y"]
        removalindex = None
        for index,data in enumerate(troopslist):
            if not index==targetnum:
                if data["x"]==x and data["y"]==y and not data["type"]==troopslist[targetnum]["type"]:
                    print("death happen please be quit for a minute or you can say even a second it's your choice hahahh.!!!")
                    removalindex=index
        
        return removalindex


    def satifycondition(self,x,y):
        issatisfy = False
        if x>10 and x<600-40 and y >10 and y<600-40:
            issatisfy = True

        return issatisfy

    def givetargetareas(self,co_arr):
        targetareas = []
        for index,data in enumerate(co_arr):
            obj = self.getobj(data[0],data[1],data[2])
            targetareas.append(obj)
        return targetareas
    
    def horsetargetarea(self,troopslist,index,opponenttype):
        co_arr = []
        x = troopslist[index]["x"]
        y = troopslist[index]["y"]
        co_arr.append([x,y,"red"])
        num1 = 1
        num2 = 2
        for i in range(8):
            if i==4:
                num1 = 2
                num2 = 1
            if i>3:
                i-=4

            innerexecuted = False
            count = i
            if count>3:
                count-3
            x = troopslist[index]["x"]-num1*self.squaresize if i==0 or i==2 else  troopslist[index]["x"]+num1*self.squaresize
            y = troopslist[index]["y"]-num2*self.squaresize if i ==0 or i==1 else troopslist[index]["y"]+num2*self.squaresize

            for index1,data in enumerate(troopslist):
                if data["x"]==x and data["y"]==y:
                    innerexecuted = True
                    hastoadd = True if data["type"]==opponenttype else False
                    if hastoadd:
                        self.satifycondition(x,y) and co_arr.append([x,y,"red"])
            not innerexecuted and self.satifycondition(x,y) and co_arr.append([x,y,"red"])


            


        
        return self.givetargetareas(co_arr)


    # give the target area for all leftng the camel
    def junction(self,index=0,boxco=[],alltrops=[],isstraightpossible=True,isstraighthitpossible=True,forward=0,backward=0,leftward=0,rightward=0,iscrosspossible=False,crossdirection=[],type="white",name="soldier",direction=None):
        # color = "red"
        global forover
        targetareas = []
        co_arr = []
        co_arr.append([alltrops[index]["x"],alltrops[index]["y"],"red"])
        
        # many colors are taken to avoid the collision of the two colors together  while displaying on the screen
        colorli = ["green","yellow","orange","purple","blue","pink","gray","violet",(53, 219, 158),(1, 20, 89),(255, 55, 5),(230, 69, 98),(187, 230, 69),(133, 138, 120),(237, 255, 189),(17, 133, 38)]
        colornum = 0
        color="green"
        direction = [forward,backward,leftward,rightward]
        
        # forward backward leftward rightward
        isdirection = [True,True,True,True]

        for num,dir in enumerate(direction):
            for i in range(dir):
                if isdirection[num]:
                    x = alltrops[index]["x"] if num==0 or num==1 else alltrops[index]["x"]-i*self.squaresize if not num==3 else alltrops[index]["x"]+i*self.squaresize
                    y = alltrops[index]["y"] if num==2 or num==3 else alltrops[index]["y"]-i*self.squaresize if not num==1 else alltrops[index]["y"]+i*self.squaresize
                    isoky = self.satifycondition(x,y)
                    innerexecuted = False
                    if not i==0:
                        if isoky:
                            for index1,data1 in enumerate(alltrops):
                                if data1["x"]==x and data1["y"]==y:
                                    innerexecuted = True
                                    if data1["type"]==type:
                                        isdirection[num]=False
                                    else:
                                        if isstraighthitpossible:
                                            if colornum>len(colorli)-1:
                                                colornum=0
                                            co_arr.append([x,y,colorli[colornum]])
                                            colornum+=1
                                            isdirection[num]=False
                                        else:
                                            isdirection[num]=False
                            if not innerexecuted:
                                if colornum>len(colorli)-1:
                                    colornum=0
                                co_arr.append([x,y,colorli[colornum]])
                                colornum+=1
        

        iscrossdirection = [True,True,True,True]
        for num2,dir2 in enumerate(crossdirection):
            for i in range(dir2):
                if iscrossdirection[num2]:
                    x = alltrops[index]["x"]-i*self.squaresize if num2==0 or num2==3 else alltrops[index]["x"]+i*self.squaresize
                    y = alltrops[index]["y"]-i*self.squaresize if num2==0 or num2==1 else alltrops[index]["y"]+i*self.squaresize
                    isoky = self.satifycondition(x,y)
                    innerexecuted = False
                    if not i==0:
                        if isoky:
                            for index1,data1 in enumerate(alltrops):
                                if data1["x"]==x and data1["y"]==y:
                                    innerexecuted = True
                                    if data1["type"]==type:
                                        iscrossdirection[num2]=False
                                    else:
                                        if iscrosspossible:
                                            if colornum>len(colorli)-1:
                                                colornum=0
                                            co_arr.append([x,y,colorli[colornum]])
                                            colornum+=1
                                            iscrossdirection[num2]=False
                                        else:
                                            iscrossdirection[num2]=False
                            if not innerexecuted:
                                if colornum>len(colorli)-1:
                                    colornum=0
                                co_arr.append([x,y,colorli[colornum]])
                                colornum+=1
        

                                

        targetareas = self.givetargetareas(co_arr)
        return targetareas