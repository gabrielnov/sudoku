import models
import copy
import board
import scores
import inputs

tab_copy = []

def start_game(level):
    
    tab, valid_plays_count = board.create_matrix(level)

    global tab_copy
    tab_copy = copy.deepcopy(tab)

    tries = 0

    while valid_plays_count > 0:
        board.clear_console()
        board.show_tab(tab)

        play = inputs.user_input(tab)    
        valid_input = inputs.valid(tab, play)
        
        while not valid_input:
            print("Esta jogada é inválida.Tente novamente!")
            play = inputs.user_input(tab)
            valid_input = inputs.valid(tab, play)

        
        board.update_tab(tab, play)

        tries += 1
        valid_plays_count -= 1

    print(f"Parabéns! Você resolveu o desafio em {tries} jogadas!")
    player = input("Entre seu nome para a lista de scores : ")

    game = models.Game(player, tries, level[2])
    
    scores.register(game)

def show_menu():
    board.clear_console()
    print("MENU PRINCIPAL\n(1) Ver scores\n(2) Jogar\n(3) Sair\n")
    option = input("Escolha uma opção: ")

    if option == '1':
        scores.read()
    if option == '2':
        level = inputs.level_selection()
        start_game(level)
    if option == '3':
        exit()

    show_menu()

def main():
    show_menu()   

    
      
main()
