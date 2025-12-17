fileInput = input(">>> ")

with open(fileInput, "r", encoding="utf-8") as f: file = [line.strip().split("-") for line in f.readline().split(",")]

rangedIds = []
solP1 = 0
solP2 = 0

try:
    for idx in range(len(file)):
        for i in range(int(file[idx][0]),int(file[idx][1]) + 1): rangedIds.append(i)
    
    for i in rangedIds:
        firstPart, secondPart = str(i)[:len(str(i)) // 2], str(i)[len(str(i)) // 2:]
        if firstPart == secondPart:
            solP1 = solP1 + i

# TO MODIFY
        s = str(i)
        n = len(s)
        for k in range(1, n // 2 + 1):
            if n % k == 0:
                if s[:k] * (n // k) == s:
                    solP2 = solP2 + i
                    break
                
finally: print("Part 1:", solP1, "Part 2:", solP2)