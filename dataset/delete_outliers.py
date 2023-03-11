import csv

# Define the number of coordinate pairs to remove for each constellation
num_pairs_to_remove = {"Aquarius":11, "Aries":3, "Cancer":4, "Capricorn":6, "Gemini":15, "Leo":10, "Libra":5, "Pisces":14, "Sagittarius":14, "Scorpio":9, "Taurus":9, "Virgo":9}

# Read in the data file
with open('constellation_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

# Keep track of the remaining rows
remaining_rows = []

# Loop through each row and remove the specified number of coordinate pairs for each constellation
current_constellation = ""
current_num_removed = 0
for row in rows:
    # Check if the current row is for a new constellation
    if row['constellation_name'] != current_constellation:
        current_constellation = row['constellation_name']
        current_num_removed = 0

    # Get the number of coordinate pairs to remove for the current constellation
    num_pairs = num_pairs_to_remove.get(current_constellation, 0)

    # Check if the current row still has coordinate pairs to remove
    if current_num_removed < num_pairs:
        current_num_removed += 1
    else:
        remaining_rows.append(row)

# Write the remaining rows to a new file
with open('constellations_filtered.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(remaining_rows)