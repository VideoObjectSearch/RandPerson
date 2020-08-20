# *********************
# 16 texture patterns
# *********************
import cv2
import os
import math
import random

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def pattern1(image,h):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,20):
        cv2.line(image, (i, 0), (i, 500), color, 2)
        cv2.line(image, (0, i), (500, i), color, 2)
    return image

def pattern2(image,h):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,20):
        cv2.line(image, (0, i), (500, i), color, 5)
    return image

def pattern3(image,h):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,100):
        cv2.line(image, (0, i), (50, i+100), color, 5)
        cv2.line(image, (50, i+100), (100, i), color, 5)
        cv2.line(image, (100, i), (150, i + 100), color, 5)
        cv2.line(image, (150, i + 100), (200, i), color, 5)
        cv2.line(image, (200, i), (250, i + 100), color, 5)
        cv2.line(image, (250, i + 100), (300, i), color, 5)
        cv2.line(image, (300, i), (350, i + 100), color, 5)
        cv2.line(image, (350, i + 100), (400, i), color, 5)
        cv2.line(image, (400, i), (450, i + 100), color, 5)
        cv2.line(image, (450, i + 100), (500, i), color, 5)
    return image

def pattern4(image,h):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,50):
        cv2.rectangle(image, (25,i+25), (50,i+50),color, 2)
        cv2.rectangle(image, (75, i + 25), (100, i + 50), color, 2)
        cv2.rectangle(image, (125, i + 25), (150, i + 50), color, 2)
        cv2.rectangle(image, (175, i + 25), (200, i + 50), color, 2)
        cv2.rectangle(image, (225, i + 25), (250, i + 50), color, 2)
        cv2.rectangle(image, (275, i + 25), (300, i + 50), color, 2)
        cv2.rectangle(image, (325, i + 25), (350, i + 50), color, 2)
        cv2.rectangle(image, (375, i + 25), (400, i + 50), color, 2)
        cv2.rectangle(image, (425, i + 25), (450, i + 50), color, 2)
        cv2.rectangle(image, (575, i + 25), (500, i + 50), color, 2)
    return image

def pattern5(image,h):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,50):
        cv2.line(image, (0, i), (500, i), color, 25)
    return image

def pattern6(image,h,h2):
    color1 = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    for i in range(0,500,40):
        cv2.line(image, (i, 0), (i, 500), color1, 8)
        cv2.line(image, (0, i), (500, i), color2, 8)
    return image

def pattern7(image,h,h2):
    color1 = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    for i in range(0,500,40):
        cv2.line(image, (0, i), (500, i), color1, 10)
        cv2.line(image, (0, i+20), (500, i+20), color2, 10)
    return image

def pattern8(image,h,h2):
    color1 = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    for i in range(0,600,200):
        cv2.line(image, (0, i), (50, i+100), color1, 5)
        cv2.line(image, (50, i+100), (100, i), color1, 5)
        cv2.line(image, (100, i), (150, i + 100), color1, 5)
        cv2.line(image, (150, i + 100), (200, i), color1, 5)
        cv2.line(image, (200, i), (250, i + 100), color1, 5)
        cv2.line(image, (250, i + 100), (300, i), color1, 5)
        cv2.line(image, (300, i), (350, i + 100), color1, 5)
        cv2.line(image, (350, i + 100), (400, i), color1, 5)
        cv2.line(image, (400, i), (450, i + 100), color1, 5)
        cv2.line(image, (450, i + 100), (500, i), color1, 5)

        cv2.line(image, (0, i+100), (50, i + 200), color2, 5)
        cv2.line(image, (50, i + 200), (100, i+100), color2, 5)
        cv2.line(image, (100, i+100), (150, i + 200), color2, 5)
        cv2.line(image, (150, i + 200), (200, i+100), color2, 5)
        cv2.line(image, (200, i+100), (250, i + 200), color2, 5)
        cv2.line(image, (250, i + 200), (300, i+100), color2, 5)
        cv2.line(image, (300, i+100), (350, i + 200), color2, 5)
        cv2.line(image, (350, i + 200), (400, i+100), color2, 5)
        cv2.line(image, (400, i+100), (450, i + 200), color2, 5)
        cv2.line(image, (450, i + 200), (500, i+100), color2, 5)
    return image

