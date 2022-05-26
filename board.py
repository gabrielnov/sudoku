import random
import os

def create_matrix(level):
    f = open("desafios.txt")

    content = f.readlines()
    
    f.close()

    valid_tabs = []

    for line in content:
        count = 0
        for c in line:
            if c == '.':
                count += 1
        
        if count >= level[0] and count <= level[1]:
            valid_tabs.append(line)
   
    print(valid_tabs)
    line = valid_tabs[random.randint(0, len(valid_tabs))]

    count = 0
    for i in range(16):
        if line[i] == '.':
            count += 1

    m = []

    i = 0
    j = 4
    for k in range(4):
        l = line[i:j]
        m.append(list(l))
        i = j 
        j = j + 4

    return m, count

def show_tab(m):
    for i in range (4):
        if i == 2:
            print("- - + - -")
        for j in range(4):
            if j == 2:
                print("|",  end=" ")
            print(m[i][j], end=" ")
        print()
    print("\n")

def update_tab(tab,play):
    tab[play.x][play.y] = play.n

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)