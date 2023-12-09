def game_formatting(a):
    new_game_list = []

    for i in range(len(a)):
        if a[i] == ":":
            new_str = a[i+1:].split(";")
            break
        else:
            pass
    
    for i in new_str:
        subset = i.strip()
        subset_split = subset.split(",")
        
        for j in subset_split:
            new_game_list.append(j.strip())
    
    return(new_game_list)

def game_totaling(b):
    game_dict = {"red": 0, "green": 0, "blue": 0}
    letters = ["r", "g", "b"]
    
    for cube in b:
        for result in range(len(cube)):
            if cube[result] in letters:
                if cube[result] == "r":
                    game_dict["red"] += int(cube[:result -1])
                elif cube[result] == "b":
                    game_dict["blue"] += int(cube[:result -1])
                elif cube[result] == "g":
                    game_dict["green"] += int(cube[:result -1])
                break
    
    return(game_dict)

def game_possible(c):
    possible = 0
    
    if c["red"] > 12 or c["blue"] > 14 or c["green"] > 13:
        possible = 2
    else:
        possible = 1
    return(possible)

with open('input2.txt', 'r') as f:
    games = f.read().splitlines()

game_sum = 0
counter = 1

for game in games:
    game_round = game_formatting(game)
    #print(game_round)
    game_total = game_totaling(game_round)
    #print(game_total)
    game_result = game_possible(game_total)
    #print(game_result)

    if game_result == 1:
        print(game_total)
        game_sum += counter
        print(game_sum)

    counter +=1

print(f"Sum of possible games: {game_sum}")
