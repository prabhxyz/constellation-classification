import glob
import os
import cv2
from PIL import Image, ImageFilter
import pyperclip as pc

# Folder
main_folder = "img/output/test"

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

data = ""
# loop through each subfolder
for subfolder in os.listdir(main_folder):
    if os.path.isdir(os.path.join(main_folder, subfolder)):
        subfolder_path = os.path.join(main_folder, subfolder)
        for jpg_file in glob.glob(os.path.join(subfolder_path, "*.jpg")):
            x_lst, y_lst = process_raw(jpg_file, 10)
            lst = list(zip(x_lst, y_lst))
            final_lst = [str(x) for tup in lst for x in tup]
            final_lst = result = ",".join(final_lst)
            print(subfolder+","+final_lst)
            data += subfolder+","+final_lst+"\n"
pc.copy(data)
print("Copied!")