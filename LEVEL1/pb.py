# File reading function
def read_file(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the number N
        N = int(file.readline().strip())

        # Read the next N lines to get the n strings
        strings = []
        for _ in range(N):
            strings.append(file.readline().strip())

    return N, strings

# Example usage

input_files = ['level1_1.in', 'level1_2.in', 'level1_3.in', 'level1_4.in', 'level1_5.in']

for input_file in input_files:
    N, strings = read_file(input_file)
    output_file = input_file.replace('.in', '.out')
    
    with open(output_file, 'w') as file:
        for string in strings:
            ply1 = string[0]
            ply2 = string[1]
            if ply1 == "R" and ply2 == "S" or ply1 == "S" and ply2 == "R":
                file.write("R\n")
            elif ply1 == "R" and ply2 == "P" or ply1 == "P" and ply2 == "R":
                file.write("P\n")
            elif ply1 == "P" and ply2 == "S" or ply1 == "S" and ply2 == "P":
                file.write("S\n")
            else:
                file.write(f"{ply1}\n")

