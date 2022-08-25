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
    
    # def issoldiercrossavai(self,troopslist):



    def checkcollision(self,targetnum,troopslist):
        x = troopslist[targetnum]["x"]
        y = troopslist[targetnum]["y"]
        for index,data in enumerate(troopslist):
            if not index==targetnum:
                if data["x"]==x and data["y"]==y and not data["type"]==troopslist[targetnum]["type"]:
                    print("death happen please be quit for a minute or you can say even a second it's your choice hahahh.!!!")


    def satifycondition(self,x,y):
        issatisfy = False
        if x>10 and x<600-40 and y >10 and y<600-40:
            issatisfy = True

        return issatisfy

    def givetargetareas(self,co_arr):
        targetareas = []
        for index,data in enumerate(co_arr):
            print(data[2])
            obj = self.getobj(data[0],data[1],data[2])
            targetareas.append(obj)
        # print(targetareas)
        return targetareas

    # give the direction for only soldiers
    def junction(self,index=0,boxco=[],alltrops=[],isstraightpossible=True,isstraighthitpossible=True,forward=0,backward=0,leftward=0,rightward=0,iscrosspossible=False,crossdirection=[],type="white",name="soldier",direction=None):
        color = "red"
        global forover
        targetareas = []
        co_arr = []
        co_arr.append([alltrops[index]["x"],alltrops[index]["y"],color])
        color="green"
        direction = [forward,backward,leftward,rightward]
        
        # forward backward leftward rightward
        isdirection = [True,True,True,True]

        for num,dir in enumerate(direction):
            print(dir)
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
                                            co_arr.append([x,y,color])
                                            color = "green" if color=="red" else "red"
                                            isdirection[num]=False
                                        else:
                                            isdirection[num]=False
                            if not innerexecuted:
                                co_arr.append([x,y,color])
                                color = "green" if color=="red" else "red"
        

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
                                        if isstraighthitpossible:
                                            co_arr.append([x,y,color])
                                            color = "green" if color=="red" else "red"
                                            iscrossdirection[num2]=False
                                        else:
                                            iscrossdirection[num2]=False
                            if not innerexecuted:
                                co_arr.append([x,y,color])
                                color = "green" if color=="red" else "red"
        

                                

        targetareas = self.givetargetareas(co_arr)
        return targetareas