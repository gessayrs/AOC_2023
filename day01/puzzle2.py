with open('input1.txt', 'r') as f:
    lines = f.read().splitlines()

numbers_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

values = []
result = 0

for line in lines:
    line_values =[]   
    for i in range(len(line)):
        if line[i].isdigit():
            line_values.append(line[i])
        elif i < len(line):
            if line[i:i+3] in numbers:
                line_values.append(numbers_dict[line[i:i+3]])
            elif line[i:i+4] in numbers:
                line_values.append(numbers_dict[line[i:i+4]])
            elif line[i:i+5] in numbers:
                line_values.append(numbers_dict[line[i:i+5]])
    values.append(str(line_values[0]) + str(line_values[-1]))

for i in values:
    result += int(i)

print(result)
