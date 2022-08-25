squaresize = 70

def getobj(x,y,color):
    obj = {
        "x":x,
        "y":y,
        "color":color
    }
    # print(obj)
    return obj


color = "purple"
squaresize = 70

def satifycondition(x,y):
    issatisfy = False
    if x>10 and x<600-10 and y >10 and y<600-40:
        issatisfy = True

    return issatisfy

def givetargetareas(co_arr):
    targetareas = []
    for index,data in enumerate(co_arr):
        obj = getobj(data[0],data[1],data[2])
        targetareas.append(obj)
    # print(targetareas)
    return targetareas

# give the direction for only soldiers
def junction(index=0,boxco=[],alltrops=[],isstraightpossible=True,isstraighthitpossible=True,forward=0,backward=0,leftward=0,righward=0,iscrosspossible=False,crossnum=0,type="white",name="soldier",direction=None):
    global forover
    targetareas = []
    co_arr = []
    co_arr.append([alltrops[index]["x"],alltrops[index]["y"],"red"])


    isleftward = True
    isforward = True
    isbackward = True
    isrightward = True
    if isstraightpossible:
        
        for i in range(forward):
            if isforward:
                x = alltrops[index]["x"]
                y = alltrops[index]["y"]-i*squaresize if direction=="up" else alltrops[index]["y"]+i*squaresize
                isoky = satifycondition(x,y)
                innerexecuted = False
                if not i==0:
                    if isoky:
                        for index1,data1 in enumerate(alltrops):
                            if data1["x"]==x and data1["y"]==y:
                                innerexecuted = True
                                if data1["type"]==type:
                                    print("both the types same ")
                                    isforward=False
                                else:
                                    print("hey there")
                                    if isstraighthitpossible:
                                        co_arr.append([x,y,"red"])
                                        isforward = False
                                    else:
                                        isforward = False
                        if not innerexecuted:
                            co_arr.append([x,y,"red"])
        # for i in range(backward):
        #     if isbackward:
        #         x = alltrops[index]["x"]
        #         y = alltrops[index]["y"]+i*squaresize if direction=="up" else alltrops[index]["y"]-i*squaresize
        #         isoky = satifycondition(x,y)
        #         innerexecuted = False
        #         if not i==0:
        #             if isoky:
        #                 for index1,data1 in enumerate(alltrops):
        #                     if data1["x"]==x and data1["y"]==y:
        #                         innerexecuted = True
        #                         if data1["type"]==type:
        #                             isbackward=False
        #                         else:
        #                             if isstraighthitpossible:
        #                                 co_arr.append([x,y,"red"])
        #                                 isbackward = False
        #                             else:
        #                                 isbackward = False
        #                 if not innerexecuted:
        #                     co_arr.append([x,y,"red"])


                        

            

    targetareas = givetargetareas(co_arr)
    return targetareas