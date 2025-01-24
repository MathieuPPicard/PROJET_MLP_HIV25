import CapGenerator as Generator
import numpy as np
import sys
import random
from PIL import Image

OK_PATH = Generator.OK_PATH
NOK_PATH = Generator.NOK_PATH
P_COLOR_PATH = Generator.P_COLOR_PATH
P_MATTER_PATH = Generator.P_MATTER_PATH
P_SIZE_PATH = Generator.P_SIZE_PATH
P_CURVE_PATH = Generator.P_CURVE_PATH

def transformRgbArray(array) :
    colorDict = {}
    x = []
    i = 0
    for line in array :
        transformLine = []
        for pixel in line :
            rgb = tuple(pixel)
            if rgb not in colorDict :
                colorDict[rgb] = i
                i += 1
            transformLine.append(colorDict[rgb])
        x.append(transformLine)
    return x

def imageToArray2(image_path, type) :
    img = Image.open(image_path)
    img = img.convert("RGB")
    rgb_x = np.array(img)
    x = transformRgbArray(rgb_x)
    if type == "OK" :
        y = 1
    elif type == "NOK" :
        y = 0
    return x,y

def imageToArray5(image_path, type) :
    img = Image.open(image_path)
    img = img.convert("RGB")
    rgb_x = np.array(img)
    x = transformRgbArray(rgb_x)
    if type == "OK" :
        y = "OK"
    elif type == "P_COLOR" :
        y = "P_COLOR"
    elif type == "P_MATTER" :
        y = "P_COLOR"
    elif type == "P_SIZE" :
        y = "P_SIZE"
    elif type == "P_CURVE" :
        y = "P_CURVE"
    return x,y


def analyse2() :
    array_x = []
    array_y = []    
    #Create the OK array
    for i in range(Generator.OK) :
        x,y = imageToArray2(f'{OK_PATH}/Ok_image_{i}.png', "OK")
        array_x.append(x)
        array_y.append(y)

    for y in range(Generator.P_COLOR) :
        x,y = imageToArray2(f'{P_COLOR_PATH}/NOk_image_{y}.png', "NOK")
        array_x.append(x)
        array_y.append(y)

    for z in range(Generator.P_MATTER) :
        x,y = imageToArray2(f'{P_MATTER_PATH}/NOk_image_{z}.png', "NOK")
        array_x.append(x)
        array_y.append(y)

    for w in range(Generator.P_SIZE) :
        x,y = imageToArray2(f'{P_SIZE_PATH}/NOk_image_{w}.png', "NOK")
        array_x.append(x)
        array_y.append(y)

    for q in range(Generator.P_CURVE) :
        x,y = imageToArray2(f'{P_CURVE_PATH}/NOk_image_{q}.png', "NOK")
        array_x.append(x)
        array_y.append(y)

    mix = list(range(len(array_x)))

    random.shuffle(mix)

    array_x = [array_x[i] for i in mix]
    array_y = [array_y[y] for y in mix]

    return array_x, array_y

def analyse5() :
    array_x = []
    array_y = []    
    #Create the OK array
    for i in range(Generator.OK) :
        x,y = imageToArray5(f'{OK_PATH}/Ok_image_{i}.png', "OK")
        array_x.append(x)
        array_y.append(y)

    for y in range(Generator.P_COLOR) :
        x,y = imageToArray5(f'{P_COLOR_PATH}/NOk_image_{y}.png', "P_COLOR")
        array_x.append(x)
        array_y.append(y)

    for z in range(Generator.P_MATTER) :
        x,y = imageToArray5(f'{P_MATTER_PATH}/NOk_image_{z}.png', "P_MATTER")
        array_x.append(x)
        array_y.append(y)

    for w in range(Generator.P_SIZE) :
        x,y = imageToArray5(f'{P_SIZE_PATH}/NOk_image_{w}.png', "P_SIZE")
        array_x.append(x)
        array_y.append(y)

    for q in range(Generator.P_CURVE) :
        x,y = imageToArray5(f'{P_CURVE_PATH}/NOk_image_{q}.png', "P_CURVE")
        array_x.append(x)
        array_y.append(y)

    mix = list(range(len(array_x)))

    random.shuffle(mix)

    array_x = [array_x[i] for i in mix]
    array_y = [array_y[y] for y in mix]

    return array_x, array_y

def main(classe) :
    if classe == 2 :
        return analyse2()
    elif classe == 5:
        return analyse5()

if __name__ ==  "__main__" :
    sys.exit(main())