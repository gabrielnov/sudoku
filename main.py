import random
import copy

class Play:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

def create_matrix(level):
    f = open("desafios.txt")

    content = f.readlines()

    
    random_number = random.randrange(0,39)
    
    line = content[random_number]

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
    print("\n\n")
    
def validate_line_and_column(tab, play):
    
    for i in range(4):
        if tab[play.x][i] == play.n:
                return False
        
        if tab[i][play.y] == play.n:
                return False
    return True

def validate_quadrant(tab, play):
    x = play.x - 1 
    y = play.y - 1

    if play.x == 0 or play.x == 2:
        x = play.x+1

    if play.y == 0 or play.y == 2:
        y = play.y+1
    
    if tab[x][play.y] == play.n or tab[play.x][y] == play.n or tab[x][y] == play.n:
        return False

    return True

def valid(tab, play):

    if tab[play.x][play.y] == '.':

        quadrant = validate_quadrant(tab, play)

        line_and_col = validate_line_and_column(tab, play)

        return quadrant and line_and_col
    
    return False

def find_possible_plays(tab, x, y):
    possible_plays = list()
    for i in range(1, 5):
        play = Play(x, y, str(i))
        if valid(tab, play):
            possible_plays.append(i)
    return possible_plays

def solve(tab, solutions):
    for i in range(4):
        for j in range(4):
            if tab[i][j] == '.':
                possible_plays = find_possible_plays(tab, i, j)   
                for play in possible_plays:
                    tab[i][j] = str(play)
                    solve(tab, solutions)
                    tab[i][j] = '.'
                return
    show_tab(tab)        

def user_input():
    x = int(input("Linha (1 a 4 ou q) : ")) - 1
    
    y = int(input("Coluna (1 a 4 ou q) :")) - 1
    
    n = input("Valor (1 a 4 ou q) : ")

    play = Play(x,y,n)

    return play

def update_tab(tab,play):
    tab[play.x][play.y] = play.n
   
def start_game(tab, valid_plays_count):
    
    while valid_plays_count > 0:
        show_tab(tab)

        play = user_input()    
        valid_input = valid(tab, play)
        
        while not valid_input:
            print("Esta jogada é inválida.Tente novamente!")
            play = user_input()
            valid_input = valid(tab, play)

        update_tab(tab, play)

        valid_plays_count -= 1

    print("Parabéns voce ganhou!!!!!")

def main():
    tab, valid_plays_count = create_matrix()    

    tab_copy = copy.deepcopy(tab)
    start_game(tab,valid_plays_count)

    solutions = list()
    print("Calculando soluções para: ")
    show_tab(tab_copy)
    solve(tab, solutions)
    
      
main()