import matplotlib.pyplot as plt
import numpy as np

def draw_dungeon_grid(dungeon):
    # 0 (empty) -> white, 1 (room) -> blue, 2 (corridor) -> gray
    cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'gray'])
    bounds = [0, 1, 2, 3]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    plt.figure(figsize=(8, 8))
    plt.imshow(dungeon, cmap=cmap, norm=norm)

    plt.grid(False)
    
    room_count = 1
    for x in range(dungeon.shape[0]):
        for y in range(dungeon.shape[1]):
            if dungeon[x, y] == 1: 
                plt.text(y, x, str(room_count), color='white', ha='center', va='center', fontweight='bold')
                room_count += 1
    
    plt.show()
