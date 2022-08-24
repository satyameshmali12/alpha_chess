squaresize = 70

def gettargetareasofsoldier(question,answer,direction,data,alltroops):
    newli = []
    if question==answer:
            color = "orange"
            for i in range(3):
                obj = {
                    "x":data["x"],
                    "y":data["y"]-i*squaresize,
                    "color":color
                }
                newli.append(obj)
                color = "orange" if not color=="orange" else "pink"
            
    return newli

def searchcollision():
    pass

def getobj(x,y,color):
    obj = {
        "x":x,
        "y":y,
        "color":color
    }
    return obj