def distance_halo(image,targetX, targetY, modifier) :
    pixels=image.load()
    for x in range(image.width):
        for y in range(image.height):
            last_guess= ((targetX**2)+(targetY**2))/2.0
            while True:
                guess=(last_guess + x/last_guess)/2
                if abs(guess - last_guess) < .000001: # example threshold
                    return guess
                last_guess=guess
