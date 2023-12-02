with open('input1.txt', 'r') as f:
    lines = f.read().splitlines()

numbers =[]
result = 0

for line in lines:
    line_num = ""
    for x in line:
        if x.isdigit():
            line_num += x
    numbers.append(line_num)
                   
for number in range(len(numbers)):
    if len(numbers[number]) == 1:
        numbers[number] = numbers[number][0] + numbers[number][0]
    if len(numbers[number]) > 2:
        numbers[number] = numbers[number][0] + numbers[number][-1]

for num in numbers:
    result += int(num)

print(result)


