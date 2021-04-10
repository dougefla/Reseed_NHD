import json
import os
import time

def binarySearch_L (arr, l, r, x):

    mid = int(l + (r - l)/2)
    if r >= l:
        in_value = arr[mid]['size']
        if in_value == x:
            return mid
        elif in_value > x:
            return binarySearch_L(arr, l, mid-1, x)
        else:
            return binarySearch_L(arr, mid+1, r, x)
    else:
        while arr[l]['size']>=x:
            l-=1
        return l

def binarySearch_R (arr, l, r, x):

    mid = int(l + (r - l)/2)
    if r >= l:
        in_value = arr[mid]['size']
        if in_value == x:
            return mid
        elif in_value > x:
            return binarySearch_R(arr, l, mid-1, x)
        else:
            return binarySearch_R(arr, mid+1, r, x)
    else:
        while arr[r]['size']<=x:
            r+=1
        return r

def is_name_match(torrent_list, local_file_name):
    result = []
    for i in torrent_list:
        if local_file_name == i["name"]:
            result.append(i)
    return result

def check_structure(i, j):
    return -1

def compare(scan_result_dir, database_dict):
    has_open = 0
    while has_open < 100:
        try:
            with open(scan_result_dir,'r') as scan_result_f:
                scan_result_dict = json.load(scan_result_f)
            break
        except:
            time.sleep(0.1)
            has_open+=1
            print("Open {} Failed, retry times:{}".format(scan_result_dir,has_open))
    if has_open >= 100:
        return -1

    # with open('/var/www/flask-prod/database.json','r') as database_f:
    #     database_dict = json.load(database_f)
    result_size_test = []
    passkey = scan_result_dict["passkey"]
    result_structure_test = []
    # print('Start Searching... ...')
    db_torrent_list = database_dict["torrent"]

    # Build Index in order of size, from small to large
    db_torrent_sorted = sorted(db_torrent_list,key=lambda x:x['size'])

    for local_file in scan_result_dict["files"]:

        # Find the similar torrent in size
        local_file_size = local_file["total_size"]

        if local_file_size>db_torrent_sorted[-1]["size"] or local_file_size<db_torrent_sorted[0]["size"]:
            continue
        else:
            size_left = binarySearch_L(db_torrent_sorted, 0, len(db_torrent_sorted)-1, max(local_file_size-1000,0))
            size_right = binarySearch_R(db_torrent_sorted, 0, len(db_torrent_sorted)-1, local_file_size+1000)

            # Search the neibor torrents
            for j in range(size_left, size_right):

                if db_torrent_sorted[j]["name"] == local_file["name"]:
                    result_size_test.append(db_torrent_sorted[j]["id"])
                    # print("Local file {} and Torrent {} Passed the Size-Name-Test.".format(local_file["name"], db_torrent_sorted[j]["id"]))

                    if check_structure(db_torrent_sorted[j], local_file) == 1:
                        result_structure_test.append(db_torrent_sorted[j]["id"])
                        # print("Local file {} and Torrent {} Passed the Structure-Test.".format(local_file["name"], db_torrent_sorted[j]["id"]))
    result = ''
    for i in result_size_test:
        result+='http://www.nexushd.org/download.php?id='+str(i)+'&passkey='+passkey+'\n'

    return result

if __name__ == '__main__':
    path = "./upload/"
    database_dict = {}
    last_time = 0

    while 1:
        if time.time() - last_time > 3600:
            print("Loading database")
            last_time = time.time()
            counter = 0
            while counter<1000:
                try:
                    with open("database.json", 'rb') as database_f:
                        database_dict = json.load(database_f)
                    print("Loading successfully with time used:{} s".format(time.time()-last_time))
                    break
                except:
                    counter+=1
                    print("Retry open database")
            if counter >= 1000:
                print("Open database failed!")
                break

        files=os.listdir(path)
        if len(files) == 0:
            continue
        else:
            for i in files:
                result = compare(path+i,database_dict)
                if result == -1:
                    print("Open {} Failed!",i)
                else:
                    result_path = './results/'+i+'.txt'
                    with open(result_path,'w') as result_f:
                        result_f.write(result)
                    os.remove(path+i)