import cv2
import numpy as np
import random
import os

# Image size
img_size = (400, 400)

os.makedirs("output/Pisces", exist_ok=True)

for i in range(2000):
    # Random locations with a range of +/- 5 pixels
    locations = [(295, 20), (240, 35), (235, 70), (150, 110), (90, 135), (20, 160), (40, 170), (75, 170), (100, 180), (160, 205), (185, 230), (280, 365), (240, 260), (270, 300), (305, 335), (310, 390), (340, 385), (335, 350)]
    locations = [(x + random.randint(-5, 5), y + random.randint(-5, 5)) for x, y in locations]
    # Create an image with black background
    img = np.zeros((img_size[1], img_size[0], 3), np.uint8)
    img[:] = (0, 0, 0)
    # Draw circles with diameter 10 at the random locations
    for x, y in locations:
        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
    # Rotate the image randomly in the range of 360 degrees
    rows, cols = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), random.uniform(0, 360), 1)
    img = cv2.warpAffine(img, rotation_matrix, (cols, rows))
    # Resize the image to 244x244
    img = cv2.resize(img, (224, 224))
    # Save the image
    cv2.imwrite(f"output/Pisces/{i}.jpg", img)