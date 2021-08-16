'''
This script is used to look for OS images from Azure marketplace
run "az vm image list --all" to get the latest list of images
Update allowed os image section to filter out allowed images
Author: Ankan Basu
'''
import collections
import json
import re

# run "az vm image list --all > vmimagelist.json"
# TODO: get the filename as an user input
with open('vmimagelist.json', 'r') as f:
    data = json.load(f)
    f.close()

my_dictionary = collections.defaultdict(list)
for item in data:
    my_dictionary[item['publisher']].append(item['sku'])

my_dictionary_set = {}
for k, v in my_dictionary.items():
    my_dictionary_set[k] = set(v)

print(f'Total number of publishers is {len(my_dictionary_set.keys())}')

with open('publisher_skus', 'w') as f:
    for k, v in my_dictionary_set.items():
        f.write(f'Publisher: {k}')
        f.write("------------------------------")
        f.write(f'Available SKUs:')
        for item in v:
            f.write(f'\t {item}')
        f.write("------------------------------")
    f.close()

def get_sku_for_publisher(publisher, mydict):
    return mydict[publisher]

print(get_sku_for_publisher('MicrosoftWindowsServer', my_dictionary_set))

# print(my_dictionary['MicrosoftWindowsServer'])
# print(my_d_set['MicrosoftWindowsServer'])

# for k, v in my_dictionary_set.items():
#     print(f'Publisher: {k}')
#     print("------------------------------")
#     print(f'Available SKUs:')
#     for item in v:
#         if re.search('win', item) or re.search('2016', item):
#             print(f'\t {item}')
#     print("------------------------------")