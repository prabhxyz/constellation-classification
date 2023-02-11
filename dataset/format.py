import os
def format():
   with open('constellation_data.csv', 'r') as file:
       lines = file.readlines()

   # Keep every other line, starting with the first line
   with open('final.csv', 'w') as new_file:
       for i, line in enumerate(lines):
           if i % 2 == 0:
               new_file.write(line)

   os.remove("constellation_data.csv")
   os.rename("final.csv", "constellation_data.csv")

