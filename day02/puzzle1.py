with open('input2.txt', 'r') as f:
    lines = f.read().splitlines()

#print(lines)

line_num = 0

for line in lines[:5]:
    #print(line)
    #new_line = line.split()
    line_num +=1
    start = line.index(":") + 2
    #print(start)
    subsets = line[8:].split(sep=';')
    for subset in subsets:
        print(subset.strip())
    print("\n")