def pattern9(image,h,h2):
    color = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    for i in range(0,500,100):
        cv2.rectangle(image, (25,i+25), (50,i+50),color, 10)
        cv2.rectangle(image, (75, i + 25), (100, i + 50), color, 10)
        cv2.rectangle(image, (125, i + 25), (150, i + 50), color, 10)
        cv2.rectangle(image, (175, i + 25), (200, i + 50), color, 10)
        cv2.rectangle(image, (225, i + 25), (250, i + 50), color, 10)
        cv2.rectangle(image, (275, i + 25), (300, i + 50), color, 10)
        cv2.rectangle(image, (325, i + 25), (350, i + 50), color, 10)
        cv2.rectangle(image, (375, i + 25), (400, i + 50), color, 10)
        cv2.rectangle(image, (425, i + 25), (450, i + 50), color, 10)
        cv2.rectangle(image, (575, i + 25), (500, i + 50), color, 10)

        cv2.rectangle(image, (25, i + 75), (50, i + 100), color2, 10)
        cv2.rectangle(image, (75, i + 75), (100, i + 100), color2, 10)
        cv2.rectangle(image, (125, i + 75), (150, i + 100), color2, 10)
        cv2.rectangle(image, (175, i + 75), (200, i + 100), color2, 10)
        cv2.rectangle(image, (225, i + 75), (250, i + 100), color2, 10)
        cv2.rectangle(image, (275, i + 75), (300, i + 100), color2, 10)
        cv2.rectangle(image, (325, i + 75), (350, i + 100), color2, 10)
        cv2.rectangle(image, (375, i + 75), (400, i + 100), color2, 10)
        cv2.rectangle(image, (425, i + 75), (450, i + 100), color2, 10)
        cv2.rectangle(image, (575, i + 75), (500, i + 100), color2, 10)
    return image

def pattern10(image,h,h2):
    color = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    for i in range(0,500,100):
        cv2.line(image, (0, i), (500, i), color, 25)
        cv2.line(image, (0, i+50), (500, i+50), color2, 25)
    return image

def pattern11(image,h,h2):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,40):
        cv2.line(image, (i, 0), (i, 500), color, 5)
    return image

def pattern12(image,h, h2):
    color1 = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    for i in range(0, 500, 60):
        cv2.line(image, (i, 0), (i, 500), color1, 10)
        cv2.line(image, (i + 20, 0), (i + 20, 500), color2, 10)
    return image

def pattern13(image,h,h2):
    color = hsv2rgb(h, 1, 1)
    for i in range(0,500,40):
        cv2.line(image, (0, i), (500-i, 500), color, 5)
        cv2.line(image, (i, 0), (500, 500-i), color, 5)
    return image

def pattern14(image,h,h2):
    color = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    time = 0
    for i in range(0,500,100):
        if time % 2 == 0:
            c1 = color
            c2 = color2
        else:
            c1 = color2
            c2 = color
        time += 1
        cv2.line(image, (0, i), (500 - i, 500), c1, 15)
        cv2.line(image, (i, 0), (500, 500 - i), c2, 15)
    return image

def pattern15(image,h,h2):
    color = hsv2rgb(h, 1, 1)
    color2 = hsv2rgb(h2, 1, 1)
    cv2.line(image, (0, 250), (500, 250), color, 150)
    cv2.line(image, (250, 0), (250, 500), color2, 150)
    return image

def pattern16(image,h,h2):
    return image

index = 0
for filename in os.listdir(r'c:\Users\yanan.wang\PycharmProjects\unityProgram\color'): #625 colors file path
    arr = filename.split('_')
    for pattern in range(1,17):
        image = cv2.imread(r'c:\\Users\\yanan.wang\\PycharmProjects\\unityProgram\\color\\' + filename)
        index += 1
        h = random.randint(0, 360)
        h2 = random.randint(0, 360)
        while abs(h - int(arr[0])) < 60:
            h = random.randint(0, 360)
        while abs(h2 - int(arr[0])) < 60 or abs(h2 - h) < 60:
            h2 = random.randint(0, 360)
        if pattern == 1:
            final_image = pattern1(image, h)
        if pattern == 2:
            final_image = pattern2(image, h)
        if pattern == 3:
            final_image = pattern3(image, h)
        if pattern == 4:
            final_image = pattern4(image, h)
        if pattern == 5:
            final_image = pattern5(image, h)
        if pattern == 6:
            final_image = pattern6(image, h, h2)
        if pattern == 7:
            final_image = pattern7(image, h, h2)
        if pattern == 8:
            final_image = pattern8(image, h, h2)
        if pattern == 9:
            final_image = pattern9(image, h, h2)
        if pattern == 10:
            final_image = pattern10(image, h, h2)
        if pattern == 11:
            final_image = pattern11(image, h, h2)
        if pattern == 12:
            final_image = pattern12(image, h, h2)
        if pattern == 13:
            final_image = pattern13(image, h, h2)
        if pattern == 14:
            final_image = pattern14(image, h, h2)
        if pattern == 15:
            final_image = pattern15(image, h, h2)
        if pattern == 16:
            final_image = pattern16(image, h, h2)
        cv2.imwrite('pattern//2020_07_12_' + str(index) + '.png', final_image)
    break




