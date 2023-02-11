import cv2
import numpy as np
import random
import os

# Constants
classes = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']
img_size = (400, 400)

# Create the output directories
for cls in classes:
    os.makedirs(f"output/train/{cls}", exist_ok=True)

# Function to create the constellation images
def create_constellation_image(locations, rotate_angle=0, brightness_adjust=0):
    # Random locations with a range of +/- 5 pixels
    locations = [(x + random.randint(-5, 5), y + random.randint(-5, 5)) for x, y in locations]
    # Create an image with black background
    img = np.zeros((img_size[1], img_size[0], 3), np.uint8)
    img[:] = (0, 0, 0)
    # Draw circles with diameter 6 at the random locations
    for x, y in locations:
        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
    # Rotate the image randomly in the range of 360 degrees
    rows, cols = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), rotate_angle, 1)
    img = cv2.warpAffine(img, rotation_matrix, (cols, rows))
    # Adjust the brightness of the image
    img = cv2.convertScaleAbs(img, alpha=(1 + brightness_adjust), beta=0)
    # Resize the image to 244x244
    img = cv2.resize(img, (224, 224))
    return img

# Create the data for each class
for cls in classes:
    if cls == "Sagittarius" or "Pisces" or "Gemini":
        num_of_images = 500
    elif cls == "Scorpio" or "Aquarius":
        num_of_images = 530
    else:
        num_of_images = 550
    for i in range(num_of_images):
        # Get the locations for the current class
        if cls == 'Aquarius':
            locations = [(85, 285), (100, 250), (110, 220), (100, 170), (125, 130), (145, 130), (160, 150), (200, 135), (180, 190), (195, 255), (270, 180), (360, 230)]
        if cls == 'Aries':
            locations = [(90, 50), (220, 225), (240, 300), (225, 330)]
        if cls == 'Cancer':
            locations = [(180, 35), (275, 70), (175, 155), (165, 210), (95, 300), (260, 370)]
        if cls == 'Capricorn':
            locations = [(40, 160), (60, 170), (125, 170), (110, 250), (180, 180), (220, 320), (240, 300), (340, 150), (350, 120)]
        if cls == 'Gemini':
            locations = [(120, 140), (75, 80), (125, 75), (160, 90), (190, 25), (220, 320), (225, 105), (310, 105), (105, 170), (45, 240), (95, 370), (130, 230), (155, 350), (235, 230), (220, 325), (265, 315), (285, 335)]
        if cls == 'Leo':
            locations = [(40, 330), (100, 220), (130, 280), (320, 220), (290, 170), (225, 110), (240, 155), (265, 50), (300, 65)]
        if cls == 'Libra':
            locations = [(50, 320), (80, 225), (60, 75), (250, 70), (350, 225)]
        if cls == 'Pisces':
            locations = [(295, 20), (240, 35), (235, 70), (150, 110), (90, 135), (20, 160), (40, 170), (75, 170), (100, 180), (160, 205), (185, 230), (280, 365), (240, 260), (270, 300), (305, 335), (310, 390), (340, 385), (335, 350)]
        if cls == 'Sagittarius':
            locations = [(310, 350), (270, 320), (240, 390), (165, 350), (85, 300), (100, 225), (180, 180), (205, 190), (315, 160), (350, 170), (60, 135), (80, 135), (125, 130), (135, 110), (190, 150), (210, 135), (285, 110), (320, 90), (335, 35), (230, 85), (225, 20)]
        if cls == 'Scorpio':
            locations = [(80, 115), (50, 110), (30, 105), (15, 150), (40, 200), (70, 230), (120, 210), (170, 200), (255, 200), (280, 210), (360, 270), (390, 245), (320, 290)]
        if cls == 'Taurus':
            locations = [(10, 230), (135, 215), (190, 225), (190, 260), (30, 315), (230, 240), (230, 110), (300, 230), (390, 190)]
        if cls == 'Virgo':
            locations = [(365, 70), (325, 150), (285, 180), (245, 155), (210, 105), (240, 285), (190, 215), (130, 220), (50, 250), (150, 320), (130, 290), (80, 305)]
        # Add code for other classes here
        # Apply data augmentation techniques
        rotate_angle = random.uniform(0, 360)
        brightness_adjust = random.uniform(-0.1, 0.1)
        img = create_constellation_image(locations, rotate_angle, brightness_adjust)
        cv2.imwrite(f"output/train/{cls}/{i}.jpg", img)