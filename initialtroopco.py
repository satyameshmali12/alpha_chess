# to get the initial co_ordinates of all the troops

def initialtroopco_ordinates(troopsline,inix,iniy,squaresize,isincrement,troopimg,type):
    troops = []
    x = inix
    y = iniy
    for index,data in enumerate(troopsline):
        obj = {
            "x":x,
            "y":y,
            "name":data,
            "type":type,
            "firstmove":True
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
            "type":type,
            "firstmove":True
        }
        troops.append(obj)

        x+=squaresize
    
    return troops


