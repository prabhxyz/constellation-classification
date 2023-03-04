import cv2
import numpy as np
import random
import os
import csv_data_maker

# Constants
classes = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']
img_size = (400, 400)

# Crete the folders
for cls in classes:
    os.makedirs(f"dataset/img/output/test/{cls}", exist_ok=True)

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

def make_test_data(num_of_images):
    # Create the data for each class
    for cls in classes:
        for i in range(num_of_images):
            # Get the locations for the current class
            if cls == 'Aquarius':
                locations = csv_data_maker.testing_data('Aquarius')
            if cls == 'Aries':
                locations = csv_data_maker.testing_data('Aries')
            if cls == 'Cancer':
                locations = csv_data_maker.testing_data('Cancer')
            if cls == 'Capricorn':
                locations = csv_data_maker.testing_data('Capricorn')
            if cls == 'Gemini':
                locations = csv_data_maker.testing_data('Gemini')
            if cls == 'Leo':
                locations = csv_data_maker.testing_data('Leo')
            if cls == 'Libra':
                locations = csv_data_maker.testing_data('Libra')
            if cls == 'Pisces':
                locations = csv_data_maker.testing_data('Pisces')
            if cls == 'Sagittarius':
                locations = csv_data_maker.testing_data('Sagittarius')
            if cls == 'Scorpio':
                locations = csv_data_maker.testing_data('Scorpio')
            if cls == 'Taurus':
                locations = csv_data_maker.testing_data('Taurus')
            if cls == 'Virgo':
                locations = csv_data_maker.testing_data('Virgo')
            # Add code for other classes here
            # Apply data augmentation techniques
            rotate_angle = random.uniform(0, 360)
            brightness_adjust = random.uniform(-0.1, 0.1)
            img = create_constellation_image(locations, rotate_angle, brightness_adjust)
            cv2.imwrite(f"dataset/img/output/test/{cls}/{i}.jpg", img)