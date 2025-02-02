import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import sys
import os

GENERATE_IMAGE = True   #If true will generate image, if false will only show the plot
OK = 2  #number of OK image cap
NOK = 4   #number of NOK image cap
COLOR = ["#FF0000","#0000FF","#00FF00"] #Choice of colors
OK_PATH = 'OK' #Your folder path for the OK image
NOK_PATH = 'NOK'   #Your folder path for the NOK image

P_COLOR = np.int8(np.ceil(NOK/4))  #sub number of NOK image (color problem)
P_COLOR_PATH = NOK_PATH + '/P_COLOR'
P_MATTER = np.int8(np.ceil(NOK/4))  #sub number of NOK image (matter problem)
P_MATTER_PATH = NOK_PATH + '/P_MATTER'
P_SIZE = np.int8(np.ceil(NOK/4)) #sub number of NOK image (size problem)
P_SIZE_PATH = NOK_PATH + '/P_SIZE'
P_CURVE = np.int8(np.ceil(NOK/4))   #sub number of NOK image (curve problem)
P_CURVE_PATH = NOK_PATH + '/P_CURVE'

# Representation of a cap will be done inside of a 17x17 square,
# Acceptable one will ONLY be 11x11 with 2 pixel for curvature
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]
#[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0]
#[0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0]
#[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0]
#[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def createOkCap(width, height):
    """
    Create a single array of a Ok cap

    Parameters:
        width (int) : The width in pixel of the image
        height (int) : The height in pixel of the image

    Returns:
        array[int] : the array
    """
    array = np.zeros((height,width))
    for i in range(width) :
        for j in range(height) :
            if i == 3 or i == 13 :
                if j >= 6 and j <= 10 : 
                    array[i][j] = 1
            if i == 4 or i == 12 :
                if j >= 5 and j <= 11 :
                    array[i][j] = 1
            if i == 5 or i == 11 :
                if j >= 4 and j <= 12 :
                    array[i][j] = 1
            if i >= 6 and i < 11 :
                if j >= 3 and j <= 13 :
                    array[i][j] = 1
    return array

'''
Input : 
    width = The width of the image
    height = the height of the image
Output : 
    array = a Nok array generated with a problem of colors
'''
def createNokCapColor(width, height) : 
    """
    Create a single array of a P_COLOR cap.

    Parameters:
        width (int) : The width in pixel of the image
        height (int) : The height in pixel of the image

    Returns:
        array[int] : the array
    """
    chance = 0.025
    nbr = 0

    array = createOkCap(width, height)
    for i in range(width) :
        for j in range(height) :
            if array[i][j] == 1 :
                if np.random.rand() < chance :
                    if nbr < 5 :
                        array[i][j] = 2
                        nbr = nbr + 1
                    else :
                        return array

    #Make sure to have at least one other color
    if nbr == 0 :
        array = createNokCapColor(width, height)
    return array

def createNokCapMatter(width, height) :
    """
    Create a single array of a P_MATTER cap.

    Parameters:
        width (int) : The width in pixel of the image
        height (int) : The height in pixel of the image

    Returns:
        array[int] : the array
    """
    chance = 0.001
    nbr = 0

    array = createOkCap(width, height)
    for i in range(width) :
        for j in range(height) :
            if array[i][j] == 1 :
                if np.random.rand() < chance :
                    array[i][j] = 0
                    nbr = nbr + 1
    
    #Make sure to have at least one empty pixel
    if nbr == 0 :
        array = createNokCapMatter(width, height)
    return array

