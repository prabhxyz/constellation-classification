import math
import random
import secrets as sec

rng = random.SystemRandom()
gen_ran = False

def move_5(num):
    direction = sec.choice(range(0, 1))
    if direction == 0:
        return num + sec.choice(range(0, 5))
    else:
        return num - sec.choice(range(0, 5))

def rotate_coords(locations, zoom, origin=(sec.choice(range(150, 250)), sec.choice(range(150, 250)))):
    angle = sec.choice(range(1, 360))
    angle = math.radians(angle)
    ox, oy = origin
    rotated_coords = []
    for x, y in locations:
        x_ = ox + zoom * (math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy))
        y_ = oy + zoom * (math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy))
        if x_ < 0:
            x_ = 0
        if y_ < 0:
            y_ = 0
        rotated_coords.append((round(x_), round(y_)))
    return rotated_coords