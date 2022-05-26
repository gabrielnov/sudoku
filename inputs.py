import solver
import models

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


    
def validate_input(x, tab):
    
    if x.isnumeric() and int(x) >= 0 and int(x) <= 4:
        return x

    if x.upper() == 'Q':
        solver.solve(tab)
        exit()

    n = input("Valor inválido. Tente novamente: ")

    return validate_input(n)

def user_input(tab):
    x = input("Linha (1 a 4 ou q) : ")
    x = int(validate_input(x, tab)) - 1
    
    y = input("Coluna (1 a 4 ou q) :")
    y = int(validate_input(y, tab)) -1
    
    n = input("Valor (1 a 4 ou q) : ")
    n = validate_input(n, tab)

    play = models.Play(x,y,n)

    return play

def level_selection():
    print("NÍVEL\n(1) Fácil\n(2) Médio\n(3) Difícil\n")
    level = input("Faça sua escolha: ")

    if level != '1' and level != '2' and level != '3':
        print("Opção inválida. Tenta novamente.\n\n")
        return level_selection()

    if level == '1':
        return [4, 6, 'Facil']
    if level == '2':
        return [7, 8, 'Medio']
    if level == '3':
        return [9, 16, 'Dificil']
