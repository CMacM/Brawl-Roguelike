import streamlit as st
import random
import time

def animate_champion_roll(players, pool, champion_dict):
    columns = st.columns(3)
    grouped = [[] for _ in range(3)]
    for idx, player in enumerate(players):
        grouped[idx % 3].append((idx, player))
    player_placeholders = [None] * len(players)
    name_placeholders = [None] * len(players)
    for col_idx, group in enumerate(grouped):
        with columns[col_idx]:
            for idx, player in group:
                name_placeholders[idx] = st.markdown(f"**{player}**")
                player_placeholders[idx] = st.empty()

    for t in range(15):
        delay = 0.03 + (t / 15) * 0.2
        for idx in range(len(players)):
            champ = random.choice(pool)
            champ_id = champion_dict.get(champ, champ)
            player_placeholders[idx].image(f"assets/icons/{champ_id}.png", width=100)
        time.sleep(delay)

    for idx in range(len(players)):
        name_placeholders[idx].empty()  # Clear the name placeholder
        player_placeholders[idx].empty()  # Clear the champion image placeholder


def animate_loot_roll(loot_dict):
    st.markdown("🎁 **Loot Incoming!**")
    time.sleep(1.5) # Short delay so players can read the message

    # Animate the loot roll
    loot_placeholder = st.empty()
    for t in range(15):
        roll = random.choice(list(loot_dict.keys())) # Randomly select a loot item to display
        loot_placeholder.image(f"{loot_dict[roll]['icon']}", width=100)
        time.sleep(0.03 + (t / 15) * 0.2)

    # Finalize the loot roll
    # Randomly select a final loot item based on the drop rates
    final_roll = random.choices(
        list(loot_dict.keys()),
        weights=[loot["drop_rate"] for loot in loot_dict.values()],
        k=1
    )[0]
    
    final_loot = loot_dict[final_roll] # Get the final loot item
    loot_placeholder.image(f"{final_loot['icon']}", width=100)
    time.sleep(1.5)

    return final_loot