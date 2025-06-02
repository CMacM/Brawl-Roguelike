# Define custom pools for each round
round_pools = {
    1: {
        "description": "Tank Time 🛡️",
        "pool": [
            "Alistar", "Amumu", "Blitzcrank", "Braum", "Cho'Gath", "Dr. Mundo", "Ornn", "Galio", "Garen", "K'Sante",
            "Leona", "Malphite", "Maokai", "Nautilus", "Poppy", "Rammus", "Rell", "Sejuani", "Shen", "Singed",
            "Sion", "Skarner", "Tahm Kench", "Taric", "Volibear", "Zac"
        ]
    },
    2: {
        "description": "Mage Madness 🔮",
        "pool": [
            "Ahri", "Anivia", "Annie", "Aurelion Sol", "Aurora", "Azir", "Brand", "Cassiopeia", "Gragas", "Hwei", "Karma", 
            "Karthus", "Kassadin", "Kennen", "Leblanc", "Lissandra", "Lux", "Lulu", "Malzahar", "Mel", "Morgana", "Nami",
            "Neeko", "Nidalee", "Orianna", "Ryze", "Seraphine", "Sona", "Soraka", "Syndra", "Taliyah", "Twisted Fate",
            "Veigar", "Vel'Koz", "Vex", "Viktor", "Vladimir", "Xerath", "Ziggs", "Zilean", "Zoe", "Zyra"
        ]
    },
    3: {
        "description": "Bandle City Brawlers 🎪",
        "pool": [
            "Amumu", "Corki", "Gnar", "Heimerdinger", "Kennen", "Kled", "Lulu", "Ziggs", "Vex", "Poppy", "Tristana", 
            "Teemo", "Veigar", "Smolder"
        ]
    },
    4: {
        "description": "Black Champs 🖤",
        "pool": [
            "Akshan", "Ambessa", "Ekko", "Illaoi", "Lucian", "Mel", "Nidalee", "Samira", "Karma", "Nocturne",
            "Nilah", "Kayn", "Qiyana", "Zed", "Warwick", "Kindred"
        ]
    },
    5: {
        "description": "Item Mirror (build what enemy builds) 🪞",
        "pool": []  # Custom pick – handled differently in code
    },
    6: {
        "description": "Don't get 1-shot (ADCs) 🎯",
        "pool": [
            "Tristana", "Lucian", "Jinx", "Ezreal", "Vayne", "Twitch", "Kalista", "Sivir", "Graves", "Kog'Maw",
            "Ashe", "Caitlyn", "Kai'Sa", "Miss Fortune", "Corki", "Jhin", "Xayah", "Smolder", "Draven", "Varus",
            "Samira", "Senna", "Zeri", "Twisted Fate", "Kindred", "Aphelios", "Akshan", "Quinn"
        ]
    },
    7: {
        "description": "NNNNNNNNNNNNNNN ☢️",
        "pool": [
            "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump"
        ]
    },
    8: {
        "description": "Chads Only 💪",
        "pool": [
            "Draven", "Darius", "Alistar", "Aatrox", "Braum", "Dr. Mundo", "Garen", "Graves", "Jarvan IV", "Jayce",
            "K'Sante", "Pantheon", "Olaf", "Galio", "Sylas", "Sett"
        ]
    },
    9: {
        "description": "Big Boob Bonanza 👙",
        "pool": [
            "Ahri", "Ashe", "Caitlyn", "Cassiopeia", "Diana", "Elise", "Evelynn", "Gragas", "Janna", "Irelia", "Kai'Sa",
            "Karma", "Katarina", "Akali", "Leblanc", "Lux", "Zyra", "Morgana", "Sivir", "Miss Fortune", "Nidalee", 
            "Leona", "Sona", "Syndra", "Vi", "Renata"
        ]
    },
    10: {
        "description": "Short Sighted (fully zoomed in) 🔎",
        "pool": []  # Custom pick – handled differently in code
    },
    11: {
        "description": "Ambre's Favourites 👧🏽",
        "pool": [
            "Jinx","Gnar", "Sona", "Twitch", "Yuumi", "Shyvana", "Milio", "Lulu", "Seraphine", "Aurelion Sol",
            "Morgana", "Rammus", "Singed", "Soraka", "Teemo"
        ]
    }
}

