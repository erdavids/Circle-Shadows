def setup():
    size(1280, 720)
    background(255, 255, 255)
    pixelDensity(2)

    
    for c in range(1000):
        center_x = random(100, 1180)
        center_y = random(100, 620)
        cs = 40
        
        # Draw Shadow
        noStroke()
        fill(15, 15, 15, 5)
        for i in range(30):
            circle(center_x, center_y, cs - i*5)
        
        # Draw Circle
        stroke(30, 30, 30)
        fill(random(50, 255), random(50, 255), random(200, 255))
        circle(center_x - 25, center_y - 25, cs)
        
    
    save("Examples/Shadow.png")
