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

# extract urn
urn = []
for item in data:
    urn.append(item['urn'])

allowed_os = [
    'windows-server-2016',
    'windows-server-2019'
    'centos-7',
    'centos-8']

def get_urn(os_type, urnlist):
    list = []
    for urn in urnlist:
        if re.search(os_type, urn):
            list.append(urn)
    return list

allowd_urns = [] # store allowed urns

for os in allowed_os:
    allowd_urns.extend(get_urn(os, urn))
print(len(allowd_urns))


for os in allowd_urns:
    print(os)