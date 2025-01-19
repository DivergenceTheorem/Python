from package import HW8
import os
import json
import csv
import pickle

os.chdir("/Users/meirzhankurmanov/Documents/GitHub/Python/Python tutorials/HW8/test_directory")
directory = os.getcwd()

log = HW8.recursive_path(directory)

os.chdir("/Users/meirzhankurmanov/Documents/GitHub/Python/Python tutorials/HW8")

with (open('log_json.json', 'w', encoding = 'utf-8') as json_file, 
      open('log_csv.csv', 'w', encoding = 'utf-8', newline="") as csv_file,
      open('log_pickle.pickle', 'wb') as pickle_file):
    # JSON file:
    json.dump(log, json_file, ensure_ascii = False)

    # CSV file:
    csv_values = {
        'Directory': [], 
        'Existing directories': [], 
        'Existing files': [], 
        'Memory size': []
        }
    
    for key, value in log.items():
        csv_values['Directory'].append(key)
        csv_values['Existing directories'].append(value['Directories'])
        csv_values['Existing files'].append(value['Files'])
        csv_values['Memory size'].append(value['Size'])
        # csv_values.append([key, value['Directories'], value['Files'], value['Size']])
    
    writer = csv.DictWriter(csv_file, fieldnames=csv_values.keys())
    writer.writeheader()
    for row in zip(*csv_values.values()):
        writer.writerow(dict(zip(csv_values.keys(), row)))

    # Pickle file:
    pickle.dump(log, pickle_file)
    
    