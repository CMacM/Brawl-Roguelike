# Define custom pools for each round
round_pools = {
    1: {
        "description": "Easy/comfort picks for tanks",
        "pool": [
            "Alistar", "Amumu", "Blitzcrank", "Braum", "Cho'Gath", "Dr. Mundo", "Ornn", "Galio", "Garen", "K'Sante",
            "Leona", "Malphite", "Maokai", "Nautilus", "Poppy", "Rammus", "Rell", "Sejuani", "Shen", "Singed",
            "Sion", "Skarner", "Tahm Kench", "Taric", "Volibear", "Zac"
        ]
    },
    2: {
        "description": "Mages",
        "pool": [
            "Ahri", "Anivia", "Annie", "Aurelion Sol", "Aurora", "Azir", "Brand", "Cassiopeia", "Gragas", "Hwei", "Karma", 
            "Karthus", "Kassadin", "Kennen", "Leblanc", "Lissandra", "Lux", "Lulu", "Malzahar", "Mel", "Morgana", "Nami",
            "Neeko", "Nidalee", "Orianna", "Ryze", "Seraphine", "Sona", "Soraka", "Syndra", "Taliyah", "Twisted Fate",
            "Veigar", "Vel'Koz", "Vex", "Viktor", "Vladimir", "Xerath", "Ziggs", "Zilean", "Zoe", "Zyra"
        ]
    },
    3: {
        "description": "Yordles",
        "pool": [
            "Amumu", "Corki", "Gnar", "Heimerdinger", "Kennen", "Kled", "Lulu", "Ziggs", "Vex", "Poppy", "Tristana", 
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
        "description": "Build what enemy builds (choose your own champ)",
        "pool": []  # Custom pick – handled differently in code
    },
    6: {
        "description": "ADC – picks get harder",
        "pool": [
            "Tristana", "Lucian", "Jinx", "Ezreal", "Vayne", "Twitch", "Kalista", "Sivir", "Graves", "Kog'Maw",
            "Ashe", "Caitlyn", "Kai'Sa", "Miss Fortune", "Corki", "Jhin", "Xayah", "Smolder", "Draven", "Varus",
            "Samira", "Senna", "Zeri", "Twisted Fate", "Kindred", "Aphelios", "Akshan", "Quinn"
        ]
    },
    7: {
        "description": "Champions beginning with N",
        "pool": [
            "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump"
        ]
    },
    8: {
        "description": "Chads",
        "pool": [
            "Draven", "Darius", "Alistar", "Aatrox", "Braum", "Dr. Mundo", "Garen", "Graves", "Jarvan IV", "Jayce",
            "K'Sante", "Pantheon", "Olaf", "Galio", "Sylas", "Sett"
        ]
    },
    9: {
        "description": "Big boobs",
        "pool": [
            "Ahri", "Ashe", "Caitlyn", "Cassiopeia", "Diana", "Elise", "Evelynn", "Gragas", "Janna", "Irelia", "Kai'Sa",
            "Karma", "Katarina", "Akali", "Leblanc", "Lux", "Zyra", "Morgana", "Sivir", "Miss Fortune", "Nidalee", 
            "Leona", "Sona", "Syndra", "Vi", "Renata"
        ]
    },
    10: {
        "description": "Fully zoomed in (choose your own champ)",
        "pool": []  # Custom pick – handled differently in code
    },
    11: {
        "description": "Champions Ambre likes to play",
        "pool": [
            "Jinx","Gnar", "Sona", "Twitch", "Yuumi", "Shyvana", "Milio", "Lulu", "Seraphine", "Aurelion Sol",
            "Morgana", "Rammus", "Singed", "Soraka", "Teemo"
        ]
    }
}

round_pools[12] = {
    "description": "Worst win rates (this month)",
    "pool": ["Skarner", "Nidalee", "Rengar", "Kalista", "K'Sante", "Azir", "Gragas", "Ezreal", "Kled", "Corki"]
}
round_pools[13] = {
    "description": "Saw it once in the past 5 years",
    "pool": ["Taric", "Kled", "Kassadin", "Nilah", "Kennen", "Fiora", "Bel'Veth", "Zilean", "Qiyana", "Udyr"]
}
round_pools[14] = {
    "description": "Abs out",
    "pool": ["Akshan", "Aatrox", "Brand", "Dr.Mundo", "Gragas", "Jax", "Kayn", "Lee Sin", "Pantheon", "Renekton",
             "Ryze", "Sett", "Sylas", "Trundle", "Tryndamere", "Varus", "Udyr", "Viego", "Viktor", "Volibear",
             "Warwick", "Yasuo", "Yone"]
}
round_pools[15] = {
    "description": "Furries",
    "pool": ["Ahri", "Aurora", "Cassiopeia", "Elise", "Lillia", "Nami", "Neeko"]
}
round_pools[16] = {
    "description": "Ambre would pet in the wild",
    "pool": ["Amumu", "Fizz", "Gnar", "Heimerdinger", "Ivern", "Kennen", "Kindred", "Nunu", "Rumble",
             "Smolder", "Teemo", "Yuumi"]
}
round_pools[17] = {
    "description": "Ambre WOULD NOT pet in the wild",
    "pool": ["Alistar", "Cho'Gath", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "Malphite", "Maokai", "Naafiri",
             "Rammus", "Rek'Sai", "Renekton", "Rengar", "Skarner", "Tahm Kench", "Twitch", "Volibear",
             "Warwick", "Ziggs"]
}
round_pools[18] = {
    "description": "Ginger reps",
    "pool": ["Zyra", "Zoe", "Trundle", "Olaf", "Miss Fortune", "Gragas", "Gnar", "Aurora"]
}
round_pools[19] = {
    "description": "Questionable Morals",
    "pool": ["Bel'Veth", "Briar", "Cassiopeia", "Cho'Gath", "Dr.Mundo", "Elise", "Evelynn", "Fiddlesticks",
             "Jhin", "Karthus", "Kha'zix", "Lissandra", "Mordekaiser", "Nocturne", "Rek'Sai", "Singed", "Thresh",
             "Renata", "Twitch", "Varus", "Vel'Koz", "Jinx", "Ziggs", "Zyra", "Ambessa"]
}
round_pools[20] = {
    "description": "Heroes / Celebrated",
    "pool": ["Ashe", "Azir", "Braum", "Caitlyn", "Darius", "Galio", "Garren", "Heimerdinger", "Irelia",
             "Janna", "Jarvan IV", "Jayce", "K'Sante", "Kayle", "Kled", "Leona", "Lucian", "Lux", "Nasus",
             "Olaf", "Pantheon", "Poppy", "Quinn", "Ryze", "Sejuani", "Taric", "Tryndamere", "VI", "Wukong",
             "Master Yi", "Xin Zhao", "Ambessa"]
}
round_pools[21] = {
    "description": "The Fallen",
    "pool": ["Aatrox", "Brand", "Maokai", "Morgana", "Renekton", "Riven", "Shaco", "Sion", "Skarner", "Thresh",
             "Urgot", "Viego", "Viktor", "Xerath"]
}
round_pools[22] = {
    "description": "Out for vengeance",
    "pool": ["Alistar", "Aurelion Sol", "Azir", "Brand", "Kalista", "Kassadin", "Lucian", "Maokai", "Nautilus",
             "Pyke", "Rell", "Renekton", "Sylas", "Syndra", "Urgot", "Varus", "Vayne", "Viego"]
}