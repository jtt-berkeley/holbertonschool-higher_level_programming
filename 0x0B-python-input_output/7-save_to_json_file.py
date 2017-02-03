#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
