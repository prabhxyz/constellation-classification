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
        if x_ < 0:
            x_ = 0
        if y_ < 0:
            y_ = 0
        rotated_coords.append((round(x_), round(y_)))
    return rotated_coords
def gen(rng):
    for i in range(rng):
        locations = [(132, 273), (35, 251), (242, 226), (96, 212), (378, 188), (219, 178), (147, 182), (304, 165), (307, 170), (237, 123), (190, 120), (186, 119), (187, 115), (251, 107)]
        add_row("Aquarius", rotate_coords(locations))
    for i in range(rng):
        locations = [(355, 250), (338, 214), (254, 183), (41, 149)]
        add_row("Aries", rotate_coords(locations))
    for i in range(rng):
        locations = [(201, 355), (91, 243), (196, 195), (226, 156), (275, 67)]
        add_row("Cancer", rotate_coords(locations))
    for i in range(rng):
        locations = [(268, 292), (155, 259), (275, 255), (107, 210), (155, 202), (79, 207), (75, 209), (202, 195), (312, 115)]
        add_row("Capricorn", rotate_coords(locations))
    for i in range(rng):
        locations = [(170, 299), (282, 282), (199, 243), (200, 243), (298, 236), (155, 234), (87, 210), (87, 209), (330, 199), (356, 186), (251, 187), (139, 164), (87, 167), (91, 165), (171, 139), (123, 123), (107, 123), (211, 84)]
        add_row("Gemini", rotate_coords(locations))
    for i in range(rng):
        locations = [(99, 316), (218, 290), (338, 279), (87, 275), (270, 256), (267, 253), (27, 232), (110, 226), (274, 212), (243, 184), (115, 173), (354, 149), (322, 147), (364, 114), (299, 119)]
        add_row("Leo", rotate_coords(locations))
    for i in range(rng):
        locations = [(123, 343), (275, 301), (300, 154), (299, 154), (95, 158), (91, 161), (195, 65)]
        add_row("Libra", rotate_coords(locations))
    for i in range(rng):
        locations = [(322, 307), (55, 299), (54, 301), (363, 291), (323, 283), (98, 283), (346, 274), (347, 274), (288, 275), (117, 275), (118, 276), (196, 267), (90, 251), (119, 211), (122, 210), (154, 143), (144, 116), (155, 100)]
        add_row("Pisces", rotate_coords(locations))
    for i in range(rng):
        locations = [(170, 332), (106, 316), (163, 295), (294, 267), (275, 239), (275, 243), (323, 207), (290, 195), (196, 187), (194, 172), (243, 164), (277, 155), (220, 156), (219, 156), (219, 123), (196, 115), (195, 115)]
        add_row("Sagittarius", rotate_coords(locations))
    for i in range(rng):
        locations = [(160, 323), (102, 319), (99, 319), (193, 307), (83, 292), (191, 261), (107, 252), (199, 219), (222, 178), (322, 147), (251, 142), (319, 107), (307, 76)]
        add_row("Scorpio", rotate_coords(locations))
    for i in range(rng):
        locations = [(307, 329), (244, 299), (219, 258), (203, 243), (227, 229), (184, 219), (310, 216), (307, 217), (219, 211), (203, 166), (84, 114), (147, 68)]
        add_row("Taurus", rotate_coords(locations))
    for i in range(rng):
        locations = [(219, 376), (157, 375), (155, 377), (175, 290), (203, 250), (283, 246), (244, 211), (179, 173), (125, 177), (123, 177), (227, 119), (219, 59), (186, 43)]
        add_row("Virgo", rotate_coords(locations))

gen(50000)
format()
