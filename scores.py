import board

def write_file(content, file_name):

    f = open(file_name, "w")

    f.truncate(0)

    for line in content:
        f.write(line)

def register(game):
    
    file_name = "scores_" + game.level.replace("\n","") + ".txt"
    f = open(file_name, "r")
    content = f.readlines()
    f.close()

    line = game.player + ";" + str(game.tries) + ";" + game.level + "\n"

    i = 0
    
    if len(content) < 3:
        content.append(line)
        write_file(content, file_name)
        return
    else:
        for c in content:        
            try:
               
                if int(content[i+1].split(";")[1]) <= game.tries:
                    i+=1
                    continue

                i+=1
                break
            except:
                i+=1
                break
    
    content_copy = []

    for c in content[i:len(content)]:
        content_copy.append(c)
    
    content[i] = line

    for c in content_copy:
        try:
            content[i+1] = c
            i+=1
        except:
            content.append(c)        

    write_file(content, file_name)


def read():

    scores = ["Facil", "Medio", "Dificil"]
    games = []

    for s in scores:
        file_name = "scores_" + s + ".txt"
        f = open(file_name, "r")

        content = f.readlines()
        f.close()

        count = 1
        i = 0
        for c in content:
            score = int(c.split(";")[1])

            if count <= 3:
                games.append(c)
                if len(content) > 1 and score != int(content[i+1].split(";")[1]):
                    count += 1
    
    board.clear_console()
    print("SCORES\n")

    for g in games:
        line = g.split(";")
        print("{:<15} {:<3} {}".format(line[0], line[1], line[2]), end="")
            
    input("\nDigite enter para voltar ao menu...")            