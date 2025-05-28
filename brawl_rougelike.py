import random
import time

# Input players
players = []
num_players = int(input("Enter number of players (2-10): "))
while len(players) < num_players:
    player_name = input(f"Enter player {len(players) + 1} name: ").strip()
    if player_name and player_name not in players:
        players.append(player_name)
    else:
        print("Invalid name or already exists. Please try again.")

# Define custom pools for each round
round_pools = {
    1: {
        "description": "Easy/comfort picks for tanks",
        "pool": [
            "Alistar", "Amumu", "Blitz", "Braum", "Cho", "Mundo", "Ornn", "Galio", "Garen", "Ksante",
            "Leona", "Malphussy", "Maokai", "Naut", "Poppy", "Rammus", "Rell", "Sej", "Shen", "Singed",
            "Sion", "Skarner", "Tahm", "Taric", "Voli", "Zac"
        ]
    },
    2: {
        "description": "Mages",
        "pool": [
            "Ahri", "Anivia", "Annie", "Aurelion", "Aurora", "Azir", "Brand", "Cass", "Gragas", "Hwei", "Karma", 
            "Karthus", "Kass", "Kennen", "Leblanc", "Liss", "Lux", "Lulu", "Malz", "Mel", "Morgana", "Nami",
            "Neeko", "Nidalee", "Orianna", "Ryze", "Seraphine", "Sona", "Raka", "Syndra", "Taliyah", "TF",
            "Veigar", "Velkoz", "Vex", "Viktor", "Vlad", "Xerath", "Ziggs", "Zilean", "Zoe", "Zyra"
        ]
    },
    3: {
        "description": "Yordles",
        "pool": [
            "Amumu", "Corki", "Gnar", "Heimer", "Kennen", "Kled", "Lulu", "Ziggs", "Vex", "Poppy", "Trist", 
            "Teemo", "Veigar", "Smolder"
        ]
    },
    4: {
        "description": "Black champs",
        "pool": [
            "Akshan", "Ambessa", "Ekko", "Illaoi", "Lucian", "Mel", "Nidalee", "Samira", "Karma", "Nocturne",
            "Nilah", "Kayn", "Qiyana", "Zed", "Warwick", "Kindred"
        ]
    },
    5: {
        "description": "Build what enemy builds – CHECKPOINT (choose your own champ)",
        "pool": []  # Custom pick – handled differently in code
    },
    6: {
        "description": "ADC – picks get harder",
        "pool": [
            "Trist", "Lucian", "Jinx", "Ezreal", "Vayne", "Twitch", "Kalista", "Sivir", "Graves", "Kog",
            "Ashe", "Caitlyn", "Kaisa", "MF", "Corki", "Jhin", "Xayah", "Smolder", "Draven", "Varus",
            "Samira", "Senna", "Zeri", "TF", "Kindred", "Aphelos", "Akshan", "Quinn"
        ]
    },
    7: {
        "description": "Champions beginning with N",
        "pool": [
            "Nafiri", "Nami", "Nasus", "Naut", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu"
        ]
    },
    8: {
        "description": "Chads",
        "pool": [
            "Draven", "Darius", "Ali", "Aatrox", "Braum", "Mundo", "Garen", "Graves", "j4", "jayce",
            "ksante", "Panth", "Olaf", "Galio", "Sylas", "Sett"
        ]
    },
    9: {
        "description": "Big boobs",
        "pool": [
            "Ahri", "Ashe", "Cait", "Cass", "Diana", "Elise", "Eve", "Gragas", "Janna", "Irelia", "Kaisa",
            "Karma", "Katarina", "Akali", "Leblanc", "Lux", "Zyra", "Morg", "Sivir", "MF", "Nidalee", 
            "Leona", "Sona", "Syndra", "Vi", "Renata"
        ]
    },
    10: {
        "description": "Fully zoomed in – CHECKPOINT (choose your own champ)",
        "pool": []  # Custom pick – handled differently in code
    }
}


# Start at round 1, track last checkpoint
round_number = 1
checkpoint = 0

def play_round(round_number):
    round_info = round_pools.get(round_number, {})
    description = round_info.get("description", "No description")
    pool = round_info.get("pool", [])
    
    print(f"\n--- ROUND {round_number} ---")
    print(f"Rule: {description}")
    
    if not pool:  # Custom pick round
        print("Choose your own champion for this round!")
        return True

    if len(pool) < len(players):
        print("Not enough champions in the pool.")
        return False

    chosen = random.sample(pool, len(players))
    for p, champ in zip(players, chosen):
        print(f"{p}: {champ}")
    return True

# Game loop
while round_number <= max(round_pools.keys()):
    if not play_round(round_number):
        break
    result = input("Enter W (win) or L (loss): ").strip().upper()
    if result == "W":
        print("✅ Win! Proceeding to next round in...")
        for i in range(3, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            time.sleep(1)
        if round_number % 5 == 0:
            checkpoint = round_number
            print("✅ Checkpoint reached!")
        round_number += 1
    elif result == "L":
        print("❌ Loss! Returning to last checkpoint...")
        round_number = checkpoint + 1 if checkpoint > 0 else 1
    else:
        print("Invalid input. Please enter W or L.")
