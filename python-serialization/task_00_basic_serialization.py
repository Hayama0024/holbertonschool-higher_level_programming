#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r', encoding="UTF-8") as f:
        result = f.read()
    return json.loads(result)
