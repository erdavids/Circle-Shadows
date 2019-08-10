# Size Parameters
w, h = 1000, 1000

# Circle Size
cs = 40

def setup():
    size(w, h)
    
    background(30, 30, 30)
    
    # Take advantage of resolution
    pixelDensity(2)

    
    for c in range(2000):
        center_x = random(w/10, w - w/10)
        center_y = random(h/10, h - h/10)
        
        # Draw Shadow
        noStroke()
        fill(15, 15, 15, 5)
        for i in range(30):
            circle(center_x + 20, center_y + 20, cs - i*5)
        
        # Draw Circle
        stroke(30, 30, 30)
        fill(random(200, 255), random(50, 255), random(50, 255), random(150, 255))
        circle(center_x, center_y, cs)
        
    
    seed = int(random(10000))
    save("Examples/redbias-" + str(seed) + ".png")
