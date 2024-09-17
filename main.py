from PIL import Image
from PIL import ImageDraw
import math
import random
teddy=Image.open("Teddy.jpg")
au=Image.open("austin.jpg")
def distance_halo(image,targetX, targetY, modifier) :
    pixels=image.load()
    for x in range(image.width):
        for y in range(image.height):
            X=0
            Y=0
            if x>=targetX:
                X=x-targetX
            else:
                X=targetX-x
            if y>=targetY:
                Y=y-targetY
            else:
                Y=targetY-y
            distance=math.sqrt((X**2)+(Y**2))
            num=distance//modifier
            r,g,b=pixels[x,y]
            r=int(r-num)
            g=int(g-num)
            b=int(b-num)
            pixels[x,y]=(r,g,b)
    image.save("halo.jpg")
def pointillism(image):
    canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")
    pixels=image.load()
    for i in range(1000000):
        x=random.randrange(image.width)
        y=random.randrange(image.height)
        r,g,b=pixels[x,y]
        size = random.randint(3,5)
        ellipsebox=[(x,y),(x+size,y+size)]
        draw = ImageDraw.Draw(canvas)
        draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
        del draw
    canvas.save("pointillism.jpg")
# distance_halo(teddy,285,356,2)
pointillism(teddy)