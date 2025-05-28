import os
import re
import requests
import pickle

def fetch_champion_assets():
    # Request latest version
    version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
    print(f"Getting champion list for version: {version}")

    # Get list of champions in current version
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
    response = requests.get(url)
    data = response.json()["data"]

    # Mapping: Display name → Riot's internal ID
    champion_id_map = {v["name"]: v["id"] for v in data.values()}

    # Write champion dictionary to assest file
    pickle.dump(champion_id_map, open("assets/champions.pickle", "wb"))

    output_dir = "assets/icons"
    base_url = f"http://ddragon.leagueoflegends.com/cdn/{version}/img/champion"

    os.makedirs(output_dir, exist_ok=True)

    failed_champs = []
    for champ in champion_id_map.keys():
        champ_id = champion_id_map[champ]
        url = f"{base_url}/{champ_id}.png"
        if os.path.exists(f"{output_dir}/{champ_id}.png"):
            continue
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(f"{output_dir}/{champ_id}.png", "wb") as f:
                f.write(response.content)
            print(f"✅ Downloaded: {champ} → {champ_id}.png")
        except Exception as e:
            print(f"❌ Failed: {champ} → {champ_id} ({e})")
            failed_champs.append(champ)

    if len(failed_champs) == 0:
        print("All champions downloaded successfully!")
    else:
        print("\nFailed to download the following champions:")
        print(failed_champs)