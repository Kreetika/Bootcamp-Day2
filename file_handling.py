#capilizing the letters of next file
with open('sample.txt','w+') as file:
    lines = file.readlines()
    for line in lines:
        print(line.upper())