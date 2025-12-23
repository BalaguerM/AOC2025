fileInput = input(">>> ")

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

arrayP1 = [list(line.strip()) for line in file]

directions = (-1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1)
countP1 = 0
countP2 = 0
done = False 
loop = 0

while not done:
    done = True
    loop += 1

    arrayP2 = [row[:] for row in arrayP1]

    for x in range(len(arrayP1)):
        for y in range(len(arrayP1[x])):
            buffer = 0
            if arrayP1[x][y] == "@":            
                for dx, dy, in directions:
                    if 0 <= x+dx < len(arrayP1) and 0 <= y+dy < len(arrayP1[x]) and arrayP1[x+dx][y+dy] == "@": buffer += 1
                
                if buffer < 4: 
                    countP2 += 1
                    arrayP2[x][y] = "."
                    done = False
    
    arrayP1 = arrayP2
    
    if loop == 1: countP1 = countP2

print("Part 1:", countP1, "// Part 2:", countP2)