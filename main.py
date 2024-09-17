from PIL import Image
texas=Image.open("Texas.png")
def distance_halo(image,targetX, targetY, modifier):
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
            last_guess= ((X**2)+(Y**2))/2.0
            i=False
            distance=0
            while i!=True:
                guess=(last_guess + x/last_guess)/2
                if abs(guess - last_guess) < .000001:
                    distance=guess
                    i=True
                last_guess=guess
            num=distance/modifier
            r,g,b,t=pixels[x,y]
            r=r-num
            g=g-num
            b=b-num
            pixels[x,y]=r,g,b,t
    image.save("halo.png")
distance_halo(texas,512,342,2)