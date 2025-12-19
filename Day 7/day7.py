fileInput = "Day 7\inputD7.txt"

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

fileB = []
lineIdx = -1


for line in file: 
    line = line.rstrip("\n")
    fileB.append([line])


    for spike in line:
        if "^" in file[lineIdx]:
            spikeIdx = line.find("^")            
            line.count("^")

print(fileB)