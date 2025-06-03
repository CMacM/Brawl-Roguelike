import streamlit as st

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
        "policy": "post_roll",
        "drop_rate" : 0.3  # 20% chance to drop
    },
    "round_skip": {
        "flavour": "With her flaming stride, the Burning God forges paths where others see walls.",
        "description": "Skip the current round and proceed to the next one. May be used after rolling.",
        "display_name": "Boots of the Burning God",
        "icon": "assets/loot_icons/boots_of_the_burning_god.png",
        "name": "round_skip",
        "policy": "anytime",
        "drop_rate" : 0.05  # 30% chance to drop
    },
    "champ_pick": {
        "flavour": "High Summoner Samzur's codex was stolen, leaving the secret of summoning champions lost to time.",
        "description": "Each player can pick a champion from the pool. Must be used before rolling.",
        "display_name": "Samzur's Summoning Codex",
        "icon": "assets/loot_icons/samzurs_summoning_codex.png",
        "name": "champ_pick",
        "policy": "pre_roll",
        "drop_rate" : 0.05  # 30% chance to drop
    },
    "team_pick": {
        "flavour": "To sip from it is to share the burden of choice, but only one will reap the rewards.",
        "description": "Allows players to pick a champion for their team from the pool. Must be used before rolling.",
        "display_name": "Chalice of Unity",
        "icon": "assets/loot_icons/chalice_of_unity.png",
        "name": "team_pick",
        "policy": "pre_roll",
        "drop_rate" : 0.3  # 25% chance to drop
    },
    "round_swapper": {
        "flavour": "A most devious trickster, Rikstain used this wand to distort reality in his favor.",
        "description": "Swap the current round with any round in the schedule. Must be used before rolling.",
        "display_name": "Rikstain's Wand of Recursion",
        "icon": "assets/loot_icons/rikstains_wand_of_recursion.png",
        "name": "round_swapper",
        "policy": "pre_roll",
        "drop_rate" : 0.15  # 15% chance to drop
    },
    "gambletronic": {
        "flavour": "Once a staple in Zaunite Casinos, this device fell out of use with the advent of Chemtech.",
        "description": "Activates a random bonus effect for the current round. Whether it helps or hinders is up to fate.",
        "display_name": "Gambletronic Mk.IV",
        "icon": "assets/loot_icons/gambletronic_mkiv.png",
        "name": "gambletronic",
        "policy": "anytime",
        "drop_rate" : 0.2  # 20% chance to drop
    },
    "setbackatron": {
        "flavour": "Oddly familiar, this Hextech device seems to have come from another timeline.",
        "description": "A loss this round only sets you back one round",
        "display_name": "Chrono-tether Core",
        "icon": "assets/loot_icons/chrono-tether_core.png",
        "name": "setbackatron",
        "policy": "anytime",
        "drop_rate" : 0.05  # 10% chance to drop
    }
}

round_modifiers = {
    "item_mirror": {
        "description": "Build what the enemy builds this round.",
        "name": "Item Mirror",
        "flavour": "<span style=color:red>Error: ShopNotOpen</span> <br> *Attempting to mirror enemy items.*",
        "type": "debuff",
        "callback": None
    },
    "myopia": {
        "description": "Fully zoomed in this round.",
        "name": "Myopia",
        "flavour": "<span style=color:red>Error: FieldOfViewOverflow</span> <br> *Shrinking simulation bounds to prevent system crash.*",
        "type": "debuff",
        "callback": None
    },
    "poverty": {
        "description": "A random player may only spend 10000 gold this round.",
        "name": "Poverty",
        "flavour": "<span style=color:red>Error: EmptyWallet</span> <br> *Proceeding with bare hands.*",
        "type": "debuff",
        "callback": None
    },
    "itemless": {
        "description": "No items this round.",
        "name": "Itemless",
        "flavour": "<span style=color:red>Error: InventoryNotFound</span> <br> *Unable to retrieve item data.*",
        "type": "debuff",
        "callback": lambda: setattr(st.session_state, "disable_items", True)
    },
    "nemesis": {
        "description": "Each player may only kill 1 champion this round.",
        "name": "Nemesis",
        "flavour": "<span style=color:red>Error: EnemyTeamNotFound</span> <br> *Limiting players to single-target engagements.*",
        "type": "debuff",
        "callback": None
    },
    "flashless": {
        "description": "Cannot take Flash this round.",
        "name": "Flashless",
        "flavour": "<span style=color:red>Error: SummonerSpellNotFound</span> <br> *Flash spell not available.*",
        "type": "debuff",
        "callback": None
    },
    "weakult": {
        "description": "Can only put 1 point into your ultimate this round.",
        "name": "Weakult",
        "flavour": "<span style=color:red>Error: UltPowerOverflow</span> <br> *Limiting ultimate power to 1 point.*",
        "type": "debuff",
        "callback": None
    },
    "damage_dash": {
        "description": "Exceed an average of 25,000 damage per player this round to advance even if you lose",
        "name": "Damage Dash",
        "flavour": "<span style=color:green>DamageThreshold == **True**</span> <br> *Setting death counter to Null.*",
        "type": "buff",
        "callback": None
    },
    "godlike": {
        "description": "Nomitate a player. If this player gets 20 kills this round, advance even if you lose",
        "name": "Godlike",
        "flavour": "<span style=color:green>GodlikePlayer == **True**</span> <br> *Reducing player count to 1.*",
        "type": "buff",
        "callback": None
    },
    "assistance": {
        "description": "Exceed an average of 15 assists per player this round to advance even if you lose",
        "name": "Assistance",
        "flavour": "<span style=color:green>AssitanceDirective == **True**</span> <br> *Helping hand extended.*",
        "type": "buff",
        "callback": None
    },
    "minion_massacre": {
        "description": "Exceed an average of 200 CS per player this round to advance even if you lose",
        "name": "Minion Massacre",
        "flavour": "<span style=color:green>MinionMassacre == **True**</span> <br> *Engaging farming simulator.*",
        "type": "buff",
        "callback": None
    },
    "psychic": {
        "description": "Guess a champion that will be rolled to advance this round.",
        "name": "Psychic",
        "flavour": "<span style=color:green>RollCall == **True**</span> <br> *Setting seed to 0.*",
        "type": "buff",
        "callback": lambda: setattr(st.session_state, "psychic_mode", True)
    },
    "alchemy": {
        "description": "Convert 1 item into a Chrono-tether Core this round.",
        "name": "Alchemy",
        "flavour": "<span style=color:green>EnableTransumation == **True**</span>: *Overwriting item properties.*",
        "type": "buff",
        "callback": lambda: setattr(st.session_state, "alchemy_mode", True)
    }
}

print("Available Round Pools:")
for round_num, details in round_pools.items():
    print(f"Round {round_num}: {details['description']}")

print("\nAvailable Loot Options:")
for loot_key, loot_info in loot_dict.items():
    print(f"{loot_info['display_name']}: {loot_info['description']}")

print("\nAvailable Round Modifiers:")
for modifier_key, modifier_info in round_modifiers.items():
    print(f"{modifier_info['name']}: {modifier_info['description']} (Type: {modifier_info['type']})")
