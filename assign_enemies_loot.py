import random

def assign_enemies_loot(rooms, dungeon_difficulty):
    enemies_list = ['Goblin', 'Orc', 'Dragon', 'Troll', 'Skeleton', 'Vampire']
    loot_list = ['Gold', 'Sword', 'Shield', 'Potion', 'Magic Ring', 'Armor']

    room_data = []
    room_count = 1

    for (x, y) in rooms:
        num_enemies = random.randint(1, min(3, dungeon_difficulty)) 
        num_loot = random.randint(0, 2)

        enemies = random.sample(enemies_list, num_enemies)
        loot = random.sample(loot_list, num_loot)

        room_info = {
            'room_number': room_count,
            'coordinates': (x, y),
            'enemies': enemies,
            'loot': loot
        }

        room_data.append(room_info)
        room_count += 1

    return room_data