def createNokCapSize(width, height) :
    """
    Create a single array of a P_SIZE cap.

    Parameters:
        width (int) : The width in pixel of the image
        height (int) : The height in pixel of the image

    Returns:
        array[int] : the array
    """
    chance = 0.5
    array = np.zeros((height,width))
    if np.random.rand() < chance :
        #Make bigger
        for i in range(width) :
            for j in range(height) :
                if i == 2 or i == 14:
                    if j >= 5 and j <= 11 : 
                        array[i][j] = 1
                if i == 3 or i == 13 :
                    if j >= 4 and j <= 12 :
                        array[i][j] = 1
                if i == 4 or i == 12:
                    if j >= 3 and j <= 13 :
                        array[i][j] = 1
                if i >= 5 and i < 12 :
                    if j >= 2 and j <= 14 :
                        array[i][j] = 1
        return array
    
    #Make smaller
    for i in range(width) :
        for j in range(height) :
            if i == 4 or i == 12 :
                if j >= 7 and j <= 9 : 
                    array[i][j] = 1
            if i == 5 or i == 11 :
                if j >= 6 and j <= 10 :
                    array[i][j] = 1
            if i == 6 or i == 10 :
                if j >= 5 and j <= 11 :
                    array[i][j] = 1
            if i >= 7 and i < 10 :
                if j >= 4 and j <= 12 :
                    array[i][j] = 1
    return array

def createNokCapCurve(width, height) : 
    """
    Create a single array of a P_CURVE cap.

    Parameters:
        width (int) : The width in pixel of the image
        height (int) : The height in pixel of the image

    Returns:
        array[int] : the array
    """
    rand = np.random.rand()
    array = np.zeros((height,width))

    #Default 1
    if rand < 0.25 :
        for i in range(width) :
            for j in range(height) :
                if i == 3 or i == 13 :
                    if j >= 7 and j <= 10 : 
                        array[i][j] = 1
                if i == 4 or i == 12 :
                    if j >= 5 and j <= 11 :
                        array[i][j] = 1
                if i == 5 or i == 11 :
                    if j >= 4 and j <= 12 :
                        array[i][j] = 1
                if i >= 6 and i < 11 :
                    if j >= 3 and j <= 13 :
                        array[i][j] = 1

    #Default 2
    elif rand > 0.25 and rand < 0.50 :
        for i in range(width) :
            for j in range(height) :
                if i == 3 or i == 13 :
                    if j >= 6 and j <= 10 : 
                        array[i][j] = 1
                if i == 4 or i == 12 :
                    if j >= 4 and j <= 11 :
                        array[i][j] = 1
                if i == 5 or i == 11 :
                    if j >= 4 and j <= 12 :
                        array[i][j] = 1
                if i >= 6 and i < 11 :
                    if j >= 3 and j <= 13 :
                        array[i][j] = 1

    #Default 3
    elif rand > 0.50 and rand < 0.75 :
        for i in range(width) :
            for j in range(height) :
                if i == 3 or i == 13 :
                    if j >= 6 and j <= 10 : 
                        array[i][j] = 1
                if i == 4 or i == 12 :
                    if j >= 5 and j <= 11 :
                        array[i][j] = 1
                if i == 5 or i == 11 :
                    if j >= 4 and j <= 13 :
                        array[i][j] = 1
                if i >= 6 and i < 11 :
                    if j >= 3 and j <= 13 :
                        array[i][j] = 1

    #Default 4
    elif rand > 0.75 :
        for i in range(width) :
            for j in range(height) :
                if i == 3 or i == 13 :
                    if j >= 6 and j <= 10 : 
                        array[i][j] = 1
                if i == 4 or i == 12 :
                    if j >= 5 and j <= 11 :
                        array[i][j] = 1
                if i == 5 or i == 11 :
                    if j >= 4 and j <= 12 :
                        array[i][j] = 1
                if i >= 6 and i < 11 :
                    if j >= 2 and j <= 13 :
                        array[i][j] = 1
    return array

def randomColorPick() :
    """
    Select a random position in the COLOR global array

    Parameters:
        None

    Returns:
        The color(hex value) in the COLOR global array
    """
    rand = np.int8(np.floor(np.random.rand() * len(COLOR)))
    return COLOR[rand]

