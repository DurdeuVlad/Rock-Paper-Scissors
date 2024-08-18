def read_file(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the number N
        nr = file.readline().strip().split()
        N = int(nr[0])
        M = int(nr[1])
        # Read the next N lines to get the n strings
        strings = []
        for _ in range(N):
            strings.append(file.readline().strip())

    return N, M ,strings

input_files = ['level3_1.in', 'level3_2.in', 'level3_3.in', 'level3_4.in', 'level3_5.in']

for input_file in input_files:
    N, M, strings = read_file(input_file)
    output_file = input_file.replace('.in', '.out')
    
    with open(output_file, 'w') as file:
        for string in strings:
            string = string.split(' ');
            c_map = {}
            for item in string:
                c_map[item[len(item)-1]] = int(item.replace(item[len(item)-1], ''));
            ans = ''
            while(c_map['R'] > 0):
                ans += 'R'
                c_map['R'] -= 1
                if(c_map['P'] > 0):
                    ans += 'P'
                    c_map['P'] -= 1
                if(c_map['R'] > 0):
                    ans += 'R'
                    c_map['R'] -= 1
                if(c_map['R'] > 0):
                    ans += 'R'
                    c_map['R'] -= 1
            while(c_map['P'] > 0):
                ans += 'P'
                c_map['P'] -= 1
            while(c_map['S'] > 0):
                ans += 'S'
                c_map['S'] -= 1
            file.write(f"{ans}\n")
                    
            
            
