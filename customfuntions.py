squaresize = 70

def getobj(x,y,color):
    obj = {
        "x":x,
        "y":y,
        "color":color
    }
    print(obj)
    return obj


color = "purple"
squaresize = 70

def satifycondition(x,y):
    issatisfy = False
    if x>10 and x<600-10 and y >10 and y<600-10:
        issatisfy = True

    return issatisfy


forover = False
# give the direction for only soldiers
def junction(index=0,boxco=[],alltrops=[],isstraightpossible=True,isstraighthitpossible=True,forward=0,backward=0,leftward=0,righward=0,iscrosspossible=False,crossnum=0,type="white",name="soldier",direction=None):
    global forover
    targetareas = []
    co_arr = []
    co_arr.append([alltrops[index]["x"],alltrops[index]["y"],"red"])
    if isstraightpossible:
        for i in range(forward):
            if i==0:
                forover=False
            if forover:
                break
            # 0 1 +1 +1
            x = alltrops[index]["x"]
            y = alltrops[index]["y"]
            innerexcuted = False
            # co_arr.append([x,y-i*squaresize,"red"])
            for index2,data2 in enumerate(alltrops):
                if x==data2["x"] and y-i*squaresize==data2["y"]:
                    
                    innerexcuted = True
                    print(data2["type"])
                    if data2["type"]=="white":
                        # forover = True
                        break
                    elif data2["type"]=="black":
                        forover = True
                        isoky = satifycondition(data2["x"],data2["y"]-i*squaresize)
                        if isoky:
                            co_arr.append([data2["x"],data2["y"]-i*squaresize,"red"])
                            break
            if not innerexcuted:
                isoky = satifycondition(x,y-i*squaresize)
                if isoky:
                    print("inner executed")
                    co_arr.append([x,y-i*squaresize,"red"])
        
        print(co_arr)
            



            # if y-(count*squaresize)
            # obj = getobj(alltrops[index]["x"],alltrops[index]["y"],"red")
    
    for index,data in enumerate(co_arr):
        # print(type(data[0]),type(data[1]),type(data[2]))
        obj = getobj(data[0],data[1],data[2])
        targetareas.append(obj)

    # print(targetareas)
    return targetareas