def createImage(array, ok, num, type) :
    """
    Select a random position in the COLOR global array

    Parameters:
        array (array) : The array of 0 and 1 to create the image from
        ok (boolean) : If the array is a Ok cap.
        num (int) : The number of the generated image
        type (string) : The type of N_OK cap, None if its a Ok cap

    Returns:
        None
    """
    rndColor = randomColorPick()
    rndColor2 = randomColorPick()
    while(rndColor == rndColor2) :
        rndColor2 = randomColorPick()
    
    colors = ['white', rndColor, rndColor2]
    cmap = mcolors.ListedColormap(colors)

    plt.figure(figsize=(1.7,1.7), dpi=10)
    plt.gca().set_position([0, 0, 1, 1])
    plt.axis('off')
    plt.imshow(array, cmap=cmap, interpolation='nearest')
    #Indicate how to name and where to save the image
    if ok == True :
        if GENERATE_IMAGE == True :
            plt.savefig(f'{OK_PATH}/Ok_image_{num}.png',bbox_inches='tight',pad_inches=0)
        elif GENERATE_IMAGE == False : 
            plt.show()
    else : 
        if GENERATE_IMAGE == True :
            if type == "P_COLOR" :
                #plt.show()
                plt.savefig(f'{P_COLOR_PATH}/NOk_image_{num}.png',bbox_inches='tight',pad_inches=0)
            if type == "P_CURVE" :
                #plt.show()
                plt.savefig(f'{P_CURVE_PATH}/NOk_image_{num}.png',bbox_inches='tight',pad_inches=0)
            if type == "P_MATTER" :
                #plt.show()
                plt.savefig(f'{P_MATTER_PATH}/NOk_image_{num}.png',bbox_inches='tight',pad_inches=0)
            if type == "P_SIZE" :
                #plt.show()
                
                plt.savefig(f'{P_SIZE_PATH}/NOk_image_{num}.png',bbox_inches='tight',pad_inches=0)
        elif GENERATE_IMAGE == False :
            plt.show()

def recalculateSubNumber() :
    """
    Recalculate the sub number of image for each NOK problems.
    """
    global P_CURVE, P_COLOR, P_MATTER, P_SIZE, NOK
    P_COLOR = np.int8(np.ceil(NOK/4))
    P_MATTER = np.int8(np.ceil(NOK/4))
    P_SIZE = np.int8(np.ceil(NOK/4))
    P_CURVE = np.int8(np.ceil(NOK/4))

def main(generateImage=None, ok=None, nok=None, color=None) :
    global GENERATE_IMAGE, OK, NOK, COLOR

    if generateImage is not None :
        GENERATE_IMAGE = generateImage
    if ok is not None :
        OK = ok
    if nok is not None :
        NOK = nok
        recalculateSubNumber()

    if color is not None :
        COLOR = color

    if not os.path.exists(OK_PATH) :
        os.makedirs(OK_PATH)

    if not os.path.exists(P_COLOR_PATH) :
        os.makedirs(P_COLOR_PATH)

    if not os.path.exists(P_CURVE_PATH) :
        os.makedirs(P_CURVE_PATH)

    if not os.path.exists(P_MATTER_PATH) :
        os.makedirs(P_MATTER_PATH)

    if not os.path.exists(P_SIZE_PATH) :
        os.makedirs(P_SIZE_PATH)
    
    #Create the ok images
    for i in range(OK):
        okArray = createOkCap(17, 17)
        createImage(okArray, True, i , type=None)

    #Create the nok images
    for p in range(P_COLOR) :
        nokArray = createNokCapColor(17,17)
        createImage(nokArray, False, p, type="P_COLOR")

    for p in range(P_CURVE) :
        nokArray = createNokCapCurve(17,17)
        createImage(nokArray, False, p, type="P_CURVE")

    for p in range(P_MATTER) :
        nokArray = createNokCapMatter(17,17)
        createImage(nokArray, False, p, type="P_MATTER")

    for p in range(P_SIZE) :
        nokArray = createNokCapSize(17,17)
        createImage(nokArray, False, p, type="P_SIZE")

if __name__ ==  "__main__" :
    sys.exit(main())