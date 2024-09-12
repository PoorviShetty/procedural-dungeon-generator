import random
import numpy as np

def generate_grid_dungeon(grid_size, num_rooms):
    dungeon = np.zeros((grid_size, grid_size), dtype=int) 
    
    rooms = []
    for _ in range(num_rooms):
        while True:
            x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            if dungeon[x, y] == 0:  
                dungeon[x, y] = 1  
                rooms.append((x, y))
                break

    for i in range(1, len(rooms)):
        x1, y1 = rooms[i - 1]
        x2, y2 = rooms[i]
        if x1 != x2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if dungeon[x, y1] == 0:
                    dungeon[x, y1] = 2  

        if y1 != y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if dungeon[x2, y] == 0:
                    dungeon[x2, y] = 2
    
    return dungeon, rooms
