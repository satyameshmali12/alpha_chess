def initialtroopco_ordinates(troopsline,inix,iniy,squaresize,isincrement,troopimg):
    troops = []
    x = inix
    y = iniy
    for index,data in enumerate(troopsline):
        obj = {
            "x":x,
            "y":y,
            "name":data
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
            "name":troopimg
        }
        troops.append(obj)

        x+=squaresize
    
    return troops


# print(initialtroopco_ordinates())
