def display_dungeon_details(room_data):
    print("Dungeon Room Details:")
    for i, room_info in enumerate(room_data, 1):
        position = room_info['coordinates']
        enemies = room_info['enemies']
        loot = room_info['loot']
        
        # print(f"Room {i} at position {position}:")
        print(f"Room {i}:")
        print(f"  Enemies: {enemies}")
        print(f"  Loot: {loot}\n")
