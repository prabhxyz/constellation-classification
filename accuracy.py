import joblib
import numpy as np
import process
import os
import sys
sys.path.append('dataset')
import train_data_maker as all

# The model that is being tested.
model = joblib.load('models/model16.sav')
# Number of images generated per constellation.
print("Generating test data...")
all.make_test_data(5)

# Variables
correct = 0
total = 0

# set the main directory path
main_dir_path = 'dataset/img/output/test'
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
        total+=1

print(f"Correct: {correct}\nTotal: {total}")
print("-----------------------------")
print(f"Accuracy: {correct/total*100}%")