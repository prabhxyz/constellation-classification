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
        f_x = move_5(nums[0])
        f_y = move_5(nums[1])
        if f_x <= 0 or f_y <= 0:
            new_locations.append((0, 0))
        else:
            new_locations.append((f_x, f_y))
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
        locations = [(131, 286), (49, 258), (240, 235), (158, 238), (102, 224), (363, 200), (151, 199), (218, 193), (107, 182), (294, 181), (300, 179), (231, 139), (191, 142)]
        add_row("Aquarius", rotate_coords(locations))
    for i in range(rng):
        locations = [(321, 237), (302, 211), (239, 185), (63, 159)]
        add_row("Aries", rotate_coords(locations))
    for i in range(rng):
        locations = [(198, 341), (95, 235), (190, 191), (219, 150), (267, 65)]
        add_row("Cancer", rotate_coords(locations))
    for i in range(rng):
        locations = [(254, 271), (159, 243), (263, 239), (119, 199), (93, 198), (160, 190), (199, 184), (279, 159), (295, 120)]
        add_row("Capricorn", rotate_coords(locations))
    for i in range(rng):
        locations = [(257, 329), (167, 295), (271, 283), (191, 247), (152, 235), (289, 233), (83, 215), (298, 206), (319, 199), (343, 187), (242, 187), (107, 183), (135, 167), (85, 169), (163, 142), (123, 124), (103, 127), (103, 131), (199, 91)]
        add_row("Gemini", rotate_coords(locations))
    for i in range(rng):
        locations = [(84, 279), (151, 255), (275, 227), (134, 215), (267, 182), (227, 174), (224, 144), (292, 118), (253, 101)]
        add_row("Leo", rotate_coords(locations))
    for i in range(rng):
        locations = [(144, 319), (265, 286), (147, 279), (116, 166), (287, 159), (287, 155), (198, 87)]
        add_row("Libra", rotate_coords(locations))
    for i in range(rng):
        locations = [(335, 263), (311, 264), (79, 255), (347, 248), (311, 240), (115, 238), (331, 230), (278, 230), (203, 227), (135, 231), (135, 227), (175, 222), (178, 219), (107, 211), (135, 175), (165, 118), (155, 96), (167, 80)]
        add_row("Pisces", rotate_coords(locations))
    for i in range(rng):
        locations = [(167, 327), (107, 311), (163, 291), (287, 263), (91, 248), (271, 238), (315, 208), (283, 192), (195, 191), (190, 171), (235, 166), (87, 163), (271, 155), (219, 157), (215, 123), (307, 115), (195, 118), (183, 108), (155, 77)]
        add_row("Sagittarius", rotate_coords(locations))
    for i in range(rng):
        locations = [(155, 296), (110, 294), (182, 283), (87, 267), (185, 245), (114, 242), (111, 243), (189, 209), (211, 171), (291, 147), (231, 143), (291, 114), (278, 87)]
        add_row("Scorpio", rotate_coords(locations))
    for i in range(rng):
        locations = [(280, 294), (231, 272), (184, 213), (283, 200), (209, 214), (195, 163), (99, 119), (149, 83)]
        add_row("Taurus", rotate_coords(locations))
    for i in range(rng):
        locations = [(208, 352), (155, 351), (215, 311), (171, 278), (195, 238), (271, 232), (233, 201), (176, 170), (126, 170), (216, 153), (215, 120), (159, 79), (211, 67), (179, 51)]
        add_row("Virgo", rotate_coords(locations))

gen(1000)
format()
