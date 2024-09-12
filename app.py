from dungeon_generator import generate_grid_dungeon
from visualiser import plot_dungeon_with_details
from assign_enemies_loot import assign_enemies_loot

def main():
    grid_size = 10
    num_rooms = 6
    dungeon_difficulty = 3

    dungeon, rooms = generate_grid_dungeon(grid_size, num_rooms)
    room_data = assign_enemies_loot(rooms, dungeon_difficulty)

    plot_dungeon_with_details(dungeon, room_data)

if __name__ == "__main__":
    main()
