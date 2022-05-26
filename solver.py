import inputs
import models
import board
import copy

def find_possible_plays(tab, x, y):
    possible_plays = list()
    for i in range(1, 5):
        play = models.Play(x, y, str(i))
        if inputs.valid(tab, play):
            possible_plays.append(i)
    return possible_plays

def solver(tab_copy, solutions):
    for i in range(4):
        for j in range(4):
            if tab_copy[i][j] == '.':
                possible_plays = find_possible_plays(tab_copy, i, j)   
                for play in possible_plays:
                    tab_copy[i][j] = str(play)
                    solver(tab_copy, solutions)
                    tab_copy[i][j] = '.'
                return
    solutions.append(copy.deepcopy(tab_copy))
       

def solve(tab):
    solutions = list()
    print("\nCalculando soluções para: \n")
    board.show_tab(tab)
    solver(tab, solutions)

    if len(solutions) == 0:
        print("\nNenhuma solução encontrada para esse tabuleiro.\n")
    for s in solutions:
        board.show_tab(s)