def determine_winner(char1, char2):
    if char1 == char2:
        return char1
    elif ((char1 == 'P' and char2 == 'S') or (char1 == 'S' and char2 == 'P')):
        return 'S'
    elif ((char1 == 'P' and char2 == 'R') or (char1 == 'R' and char2 == 'P')):
        return 'P'
    elif ((char1 == 'S' and char2 == 'R') or (char1 == 'R' and char2 == 'S')):
        return 'R'

# List of input files
input_files = ['level1_1.in', 'level1_2.in', 'level1_3.in', 'level1_4.in', 'level1_5.in']

# Process each file
for input_file in input_files:
    # Determine the corresponding output file name
    output_file = input_file.replace('.in', '.out')
    
    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # First line contains the number of entries
    n = int(lines[0].strip())

    # Open the output file for writing
    with open(output_file, 'w') as out_file:
        # Process each entry
        for i in range(1, n + 1):
            chars = lines[i].strip()
            char1, char2 = chars[0], chars[1]
            
            # Determine the winner
            result = determine_winner(char1, char2)
            
            # Write the result to the output file
            out_file.write(result + "\n")
