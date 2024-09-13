import matplotlib.pyplot as plt
import numpy as np

def draw_dungeon_grid(ax, dungeon, room_data):
    # 0 (empty) -> white, 1 (room) -> blue, 2 (corridor) -> gray
    cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'gray'])
    bounds = [0, 1, 2, 3]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    
    ax.imshow(dungeon, cmap=cmap, norm=norm)
    ax.axis('off') 

    for room in room_data:
        x, y = room['coordinates']
        room_number = room['room_number']
        
        ax.text(y, x, str(room_number), color='black', ha='center', va='center',
                fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

def display_room_details(ax, room_data):
    ax.axis('off')

    table_data = []
    for room in room_data:
        room_number = room['room_number']
        enemies = ', '.join(room['enemies']) if room['enemies'] else 'None'
        loot = ', '.join(room['loot']) if room['loot'] else 'None'
        table_data.append([room_number, enemies, loot])

    table_data.insert(0, ['Room Number', 'Enemies', 'Loot'])

    table = ax.table(cellText=table_data, colLabels=None, loc='center', cellLoc='center')
    table.scale(1, 2)
    table.auto_set_font_size(False)

    header_cells = table[0, 0], table[0, 1], table[0, 2]
    for cell in header_cells:
        cell.set_text_props(weight='bold')  
        cell.set_facecolor('blue')       

    for (i, j), cell in table.get_celld().items():
        cell.set_linewidth(0.5)  
        cell.set_edgecolor('black')

    # Display table
    ax.add_table(table)

    
def plot_dungeon_with_details(dungeon, room_data):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))

    draw_dungeon_grid(ax1, dungeon, room_data)
    display_room_details(ax2, room_data)

    plt.show()
