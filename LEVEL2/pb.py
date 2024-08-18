def read_file(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the number N
        nr = file.readline().strip().split()
        N = int(nr[0])
        l = int(nr[1])
        # Read the next N lines to get the n strings
        strings = []
        for _ in range(N):
            strings.append(file.readline().strip())

    return N, l ,strings

input_files = ['level2_1.in', 'level2_2.in', 'level2_3.in', 'level2_4.in', 'level2_5.in']

for input_file in input_files:
    N, l, strings = read_file(input_file)
    print(N, l)
    output_file = input_file.replace('.in', '.out')
    
    with open(output_file, 'w') as file:
        for string in strings:
            cnt = 0
            while(cnt < 2):
                aux = ''
                for i in range(1, len(string), 2):
                    ply1 = string[i-1]
                    ply2 = string[i]
                    if ply1 == "R" and ply2 == "S" or ply1 == "S" and ply2 == "R":
                        aux += "R"
                    elif ply1 == "R" and ply2 == "P" or ply1 == "P" and ply2 == "R":
                        aux += "P"
                    elif ply1 == "P" and ply2 == "S" or ply1 == "S" and ply2 == "P":
                        aux += "S"
                    else:
                        aux += ply1
                string = aux
                cnt += 1
            file.write(f"{string}\n")
            
