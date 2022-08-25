def initialtroopco_ordinates(troopsline,inix,iniy,squaresize,isincrement,troopimg,type):
    troops = []
    x = inix
    y = iniy
    for index,data in enumerate(troopsline):
        obj = {
            "x":x,
            "y":y,
            "name":data,
            "type":type
        }
        troops.append(obj)
        x+=squaresize

    # reintializing to the given values
    x = inix
    y = iniy+squaresize if isincrement else iniy-squaresize
    
    for i in range(8):

        obj = {
            "x":x,
            "y":y,
            "name":troopimg,
            "type":type
        }
        troops.append(obj)

        x+=squaresize
    
    return troops


# print(initialtroopco_ordinates())


# 🔺 later on remove this down function as it is kept just for the purpose of the reference
# def gettargetareasofsoldier(question,answer,direction,data,alltroops):
#     newli = []
#     if question==answer:
#             color = "orange"
#             for i in range(3):
#                 obj = {
#                     "x":data["x"],
#                     "y":data["y"]-i*squaresize,
#                     "color":color
#                 }
#                 newli.append(obj)
#                 color = "orange" if not color=="orange" else "pink"
            
#     return newli

# def searchcollision():
#     pass

