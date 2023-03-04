from PIL import Image, ImageFilter
import cv2
import numpy as np
import random
import os
import csv_data_maker
import shutil
import csv
import format

# Constants
classes = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']
img_size = (400, 400)

# Crete the folders
shutil.rmtree("img/output/train")
for cls in classes:
    os.makedirs(f"img/output/train/{cls}", exist_ok=True)

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

def make_train_data(num_of_images):
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
            rotate_angle = random.uniform(0, 360)
            brightness_adjust = random.uniform(-0.1, 0.1)
            img = create_constellation_image(locations, rotate_angle, brightness_adjust)
            cv2.imwrite(f"img/output/train/{cls}/{i}.jpg", img)
def train(min):
    constellation_keys = []
    def add_to_csv(data):
        filename = "constellation_data.csv"
        # Append the data to the .csv file
        with open(filename, mode="a") as file:
            writer = csv.writer(file)
            for row in data:
                name = row[0]
                coords = row[1]
                writer.writerow([name]+coords)

    def add_row(constellation, locations):
        new_locations = []
        for nums in locations:
            f_x = nums[0]
            f_y = nums[1]
            if f_x <= 0 or f_y <= 0:
                new_locations.append((0, 0))
            else:
                new_locations.append((f_x, f_y))
        x_coords = [x for x, y in new_locations]
        y_coords = [y for x, y in new_locations]
        star_coords = [x for xy in zip(x_coords, y_coords) for x in xy]
        data = [constellation, star_coords]
        constellation_keys.append(data)

    def process_raw(img_path, min_area):
        image = Image.open(img_path)
        image = image.filter(ImageFilter.BoxBlur(3))
        img = cv2.imread(img_path, 0)
        # Find contours in the binary image
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # x value lists
        x_lst = []
        y_lst = []
        # Loop through all contours
        for contour in contours:
            # Calculate the area of the contour
            area = cv2.contourArea(contour)
            if area > min_area:
                # Calculate the center of the contour
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    x_lst.append(cX)
                    y_lst.append(cY)
        return x_lst, y_lst

    for root, dirs, files in os.walk('img/output/train'):
        for filename in files:
            if filename.endswith('.jpg'):
                path = os.path.join(root, filename)
                folder_name = os.path.basename(os.path.abspath(root))
                x_lst, y_lst = process_raw(path, min)
                add_row(folder_name, zip(x_lst, y_lst))
    add_to_csv(constellation_keys)
def make_train(num_of_images, min):
    make_train_data(num_of_images)
    train(min)
    format.format_csv()
if __name__ == "__main__":
    make_train(50, 20)