import json
import os

def main():
    print('Your Torrent_Pass')
    passkey = input()
    with open('result.json','r') as local_json:
        local_file = json.load(local_json)
    with open('database_NHD.json','r') as database_json:
        database = json.load(database_json)
    result = []
    print('Start Searching... ...')
    data_list = database.keys()

    for i in local_file.keys():
        if i in data_list:
            local_file_size = local_file[i]
            data_file_size = database[i][0]
            if local_file_size< data_file_size+10737418 and local_file_size> data_file_size-10737418 :
                result.append(database[i][1])
                print('Find Match Torrent ID: ' + str(database[i][1]))
    
    with open('torrent_link.txt','w') as f:
        for i in result:
            f.write('http://www.nexushd.org/download.php?id='+str(i)+'&passkey='+passkey+'\n')
    print('Done! Saved at:   ' + './torrent_link.txt')

if __name__ == '__main__':
    main()