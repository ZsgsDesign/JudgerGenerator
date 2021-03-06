import os
import re
import json
import hashlib

def file_extension(path): 
    return os.path.splitext(path)[1] 

def file_name(path): 
    return os.path.splitext(path)[0] 

if __name__ == '__main__':
    file_dir = "C:/Users/ZsgsD/Desktop/workspace/NOJ_Problems/NOJ1001/"
    f=os.listdir(file_dir)
    if os.path.exists(file_dir+"info"):
        print("INFO already exists")
        exit()
    test_cases_raw = set()
    for i in f:
        test_cases_raw.add(file_name(i))
    test_cases = {}
    index = 1
    for t in test_cases_raw:
        # print(t)
        with open(os.path.join(file_dir, f"{t}.in"), "r") as f:
            input_content=f.read()
        one_info = {
            "input_size": len(input_content),
            "input_name": f"{t}.in"
        }
        test_cases[index] = one_info
        index+=1

    info = {
        "spj": True,
        "test_cases": test_cases
    }

    with open(os.path.join(file_dir, "info"), "w", encoding="utf-8") as f:
        f.write(json.dumps(info, indent=4))
    print("INFO generated")
