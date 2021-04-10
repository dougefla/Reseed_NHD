import os
import json

def list_to_path(path_list):
    path = ''
    for i in path_list:
        path = os.path.join(path, i)
    return path

def search_child(absolute_root, root_path_list, result_list):
    root_path = os.path.join(absolute_root,list_to_path(root_path_list))
    total_size = 0
    for file in os.listdir(root_path):
        path = os.sep.join([root_path, file])
        path_list = root_path_list + [file]
        if os.path.isfile(path):
            item = {}
            item["length"] = os.path.getsize(path)
            item["path"] = path_list
            result_list.append(item)
            total_size += os.path.getsize(path)
        else:
            total_size += search_child(absolute_root, path_list, result_list)
    return total_size


def search(absolute_root, root_path_list, result_dict):
    root_path = os.path.join(absolute_root,list_to_path(root_path_list))

    for file in os.listdir(root_path):
        path = os.sep.join([root_path, file])
        path_list = root_path_list + [file]
        item = {}
        item["name"] = file
        item["total_size"] = 0
        item["structure"] = []
        if os.path.isfile(path):
            item["structure"] = [{"length":os.path.getsize(path),"path":path_list}]
            item["total_size"] = os.path.getsize(path)
            result_dict["files"].append(item)
        else:
            temp_result_list = []
            item["total_size"] = search_child(absolute_root, path_list, temp_result_list)
            item["structure"] += temp_result_list
            result_dict["files"].append(item)
        print(item)

def start():
    print('++++++++++++++++++111++++111111111111111111111111111111111111111111111111111111111111111111111111111')
    print('111+111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111}}}}}}}}}}}}')
    print('111111111111111111111111111111111111111111111111111111111111111111}11}}}11}}1}1}}}}}}}}}}}}}}}}}}}}}')
    print('1111111111111111111111111111111111111111111111111111}}}}}}}}}}}}}}}}}}}}}1}}}}}}}}}}}}}}}}}}}}}}}}}}')
    print('111111111111111111111111}1}}}}}1}}}}}}}11111111111}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}')
    print('1111111111111111111111}}*.............:l}}}1}}1}}}}}}}}1....:..............,]]}}}}}}}}}}}}}}}}}}}}}}')
    print('1111111111111111}11}}1}];...............}}}1}11}}}}}}}}1...................;l}]}}}}}}}}}}}}}}}}}}]]]')
    print('11}}}}}}}}}}}}}}}}}}}}}}]]]]]l"...........]}}}}}}}}}}}}}lll]l1......."ll]ll]]}}]]]]]]]]]]]]]]]]]]]]]')
    print('}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]+............i]}}}}}}}}}}}}}}}}l.......1]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
    print('}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]+..............1}}}}}}}}}]]]]]]*.......1]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
    print('}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]+............:..~l]]]]]]]]]]]]]*.......1]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
    print('}}}}}}}}}}}}}}}}}}}}}]]]]]]]]]+................."l]]]]]]]]]]]*.......1l]]]]]]]]]]]]]]]]]]]]]llllllll')
    print('}}}}}}}}}}}}}]]]]]]]]]]]]]]]]]+..................`l]]]]]]]]]]*.......1l]]]]]]]]]]]]]llllllllllllllll')
    print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]l1.......}l1..........,*]l]]]]]]I.......1llllllllllllllllllllllllllllll')
    print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]l1.......}l]I:..........ll]ll]llI.......1llllllllllllllllllllllllllllll')
    print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]l1.......]l]lll:.........:*l]lllI.......1*lllllllllllllllllllllllllllll')
    print(']]]]]]]]]]]]]]]]]]]]]]]]l]l]]l1.......]l]]llI;..........}llllI.......1*lllllllllllllllllllllllll****')
    print(']]]]]lll]]]]llllllllllllllllll1.......]lllllllI`..........]llY.......1*lllllllll********************')
    print('lllllllllllllllllllllllllllll*1.......]llllll***".........."IY.......1******************************')
    print('lllllllllllllllllllllllllllll*1.......]*lllllllllY!..................1******************************')
    print('lllllllllllllllllllllllllllll*1.......l*********l**}.................1******************************')
    print('llllllllllllllllllll**********1.......l*************I1...............}I**********************IIIIIII')
    print('lllllllll*********************1.......l*********l*****Y:.:...........}I************IIIIIIIIIIIIIIIII')
    print('*****************************I1.......lI********I**I**I**:...........}IIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
    print('************************I**I*Yi.......1I*II*Y**I****IIII*X`..........}I*IIIIIIIIIIIIIIIIIIIIIIIIIIII')
    print('***********************Y~..................."IIIIIIIIIII***X:........}Y*IIIIIIIIIIIIIIIIIIIIIIIIIIII')
    print('**********************IY*..................:!Y*IIIIIIIIIIIIIX!.....::}YIIIIIIIIIIIIIIIIIIIIIIIIYYYYY')
    print('****************IIIIIIIIIIIIIIIIIIIIIIIIYIIIIIIIIIIIIIIIIIIIIIIIYYYYIIIIIIIIIYYYYYYYYYYYYYYYYYYYYYYY')
    print('*IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
    print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
    print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
    print('IIIIIIIIIIIIIIIIIIIIIIIIYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
    print('IIIIIIIIYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYXXXXXXXXXXXXXXX')
    print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYXXXYYYXXXXXXXXXXXXXXXXX')
    print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYXYYYXXYYYYYYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print()
    print()
    
    while 1:
        print('-------------------------------------- Reseed Tool for NexusHD --------------------------------------')
        print('+                                         Author: Douge@NHD                                         +')
        print('+                                            Version: 3.0                                           +')
        print('+                                                                                                   +')
        print('+                                             ATTENTION                                             +')
        print('+                          This program DO NOT store or upload any of your data.                    +')
        print('+                 DO NOT give anyone your torrent-password or the result.txt generated.             +')
        print('+                The comparation allows a small error, so DO check when you reseed them.            +')
        print('+                         We are not responsible for all the consequences caused.                   +')
        print('+                                                                                                   +')
        print('-----------------------------------------------------------------------------------------------------')

        absolute_root = input("Directory? (e.g. 'D:\动漫'):\n")
        passkey = input("Your passkey?:\n")
        root_path_list = []
        result_dict = {}
        result_dict["root"] = absolute_root
        result_dict["passkey"] = passkey
        result_dict["files"] = []
        search(absolute_root, root_path_list, result_dict)
        
        with open("scan_result.json",'wb') as scan_result_f:
            scan_result_json = (json.dumps(result_dict)).encode('utf-8')
            scan_result_f.write(scan_result_json)
        
        print("Done! Saved at:{}".format("./scan_result.json"))
        counter = 0
        while counter<10000000:
            counter+=1


if __name__ == '__main__':
    start()