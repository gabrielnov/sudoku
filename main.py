def create_matrix():
    f = open("desafios.txt")

    line = f.readline()
    m = []

    i = 0
    j = 4
    for k in range(4):
        l = line[i:j]
        m.append(list(l))
        i = j 
        j = j + 4

    return m

def show_tab(m):
    for i in range (4):
        print(m[i])
    print()

def get_col(m,index):
    v = []

    for i in range(4):
        v.append(m[i][index])
    return v

def solve(line, col):
    result, total = 0,0 
    
    print(f"line: {line}\n col {col}")

    for i in range(4):
        if line[i] == '.':
            line[i] = 0
            for j in range(4):
                if line[j] != '.':
                    total += int(line[j])
            result = 10 - total
            print(total)
            if result < 4:
                print(result)
        
        

def get_empty(m):
    show_tab(m)

    for i in range(4):
        for j in range(4):
            if m[i][j] == '.':
                line = m[i][0:4]
                col = get_col(m, j)
                solve(line, col)

def main():
    m = create_matrix()
    play = get_empty(m)
    
main()