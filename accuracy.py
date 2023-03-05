import cv2
import math
import random
import shutil
import joblib
import numpy as np
import process
import os

# Constants
classes = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']
img_size = (400, 400)

# Crete the folders
shutil.rmtree("dataset/img/output/test")
for cls in classes:
    os.makedirs(f"dataset/img/output/test/{cls}", exist_ok=True)

dataset_made = False

# Function to create the constellation images
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
def testing_data(constellation_name):
    if constellation_name == "Aquarius":
        locations = [(131, 286), (49, 258), (240, 235), (158, 238), (102, 224), (363, 200), (151, 199), (218, 193), (107, 182), (294, 181), (300, 179), (231, 139), (191, 142)]
        return rotate_coords(locations)
    elif constellation_name == "Aries":
        locations = [(321, 237), (302, 211), (239, 185), (63, 159)]
        return rotate_coords(locations)
    elif constellation_name == "Cancer":
        locations = [(198, 341), (95, 235), (190, 191), (219, 150), (267, 65)]
        return rotate_coords(locations)
    elif constellation_name == "Capricorn":
        locations = [(254, 271), (159, 243), (263, 239), (119, 199), (93, 198), (160, 190), (199, 184), (279, 159), (295, 120)]
        return rotate_coords(locations)
    elif constellation_name == "Gemini":
        locations = [(257, 329), (167, 295), (271, 283), (191, 247), (152, 235), (289, 233), (83, 215), (298, 206), (319, 199), (343, 187), (242, 187), (107, 183), (135, 167), (85, 169), (163, 142), (123, 124), (103, 127), (103, 131), (199, 91)]
        return rotate_coords(locations)
    elif constellation_name == "Leo":
        locations = [(84, 279), (151, 255), (275, 227), (134, 215), (267, 182), (227, 174), (224, 144), (292, 118), (253, 101)]
        return rotate_coords(locations)
    elif constellation_name == "Libra":
        locations = [(144, 319), (265, 286), (147, 279), (116, 166), (287, 159), (287, 155), (198, 87)]
        return rotate_coords(locations)
    elif constellation_name == "Pisces":
        locations = [(335, 263), (311, 264), (79, 255), (347, 248), (311, 240), (115, 238), (331, 230), (278, 230), (203, 227), (135, 231), (135, 227), (175, 222), (178, 219), (107, 211), (135, 175), (165, 118), (155, 96), (167, 80)]
        return rotate_coords(locations)
    elif constellation_name == "Sagittarius":
        locations = [(167, 327), (107, 311), (163, 291), (287, 263), (91, 248), (271, 238), (315, 208), (283, 192), (195, 191), (190, 171), (235, 166), (87, 163), (271, 155), (219, 157), (215, 123), (307, 115), (195, 118), (183, 108), (155, 77)]
        return rotate_coords(locations)
    elif constellation_name == "Scorpio":
        locations = [(155, 296), (110, 294), (182, 283), (87, 267), (185, 245), (114, 242), (111, 243), (189, 209), (211, 171), (291, 147), (231, 143), (291, 114), (278, 87)]
        return rotate_coords(locations)
    elif constellation_name == "Taurus":
        locations = [(280, 294), (231, 272), (184, 213), (283, 200), (209, 214), (195, 163), (99, 119), (149, 83)]
        return rotate_coords(locations)
    elif constellation_name == "Virgo":
        locations = [(208, 352), (155, 351), (215, 311), (171, 278), (195, 238), (271, 232), (233, 201), (176, 170), (126, 170), (216, 153), (215, 120), (159, 79), (211, 67), (179, 51)]
        return rotate_coords(locations)

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
                locations = testing_data('Aquarius')
            if cls == 'Aries':
                locations = testing_data('Aries')
            if cls == 'Cancer':
                locations = testing_data('Cancer')
            if cls == 'Capricorn':
                locations = testing_data('Capricorn')
            if cls == 'Gemini':
                locations = testing_data('Gemini')
            if cls == 'Leo':
                locations = testing_data('Leo')
            if cls == 'Libra':
                locations = testing_data('Libra')
            if cls == 'Pisces':
                locations = testing_data('Pisces')
            if cls == 'Sagittarius':
                locations = testing_data('Sagittarius')
            if cls == 'Scorpio':
                locations = testing_data('Scorpio')
            if cls == 'Taurus':
                locations = testing_data('Taurus')
            if cls == 'Virgo':
                locations = testing_data('Virgo')
            rotate_angle = random.uniform(0, 360)
            brightness_adjust = random.uniform(-0.1, 0.1)
            img = create_constellation_image(locations, rotate_angle, brightness_adjust)
            cv2.imwrite(f"dataset/img/output/test/{cls}/{i}.jpg", img)
