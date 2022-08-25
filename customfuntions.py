class chess:
    def __init__(self):
        color = "purple"
        self.squaresize = 70

    def getobj(self,x,y,color):
        obj = {
            "x":x,
            "y":y,
            "color":color
        }
        return obj

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
        # print(targetareas)
        return targetareas

    # give the direction for only soldiers
    def junction(self,index=0,boxco=[],alltrops=[],isstraightpossible=True,isstraighthitpossible=True,forward=0,backward=0,leftward=0,rightward=0,iscrosspossible=False,crossnum=0,type="white",name="soldier",direction=None):
        global forover
        targetareas = []
        co_arr = []
        co_arr.append([alltrops[index]["x"],alltrops[index]["y"],"red"])
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
                                            co_arr.append([x,y,"red"])
                                            isdirection[num]=False
                                        else:
                                            isdirection[num]=False
                            if not innerexecuted:
                                co_arr.append([x,y,"red"])

        targetareas = self.givetargetareas(co_arr)
        return targetareas