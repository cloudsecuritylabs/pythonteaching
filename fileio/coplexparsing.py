"""
0. start with lising allowed locations

get the list of publishers in allowed locations
1. az vm image list-publishers -l westus > publisher.westus.txt [location needs to come from a list]

find out all the image offers
2. az vm image list-offers -l westus -p microsoft-ads [publisher needs to come from a list]

3. az vm image list-skus -l westus -f windowsserver -p MicrosoftWindowsServer > windowsserver.txt [ this one will give us the sku's we need]

"""
import json
import re
# az vm image list-publishers -l centralus >> publishers.txt
# az vm image list-publishers -l eastus2 >> publishers.txt
# az vm image list-publishers -l northeurope >> publishers.txt
# az vm image list-publishers -l westeurope >> publishers.txt
# az vm image list-publishers -l eastasia >> publishers.txt
# az vm image list-publishers -l southeastasia >> publishers.txt
allowed_locations = ['centralus', 'eastus2', 'northeurope', 'westeurope', 'eastasia', 'southeastasia']

with open('publishers.txt', 'r') as f:
    data = json.load(f)
    f.close()

# extract sku from marketplace
publishers = []
for item in data:
    print(item['name'])
    publishers.append(item['name'])

print(len(publishers))
publisher_set = set(publishers)
print(len(publisher_set))

with open('trimmed_publishers.txt', 'w') as f:
    for p in publisher_set:
        f.write(f'{p} \n')
    f.close()

