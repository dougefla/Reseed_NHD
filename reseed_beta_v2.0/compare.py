import json
import os

def dict2list(db_dict):
    result_list = []
    for i in db_dict.keys():
        temp_dict = {}
        temp_dict['index'] = i
        temp_dict['size'] = db_dict[i]['size']
        temp_dict['team'] = db_dict[i]['team']
        temp_dict['title'] = db_dict[i]['title']
        result_list.append(temp_dict)
    result_list2 = sorted(result_list, key=lambda list1: eval(list1["size"]))
    return result_list2

def binarySearch_L (arr, l, r, x):
    mid = int(l + (r - l)/2)
    if r >= l:
        in_value = eval(arr[mid]['size'])
        if in_value == x:
            return mid
        elif in_value > x:
            return binarySearch_L(arr, l, mid-1, x)
        else:
            return binarySearch_L(arr, mid+1, r, x)
    else:
        while eval(arr[l]['size'])>=x:
            l-=1
        return l

def binarySearch_R (arr, l, r, x):
    mid = int(l + (r - l)/2)
    if r >= l:
        in_value = eval(arr[mid]['size'])
        if in_value == x:
            return mid
        elif in_value > x:
            return binarySearch_R(arr, l, mid-1, x)
        else:
            return binarySearch_R(arr, mid+1, r, x)
    else:
        while eval(arr[r]['size'])<=x:
            r+=1
        return r

def main():
    print('Your Authkey:')
    authkey = input()
    print('Your Torrent_Pass')
    torrent_pass = input()
    with open('result.json','r') as local_json:
        local_files = json.load(local_json)
    with open('database.json','r') as database_json:
        database = json.load(database_json)
    
    database_list = dict2list(database)
    #print(database_list)
    result = []
    print('Start Searching... ...')
    for i in local_files.keys():
        try:
            name = i
            size = local_files[i]
            size_left = binarySearch_L(database_list, 0, len(database_list)-1, size-11000000)
            size_right = binarySearch_R(database_list, 0, len(database_list)-1, size+11000000)
            # for k in range(size_left, size_right):
            #     print(database_list[k])
            #print(size_left,size_right)
            for j in range(size_left, size_right):
                if database_list[j]['team'] in name:
                    title_db = (database_list[j]['title']).split()
                    time = title_db[-1].strip('[').strip(']')
                    if time in name:
                        main_title = title_db[0]
                        if '(AKA:' in title_db:
                            idx = title_db.index('(AKA:')
                            alt_title = (title_db[idx+1]).strip(')')
                        else:
                            alt_title = title_db[0]
                        if main_title in name or alt_title in name:
                            string = 'https://awesome-hd.me/torrents.php?action=download&id={}&authkey={}&torrent_pass={}'.format(str(j),authkey,torrent_pass)
                            result.append(string)
                            print(name, title_db)
        except:
            continue
        # for j in database.keys():
        #     try:
        #         data_size = eval(database[j]['size'])
        #         if data_size>size-10737418 and data_size<size+10737418:
        #             if database[j]['team'] in name:
        #                 title_db = (database[j]['title']).split()
        #                 time = title_db[-1].strip('[').strip(']')
        #                 if time in name:
        #                     main_title = title_db[0]
        #                     if '(AKA:' in title_db:
        #                         idx = title_db.index('(AKA:')
        #                         alt_title = title_db[idx+1]
        #                     else:
        #                         alt_title = title_db[0]
        #                     if main_title in name or alt_title in name:
        #                         string = 'https://awesome-hd.me/torrents.php?action=download&id={}&authkey={}&torrent_pass={}'.format(str(j),authkey,torrent_pass)
        #                         result.append(string)
        #     except:
        #         continue
    with open('torrent_link.txt','w') as f:
        f.writelines([line+'\n' for line in result])
    print('Done! Saved at:   ' + './torrent_link.txt')
if __name__ == '__main__':
    main()