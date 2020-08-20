# *********************
# Generate 625 colors
# *********************
from PIL import Image
import math

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


for i in range(0,24):
    h, s, v = 0, 0, 0
    h = i*15
    for j in range(2,11,2):
        s = j*0.1
        for k in range(2,11,2):
            v = k*0.1
            color = hsv2rgb(h, s, v)
            img = Image.new("RGBA", (500, 500), color)
            img.save("color/" + str(int(h))+"_"+str(int(s*10))+"_"+str(int(v*10))+".png")
# black, white, gray
for i in range(0,25):
    color = hsv2rgb(0, 0, i/24)
    img = Image.new("RGBA", (500, 500), color)
    img.save("color/" + str(0) + "_" + str(0) + "_" + str(int(i * 10)) + ".png")