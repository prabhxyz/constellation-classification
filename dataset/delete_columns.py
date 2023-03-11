import csv

def delete_columns():
    n = 43
    filename = 'constellation_data.csv'

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    new_data = [row[:n] for row in data]

    new_filename = 'constellation_data.csv'
    with open(new_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_data)