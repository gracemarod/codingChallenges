
image = [[0,0,0,1,1,1,1,1,1,3,3,8,7,4,7,6,7,1],
         [0,0,0,0,1,1,1,1,0,5,5,5,5,5,5,0,0,0],
         [1,1,1,1,0,5,5,5,5,5,5,5,5,5,5,4,7,6],
         [1,1,1,1,0,5,5,5,5,5,5,5,5,5,5,4,7,5]]

oldColor = "5"
def floodfill(image, x, y, oldColor, newColor):

    #print image[x][y]
    if image[x][y] != oldColor:
        
        return None
    else:
        print image
        image[x][y] = newColor
        
        floodfill(image, x+1, y,oldColor,newColor) 
        floodfill(image, x-1, y,oldColor,newColor)
        floodfill(image, x, y+1,oldColor,newColor)
        floodfill(image, x, y-1,oldColor,newColor)
        
floodfill(image,3,2,1,7)     