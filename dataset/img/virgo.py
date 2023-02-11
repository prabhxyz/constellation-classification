import cv2
import numpy as np
import random
import os

# Image size
img_size = (400, 400)

os.makedirs("output/Virgo", exist_ok=True)

for i in range(2500):
    # Random locations with a range of +/- 5 pixels
    locations = [(365, 70), (325, 150), (285, 180), (245, 155), (210, 105), (240, 285), (190, 215), (130, 220), (50, 250), (150, 320), (130, 290), (80, 305)]
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
    cv2.imwrite(f"output/Virgo/{i}.jpg", img)