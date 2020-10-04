import os
import base64
import re
import glob
import time
import datetime
import json
def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
def walk_dir(root_path,save_dir='.'):
    result = {}

    if not os.access(save_dir, os.W_OK):
        print("Save Path [{}] Is UNWRITABLE, Please Change Directories!".format(save_dir))
        return -1
    elif not os.access(root_path, os.R_OK):
        print("Index Path [{}] Is UNREADABLE, Please Check If The Path Is Correct!".format(root_path))
        return -1
    else:
        print("Start Scanning, Please wait...")

    for file in os.listdir(root_path):
        print("Building Index：{}".format(file))
        path = os.sep.join([root_path, file])
        if os.path.isfile(path):
            try:
                result[file] = os.path.getsize(path)
            except FileNotFoundError:
                print("File[{}]Exits But An Error Occurred While Reading. This Index May Be Incomplete. Please Check This File For Details And Try Again".format(path))
                continue
        else:
            try:
                result[file] = getFileSize(path)
            except FileNotFoundError:
                print("File[{}]Exits But An Error Occurred While Reading. This Index May Be Incomplete. Please Check This File For Details And Try Again".format(path))
                continue
    return result

def main():
    print("Path?")
    path = input()
    result = walk_dir(path)
    with open('result.json','w') as f:
        f.write(json.dumps(result))

if __name__ == '__main__':
    main()