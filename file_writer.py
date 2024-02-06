import json

def write_to_file(filename, data):

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)