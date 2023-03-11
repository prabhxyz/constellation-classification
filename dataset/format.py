import delete_columns

def format_csv():
    with open('constellation_data.csv', 'r') as file:
        lines = file.readlines()

    # Write new header as the first line
    with open('constellation_data.csv', 'w') as new_file:
        for line in lines:
            # split the line into columns using a comma as the separator
            columns = line.split(',')
            # check if all columns are empty (i.e., contain only whitespace)
            if all(col.strip() == '' for col in columns):
                continue  # skip the row if all columns are empty
            elif line.strip():  # check if line contains non-whitespace characters
                new_file.write(line)

    delete_columns.delete_columns()

if __name__ == '__main__':
    format_csv()
