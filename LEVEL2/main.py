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

def process_tournament(tournament_info, rounds=100):
    #rounds = int(tournament_info[0][0])  # Number of rounds to simulate
    #number_of_fighters = int(tournament_info[0][1])  # Number of fighters in each tournament string
    
    results = []
    tournament_number = 1
    
    for tournament in tournament_info:
        print(f"\ntournament_number: {tournament_number}")
        fighters = list(tournament)
        
        # Loop for the specified number of rounds or until only one fighter remains
        for round_number in range(rounds):
            if len(fighters) == 1:
                break
            
            next_round = []
            # Pair fighters and decide the winner
            print(f"round_number: {round_number} ")
            for i in range(0, len(fighters)-1, 2):
                winner = decide_winner(fighters[i] + fighters[i + 1])
                print(f"Fighter 1: {fighters[i]} and fighter 2 {fighters[i+1]}. winner: {winner}")
                next_round.append(winner)
            
            fighters = next_round  # Move to the next round with the winners
            
        # Add the final result of this tournament to the results list
        results.append(''.join(fighters))
    
    return results

# Initialize a list to store the contents of each file


# Loop through the file names from 1 to 5
for i in range(1, 6):
    # Construct the file name
    file_contents = []
    filename = f"level4_{i}.out"
    
    # Open and read the contents of the file
    with open(filename, 'r') as file:
        # Read the lines and strip any extra whitespace or newline characters
        lines = [line.strip() for line in file.readlines()]
        
        # Append the contents to the file_contents list
        file_contents.append(lines)
    

    file_contents = file_contents[0]
    result = process_tournament(file_contents)
    print(file_contents)
    print(result)

    with open(filename.replace("out", "out2"), 'w') as file:
        for line in result:
            file.write(line+"\n")


# Display the contents of all files (optional)
# for i, content in enumerate(file_contents, start=1):
#     print(f"Contents of level1_{i}.in:")
#     for line in content:
#         print(line)
#     print("\n" + "-"*20 + "\n")