# Rules added by Ambre, need to make sure these are formatted better
round_pools[12] = {
    "description": "Worst Win Rates 📉",
    "pool": ["Skarner", "Nidalee", "Rengar", "Kalista", "K'Sante", "Azir", "Gragas", "Ezreal", "Kled", "Corki"]
}
round_pools[13] = {
    "description": "Saw it once in the past 5 years 💤",
    "pool": ["Taric", "Kled", "Kassadin", "Nilah", "Kennen", "Fiora", "Bel'Veth", "Zilean", "Qiyana", "Udyr"]
}
round_pools[14] = {
    "description": "Abs out 🆎",
    "pool": ["Akshan", "Aatrox", "Brand", "Dr. Mundo", "Gragas", "Jax", "Kayn", "Lee Sin", "Pantheon", "Renekton",
             "Ryze", "Sett", "Sylas", "Trundle", "Tryndamere", "Varus", "Udyr", "Viego", "Viktor", "Volibear",
             "Warwick", "Yasuo", "Yone"]
}
round_pools[15] = {
    "description": "Furries 🐯",
    "pool": ["Ahri", "Aurora", "Cassiopeia", "Elise", "Lillia", "Nami", "Neeko"]
}
round_pools[16] = {
    "description": "Ambre would pet in the wild 😻",
    "pool": ["Amumu", "Fizz", "Gnar", "Heimerdinger", "Ivern", "Kennen", "Kindred", "Nunu", "Rumble",
             "Smolder", "Teemo", "Yuumi"]
}
round_pools[17] = {
    "description": "Ambre WOULD NOT pet in the wild 🙀",
    "pool": ["Alistar", "Cho'Gath", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "Malphite", "Maokai", "Naafiri",
             "Rammus", "Rek'Sai", "Renekton", "Rengar", "Skarner", "Tahm Kench", "Twitch", "Volibear",
             "Warwick", "Ziggs"]
}
round_pools[18] = {
    "description": "Ginger Reps 🧡",
    "pool": ["Zyra", "Zoe", "Trundle", "Olaf", "Miss Fortune", "Gragas", "Gnar", "Aurora"]
}
round_pools[19] = {
    "description": "Questionable Morals 🤔",
    "pool": ["Bel'Veth", "Briar", "Cassiopeia", "Cho'Gath", "Dr. Mundo", "Elise", "Evelynn", "Fiddlesticks",
             "Jhin", "Karthus", "Kha'Zix", "Lissandra", "Mordekaiser", "Nocturne", "Rek'Sai", "Singed", "Thresh",
             "Renata", "Twitch", "Varus", "Vel'Koz", "Jinx", "Ziggs", "Zyra", "Ambessa"]
}
round_pools[20] = {
    "description": "Heroes of Runeterra 🏰",
    "pool": ["Ashe", "Azir", "Braum", "Caitlyn", "Darius", "Galio", "Garen", "Heimerdinger", "Irelia",
             "Janna", "Jarvan IV", "Jayce", "K'Sante", "Kayle", "Kled", "Leona", "Lucian", "Lux", "Nasus",
             "Olaf", "Pantheon", "Poppy", "Quinn", "Ryze", "Sejuani", "Taric", "Tryndamere", "Vi", "Wukong",
             "Master Yi", "Xin Zhao", "Ambessa"]
}
round_pools[21] = {
    "description": "The Fallen Ones 😈",
    "pool": ["Aatrox", "Brand", "Maokai", "Morgana", "Renekton", "Riven", "Shaco", "Sion", "Skarner", "Thresh",
             "Urgot", "Viego", "Viktor", "Xerath"]
}
round_pools[22] = {
    "description": "Out for Vengeance 🗡️",
    "pool": ["Alistar", "Aurelion Sol", "Azir", "Brand", "Kalista", "Kassadin", "Lucian", "Maokai", "Nautilus",
             "Pyke", "Rell", "Renekton", "Sylas", "Syndra", "Urgot", "Varus", "Vayne", "Viego"]
}

loot_dict = {
    "reroll": {
        "flavour": "The great gambler Makael's die won him many a game, until it cost his head.",
        "description": "Re-roll your champion selection for this round.",
        "display_name": "Makael's Magic Die",
        "icon": "assets/loot_icons/makaels_magic_die.png",
        "name": "reroll",
        "drop_rate" : 0.4  # 20% chance to drop
    },
    "round_skip": {
        "flavour": "Each step scorches the path forward, leaving no room for retreat.",
        "description": "Skip the current round and proceed to the next one. May be used after rolling.",
        "display_name": "Boots of the Burning God",
        "icon": "assets/loot_icons/boots_of_the_burning_god.png",
        "name": "round_skip",
        "drop_rate" : 0.05  # 30% chance to drop
    },
    "champ_pick": {
        "flavour": "High Summoner Samzur's codex was stolen, leaving the secret of summoning champions lost to time.",
        "description": "Each player can pick a champion from the pool. Must be used before rolling.",
        "display_name": "Samzur's Summoning Codex",
        "icon": "assets/loot_icons/samzurs_summoning_codex.png",
        "name": "champ_pick",
        "drop_rate" : 0.05  # 30% chance to drop
    },
    "team_pick": {
        "flavour": "To sip from it is to share the burden of choice, but only one will reap the rewards.",
        "description": "Allows players to pick a champion for their team from the pool. Must be used before rolling.",
        "display_name": "Chalice of Unity",
        "icon": "assets/loot_icons/chalice_of_unity.png",
        "name": "team_pick",
        "drop_rate" : 0.4  # 25% chance to drop
    },
    "round_swapper": {
        "flavour": "A most devious trickster, Rikstain used this wand to distort reality in his favor.",
        "description": "Swap the current round with any previous round. Can only be used once per game.",
        "display_name": "Rikstain's Wand of Recursion",
        "icon": "assets/loot_icons/rikstains_wand_of_recursion.png",
        "name": "round_swapper",
        "drop_rate" : 0.15  # 15% chance to drop
    },
    "gambletronic": {
        "flavour": "Once a staple in Zaunite Casinos, this device fell out use with the advent of Chemtech.",
        "description": "Activates a random bonus effect for the current round. Whether it helps or hinders is up to fate.",
        "display_name": "Gambletronic Mk.IV",
        "icon": "assets/loot_icons/gambletronic_mkiv.png",
        "name": "gambletronic",
        "drop_rate" : 0  # 20% chance to drop
    },
    "setbackatron": {
        "flavour": "Oddly familiar, this Hextech device seems to have come from another timeline.",
        "description": "A loss this round only sets you back one round",
        "display_name": "Chrono-tether Core",
        "icon": "assets/loot_icons/chrono-tether_core.png",
        "name": "setbackatron",
        "drop_rate" : 0.05  # 10% chance to drop
    }
}

print("Available Round Pools:")
for round_num, details in round_pools.items():
    print(f"Round {round_num}: {details['description']}")

print("\nAvailable Loot Options:")
for loot_key, loot_info in loot_dict.items():
    print(f"{loot_info['display_name']}: {loot_info['description']}")
