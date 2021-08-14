# find all card numbers that are VISA
file = open('samplecreditcard.txt', 'r')
# print(file.read())

save = open('visacards.txt', 'w')
for line in file:
    line_split = line.split(',')
    # print(line_split[0])
    if (line_split[0] == 'Visa'):
        print(line_split[1])
        save.write(line_split[1])

# expand this example to store card numbers for American Express

file.close()
save.close()