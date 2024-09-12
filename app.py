from dungeon_generator import generate_grid_dungeon
from visualiser import draw_dungeon_grid
from assign_enemies_loot import assign_enemies_loot
from dungeon_details_generator import display_dungeon_details

def main():
    grid_size = 10
    num_rooms = 6
    dungeon_difficulty = 3

    dungeon, rooms = generate_grid_dungeon(grid_size, num_rooms)
    room_data = assign_enemies_loot(rooms, dungeon_difficulty)

    display_dungeon_details(room_data)
    draw_dungeon_grid(dungeon)


if __name__ == "__main__":
    main()