def test(model, test_img_num):
    global dataset_made
    print("-----------------------------")
    print(f"Loading model v{model}...")
    model = joblib.load(f'models/model{model}.sav')
    # Test Data
    if not dataset_made:
        print("Generating testing data...")
        make_test_data(test_img_num)
        dataset_made = True
    # Variables
    main_dir_path = 'dataset/img/output/test'
    correct = 0
    aquarius_correct = 0
    aries_correct = 0
    cancer_correct = 0
    capricorn_correct = 0
    gemini_correct = 0
    leo_correct = 0
    libra_correct = 0
    pisces_correct = 0
    sagittarius_correct = 0
    scorpio_correct = 0
    taurus_correct = 0
    virgo_correct = 0
    total = 0
    print("Testing...")
    for dirpath, dirnames, filenames in os.walk(main_dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            list1, list2 = process.process_raw(file_path, 10)
            final_list = []
            for i in range(len(list1)):
                final_list.append(list1[i])
                final_list.append(list2[i])
            for zero in range(42 - len(final_list)):
                final_list.append(0)
            if len(final_list) > 42:
                final_list = final_list[:42]
            final_list = np.array(final_list)
            final_list = final_list.reshape(1, -1)
            X_predict = np.array(final_list)
            prediction = model.predict(X_predict)
            clnum_dict = {'Aquarius': 0, 'Aries': 1, 'Cancer': 2, 'Capricorn': 3, 'Gemini': 4, 'Leo': 5, 'Libra': 6,
                          'Pisces': 7, 'Sagittarius': 8, 'Scorpio': 9, 'Taurus': 10, 'Virgo': 11}
            clnum = clnum_dict[prediction[0]]
            cur_con = 0
            if prediction[0] == os.path.basename(dirpath):
                correct+=1
                if prediction[0] == 'Aquarius':
                    aquarius_correct+=1
                elif prediction[0] == 'Aries':
                    aries_correct+=1
                elif prediction[0] == 'Cancer':
                    cancer_correct+=1
                elif prediction[0] == 'Capricorn':
                    capricorn_correct+=1
                elif prediction[0] == 'Gemini':
                    gemini_correct+=1
                elif prediction[0] == 'Leo':
                    leo_correct+=1
                elif prediction[0] == 'Libra':
                    libra_correct+=1
                elif prediction[0] == 'Pisces':
                    pisces_correct+=1
                elif prediction[0] == 'Sagittarius':
                    sagittarius_correct+=1
                elif prediction[0] == 'Scorpio':
                    scorpio_correct+=1
                elif prediction[0] == 'Taurus':
                    taurus_correct+=1
                elif prediction[0] == 'Virgo':
                    virgo_correct+=1
            total+=1
    print("-----------------------------")
    print(f"Aquarius: {aquarius_correct}/{test_img_num} | {(aquarius_correct/test_img_num)*100}"+"\n"+f"Aries: {aries_correct}/{test_img_num} | {(aries_correct/test_img_num)*100}"+"\n"+f"Cancer: {cancer_correct}/{test_img_num} | {(cancer_correct/test_img_num)*100}"+"\n"+f"Capricorn: {capricorn_correct}/{test_img_num} | {(capricorn_correct/test_img_num)*100}"+"\n"+f"Gemini: {gemini_correct}/{test_img_num} | {(gemini_correct/test_img_num)*100}"+"\n"+f"Leo: {leo_correct}/{test_img_num} | {(leo_correct/test_img_num)*100}"+"\n"+f"Libra: {libra_correct}/{test_img_num} | {(libra_correct/test_img_num)*100}"+"\n"+f"Pisces: {pisces_correct}/{test_img_num} | {(pisces_correct/test_img_num)*100}"+"\n"+f"Sagittarius: {sagittarius_correct}/{test_img_num} | {(sagittarius_correct/test_img_num)*100}"+"\n"+f"Scorpio: {scorpio_correct}/{test_img_num} | {(scorpio_correct/test_img_num)*100}"+"\n"+f"Taurus: {taurus_correct}/{test_img_num} | {(taurus_correct/test_img_num)*100}"+"\n"+f"Virgo: {virgo_correct}/{test_img_num} | {(virgo_correct/test_img_num)*100}")
    print("-----------")
    print(f"Correct: {correct}\nTotal: {total}")
    print("-----------")
    print(f"Accuracy: {correct/total*100}%")
    return correct/total*100

def list_test(start, end, test_img_num):
    scores = {}
    for x in range(start, end+1):
        scores[f"model{x}"] = test(x, test_img_num)
    print("-----------------------------")
    for key, value in scores.items():
        print(f"{key}: {value}%")

def list_test_mean(start, end, reps, test_img_num):
    scores = {}
    for model_names in range(start, end+1):
        scores[f"model{model_names}"] = []
    for x in range(start, end+1):
        scores[f"model{x}"].append(mean_test(x, reps, test_img_num))
    print("-----------------------------")
    for key, value in scores.items():
        print(f"{key}: {sum(value)/len(value)}%")

def mean_test(model, reps, test_img_num):
    scores = []
    for x in range(reps):
        scores.append(test(model, test_img_num))
    print("-----------------------------")
    print("Average:", str(sum(scores)/len(scores))+ "%")
    return sum(scores)/len(scores)

# Model Number, Number of Test Images
list_test_mean(23, 25, 1, 25)