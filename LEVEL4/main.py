def parse_fighter_string(fighter_string):
    fighters = []
    parts = fighter_string.split()
    for part in parts:
        count = int(part[:-1])  # Number before the letter
        style = part[-1]        # The last character, which is the style (R, P, S)
        fighters.extend([style] * count)
    return fighters


def generate_tournament_old(fighter_string):
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

def generate_tournament(fighter_string):
    fighters = parse_fighter_string(fighter_string)
    
    # Count the number of each fighter type
    rock_count = fighters.count('R')
    paper_count = fighters.count('P')
    scissor_count = fighters.count('S')
    max_count = rock_count+paper_count+scissor_count
    
    # Initialize left and right halves
    left_half = []
    right_half = []
    
    # Handle the left half: all rocks and exactly one paper
    if rock_count > 0:
        left_half.extend(['R'] * min(rock_count, int(max_count/2)-1))
        rock_count -= min(rock_count, int(max_count/2)-1)  # most rocks placed
    if paper_count > 0:
        left_half.append('P')
        paper_count -= 1  # One paper placed
    
    # R < P*3
    # rp_pairs = min(paper_count, rock_count)
    # right_half.extend(['R', 'P'] * rp_pairs)

    # paper_count -= rp_pairs
    # rock_count -= rp_pairs
    
    if rock_count > paper_count*3:
        right_half=generate_tournament(str(rock_count)+"R "+str(paper_count)+"P "+str(scissor_count)+"S")
    else:
        while rock_count > 0 and paper_count > 0:
            if rock_count > 0 and paper_count > 0:
                # Add 'RP' pair
                right_half.append('RP')
                rock_count -= 1
                paper_count -= 1
            
            if rock_count > 1:
                # Add 'RR' pair
                right_half.append('RR')
                rock_count -= 2
            
            # Break the loop if neither 'RP' nor 'RR' can be added
            if rock_count <= 0 or paper_count <= 0:
                break   

        # Add remaining papers to the right half
        right_half.extend(['P'] * paper_count)
        

        # Add any remaining rocks
        if rock_count > 0:
            right_half.extend(['R'] * rock_count)
            rock_count = 0
        # Add any remaining scissors
        if scissor_count > 0:
            right_half.extend(['S'] * scissor_count)
            scissor_count = 0
    
    

    # Combine both halves to form the final tournament lineup
    left_half_string = ''.join(left_half)
    right_half_string = ''.join(right_half)
    print(left_half_string + '|' + right_half_string)
    full_string = left_half_string +right_half_string
    return full_string

# Example usage:
print(generate_tournament("25R 4P 3S"))  # Output will be based on the provided rules

def generate_tournaments(full_fight_list):
    result = []
    for line in full_fight_list[1:]:
        result.append(str(generate_tournament(line)))
    return result

# # Loop through the file names from 1 to 5
for i in range(1, 2):
    # Construct the file name
    file_contents = []
    filename = f"level4_{i}.in"
    
    # Open and read the contents of the file
    with open(filename, 'r') as file:
        # Read the lines and strip any extra whitespace or newline characters
        lines = [line.strip() for line in file.readlines()]
        
        # Append the contents to the file_contents list
        file_contents.append(lines)
    

    file_contents = file_contents[0]
    
    
    # result = process_tournament(file_contents)
    # print(file_contents)
    # print(result)
    result = generate_tournaments(file_contents)

    with open(filename.replace("in", "out"), 'w') as file:
        for line in result:
            file.write(line+"\n")


# Display the contents of all files (optional)
# for i, content in enumerate(file_contents, start=1):
#     print(f"Contents of level1_{i}.in:")
#     for line in content:
#         print(line)
#     print("\n" + "-"*20 + "\n")
