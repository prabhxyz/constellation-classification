import csv
import math
import random
import os
from format import format

# Remove First to Create BrandNew File
if os.path.exists("constellation_data.csv"):
    os.remove("constellation_data.csv")

def move_5(num):
    direction = random.randint(0, 1)
    if direction == 0:
        return num + random.randint(0, 5)
    else:
        return num - random.randint(0, 5)
def add_to_csv(constellation, *star_coords):
    filename = "constellation_data.csv"
    # Check if the file exists
    if not os.path.exists(filename):
        # If it doesn't, create the file and write the header
        with open(filename, mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(['constellation_name', 's1_x', 's1_y', 's2_x', 's2_y', 's3_x', 's3_y', 's4_x', 's4_y', 's5_x', 's5_y', 's6_x', 's6_y', 's7_x', 's7_y', 's8_x', 's8_y', 's9_x', 's9_y', 's10_x', 's10_y', 's11_x', 's11_y', 's12_x', 's12_y', 's13_x', 's13_y', 's14_x', 's14_y', 's15_x', 's15_y', 's16_x', 's16_y', 's17_x', 's17_y', 's18_x', 's18_y', 's19_x', 's19_y', 's20_x', 's20_y', 's21_x', 's21_y'])

    # Open the .csv file in append mode
    with open(filename, mode="a") as file:
        writer = csv.writer(file)
        # Write the constellation name and all the star coordinates as a single row in the .csv file
        writer.writerow([constellation] + list(star_coords))

def add_row(constellation, locations):
    new_locations = []
    for nums in locations:
        new_locations.append((move_5(nums[0]), move_5(nums[1])))
    x_coords = [x for x, y in new_locations]
    y_coords = [y for x, y in new_locations]
    star_coords = [x for xy in zip(x_coords, y_coords) for x in xy]
    add_to_csv(constellation, *star_coords)
def rotate_coords(locations, origin=(random.randrange(150, 250), random.randrange(150, 250)), zoom=random.uniform(0.1, 2)):
    angle = random.randint(1, 360)
    angle = math.radians(angle)
    ox, oy = origin
    rotated_coords = []
    for x, y in locations:
        x_ = ox + zoom * (math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy))
        y_ = oy + zoom * (math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy))
        rotated_coords.append((round(x_), round(y_)))
    return rotated_coords
def gen(rng):
    for i in range(rng):
        locations = [(85, 285), (100, 250), (110, 220), (100, 170), (125, 130), (145, 130), (160, 150), (200, 135), (180, 190), (195, 255), (270, 180), (360, 230)]
        add_row("Aquarius", rotate_coords(locations))
    for i in range(rng):
        locations = [(90, 50), (220, 225), (240, 300), (225, 330)]
        add_row("Aries", rotate_coords(locations))
    for i in range(rng):
        locations = [(180, 35), (275, 70), (175, 155), (165, 210), (95, 300), (260, 370)]
        add_row("Cancer", rotate_coords(locations))
    for i in range(rng):
        locations = [(40, 160), (60, 170), (125, 170), (110, 250), (180, 180), (220, 320), (240, 300), (340, 150), (350, 120)]
        add_row("Capricorn", rotate_coords(locations))
    for i in range(rng):
        locations = [(120, 140), (75, 80), (125, 75), (160, 90), (190, 25), (220, 320), (225, 105), (310, 105), (105, 170), (45, 240), (95, 370), (130, 230), (155, 350), (235, 230), (220, 325), (265, 315), (285, 335)]
        add_row("Gemini", rotate_coords(locations))
    for i in range(rng):
        locations = [(40, 330), (100, 220), (130, 280), (320, 220), (290, 170), (225, 110), (240, 155), (265, 50), (300, 65)]
        add_row("Leo", rotate_coords(locations))
    for i in range(rng):
        locations = [(50, 320), (80, 225), (60, 75), (250, 70), (350, 225)]
        add_row("Libra", rotate_coords(locations))
    for i in range(rng):
        locations = [(295, 20), (240, 35), (235, 70), (150, 110), (90, 135), (20, 160), (40, 170), (75, 170), (100, 180), (160, 205), (185, 230), (280, 365), (240, 260), (270, 300), (305, 335), (310, 390), (340, 385), (335, 350)]
        add_row("Pisces", rotate_coords(locations))
    for i in range(rng):
        locations = [(310, 350), (270, 320), (240, 390), (165, 350), (85, 300), (100, 225), (180, 180), (205, 190), (315, 160), (350, 170), (60, 135), (80, 135), (125, 130), (135, 110), (190, 150), (210, 135), (285, 110), (320, 90), (335, 35), (230, 85), (225, 20)]
        add_row("Sagittarius", rotate_coords(locations))
    for i in range(rng):
        locations = [(80, 115), (50, 110), (30, 105), (15, 150), (40, 200), (70, 230), (120, 210), (170, 200), (255, 200), (280, 210), (360, 270), (390, 245), (320, 290)]
        add_row("Scorpio", rotate_coords(locations))
    for i in range(rng):
        locations = [(10, 230), (135, 215), (190, 225), (190, 260), (30, 315), (230, 240), (230, 110), (300, 230), (390, 190)]
        add_row("Taurus", rotate_coords(locations))
    for i in range(rng):
        locations = [(365, 70), (325, 150), (285, 180), (245, 155), (210, 105), (240, 285), (190, 215), (130, 220), (50, 250), (150, 320), (130, 290), (80, 305)]
        add_row("Virgo", rotate_coords(locations))

gen(50000)
format()
