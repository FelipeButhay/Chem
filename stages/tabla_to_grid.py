import os
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')

def tabla_to_grid(z: list[int]) -> list[tuple[int]]:
             # [Z, NOMBRE, SIMBOLO, [PERIODO, GRUPO], ESTADO (0: vacio, 1: bien, 2:mal, 3:no en juego)]
    grid = [[None for x in range(18)] for y in range(10)]
    grid_data = []
    
    with open(f"{direc}/uwu.txt", "r", encoding="utf-8") as file:
        for line in list(file)[1:]:
            line = line.split(",")
            line[0] = int(line[0])
            line[3] = line[3].replace("(", "").replace(")", "").replace("\n", "").split(";")
            try:
                line[3] = [int(line[3][0])-1, int(line[3][1])-1]
            except:
                line[3] = [int(line[3][0])+3-1, int(line[3][1][:-1])+2-1]
                
            if line[0] in z:
                line.append(0)
            else:
                line.append(3)
                
            grid[line[3][0]][line[3][1]] = line
            grid_data.append(line)
            print(line)
            
    return grid, grid_data