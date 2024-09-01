import itertools



def decide_winner(fight: str) -> str:
    style1, style2 = fight
    

    if style1 == style2:
        return style2
    elif (style1 == 'S' and style2 == 'P') or (style1 == 'P' and style2 == 'R') or (style1 == 'R' and style2 == 'S'):
        return style1  
    else:
        return style2  
    
# input here the lines read by the program from the file, the first line must be the number of fights
def process_fights(list_fights):
    return_contents = []
    for i in range(1, int(list_fights[0])+1):
        return_contents.append(decide_winner(list_fights[i]))
    return return_contents

def process_tournament(tournament_info, rounds=2):
    results = []
    
    for tournament in tournament_info:
        fighters = list(tournament)
        
        # Loop for the specified number of rounds or until only one fighter remains
        for round_number in range(rounds):
            if len(fighters) == 1:
                break
            
            next_round = []
            # Pair fighters and decide the winner
            for i in range(0, len(fighters), 2):
                winner = decide_winner(fighters[i] + fighters[i + 1])
                next_round.append(winner)
            
            fighters = next_round  # Move to the next round with the winners
            
        # Add the final result of this tournament to the results list
        results.append(''.join(fighters))
    
    return results


# Initialize a list to store the contents of each file


def parse_fighter_string(fighter_string):
    fighters = []
    parts = fighter_string.split()
    for part in parts:
        count = int(part[:-1])  # Number before the letter
        style = part[-1]        # The last character, which is the style (R, P, S)
        fighters.extend([style] * count)
    return ''.join(fighters)


def generate_tournament(fighter_string):
    # Parse the input string
    fighters = parse_fighter_string(fighter_string)
    
    # Count the number of R, P, and S
    count_R = fighters.count('R')
    count_P = fighters.count('P')
    count_S = fighters.count('S')

    #print(count_R, count_P, count_S)
    # # Step 1: Pair all Rocks with all Papers
    fights = []

    while count_R > 0 and count_P > 0:
        if count_R > 0 and count_P > 0:
            # Add 'RP' pair
            fights.append('RP')
            count_R -= 1
            count_P -= 1
        
        if count_R > 1:
            # Add 'RR' pair
            fights.append('RR')
            count_R -= 2
        
        # Break the loop if neither 'RP' nor 'RR' can be added
        if count_R <= 0 or count_P <= 0:
            break


    # Step 3: Pair extra Papers with Scissors
    num_PS_pairs = min(count_P, count_S)
    fights.extend(['PS'] * num_PS_pairs)
    
    count_P -= num_PS_pairs
    count_S -= num_PS_pairs

    # Step 4: Pair remaining Scissors with themselves
    fights.extend(['SS'] * (count_S // 2))
    count_S -= 2 * (count_S // 2)

    # add the rest of the fighters at the start
    num_SR_pairs = min(count_R, count_S)
    fights.extend(['SR'] * (num_SR_pairs))
    count_R -= num_SR_pairs
    count_S -= num_SR_pairs

    #print(fights)
    # arange the final fights
    
    final_fights = fights
    #print(count_R, count_P, count_S)
    # Check if no Rock is left
    if 'R' in final_fights:
        return None
    return ''.join(final_fights)

# Loop through the file names from 1 to 5
for i in range(1, 2):
    # Construct the file name
    file_contents = []
    filename = f"level3_{i}.in"
    
    # Open and read the contents of the file
    with open(filename, 'r') as file:
        # Read the lines and strip any extra whitespace or newline characters
        lines = [line.strip() for line in file.readlines()]
        
        # Append the contents to the file_contents list
        file_contents.append(lines)
    

    file_contents = file_contents[0]
    result = []
    for line in file_contents[1:]:
        result.append(str(generate_tournament(line)))
    
    # result = process_tournament(file_contents)
    # print(file_contents)
    # print(result)

    with open(filename.replace("in", "out"), 'w') as file:
        for line in result:
            file.write(line+"\n")


# Display the contents of all files (optional)
# for i, content in enumerate(file_contents, start=1):
#     print(f"Contents of level1_{i}.in:")
#     for line in content:
#         print(line)
#     print("\n" + "-"*20 + "\n")
