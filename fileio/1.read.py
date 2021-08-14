# find all card numbers that are VISA
file = open('samplecreditcard.txt', 'r')
# print(file.read())

for line in file:
    line_split = line.split(',')
    # print(line_split[0])
    if (line_split[0] == 'Visa'):
        print(line_split[1])
    # count = count + 1


file.close()