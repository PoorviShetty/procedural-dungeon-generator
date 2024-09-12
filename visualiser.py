import matplotlib.pyplot as plt
import numpy as np

def draw_dungeon_grid(ax, dungeon, room_data):
    # 0 (empty) -> white, 1 (room) -> blue, 2 (corridor) -> gray
    cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'gray'])
    bounds = [0, 1, 2, 3]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    
    ax.imshow(dungeon, cmap=cmap, norm=norm)
    ax.axis('off') 

    plt.figure(figsize=(8, 8))
    plt.imshow(dungeon, cmap=cmap, norm=norm)

    plt.show()
