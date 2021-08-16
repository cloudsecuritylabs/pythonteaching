'''
This script is used to look for OS images from Azure marketplace
run "az vm image list --all" to get the latest list of images
Update allowed os image section to filter out allowed images
Author: Ankan Basu
'''
import json
import re

# run "az vm image list --all > vmimagelist.json"
# TODO: get the filename as an user input
with open('vmimagelist.json', 'r') as f:
    data = json.load(f)
    f.close()

print(data)

# extract sku from marketplace
sku = []
for item in data:
    sku.append(item['sku'])

# allowed OS from TDA as of August 4th, 2021
# only technologies applicable to Azure is listed here
allowed_os_sku = [
    'windows-server-2016',
    'windows-server-2019',
    'Windows-10:20h2',
    'ubuntu-20',
    'ubuntu-18',
    'suse15',
    'suse12',
    'rhel7',
    'rhel8',
    'oracle-linux-7',
    'oracle-linux-8',
    'centos-7',
]

'''
function to extract skus for allowed os types
'''
def get_sku(os_type, skulist):
    list = []
    for sku in skulist:
        if re.search(os_type, sku):
            list.append(sku)
    return list

allowd_urns = [] # store allowed urns

for os in allowed_os_sku:
    allowd_urns.extend(get_sku(os, sku))

with open('skulist.txt', 'w') as f:
    for urn in allowd_urns:
        f.write(f'{urn}\n')
    f.close()


print(allowd_urns)
print(len(allowd_urns))
