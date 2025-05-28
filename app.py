import streamlit as st
import pickle
from src.assets import fetch_champion_assets
from src.data import round_pools
from src.logic import roll_champions

st.set_page_config(page_title="Brawl Rogue", layout="centered")

# Run fetch_champions on startup to ensure up to date
@st.cache_resource(show_spinner="Fetching champion icons...")
def init_champions():
    fetch_champion_assets()
init_champions()

# Load champion dict
champion_dict = pickle.load(open("assets/champions.pickle", "rb"))

# Session state
if "players" not in st.session_state:
    st.session_state.players = []
if "round_number" not in st.session_state:
    st.session_state.round_number = 1
if "checkpoint" not in st.session_state:
    st.session_state.checkpoint = 0

st.title("🏆 Brawl Rogue")

# Player entry
with st.expander("🎮 Add Players"):
    num_players = st.number_input("Number of players", min_value=2, max_value=10, step=1)
    for i in range(num_players):
        name = st.text_input(f"Player {i+1} name", key=f"player_{i}")
        if name:
            if name not in st.session_state.players:
                st.session_state.players.append(name)
    if len(st.session_state.players) == num_players:
        st.success("All players entered!")

# Main game logic
if len(st.session_state.players) >= 2:
    round_info = round_pools.get(st.session_state.round_number, {})
    st.subheader(f"🔄 Round {st.session_state.round_number}")
    st.caption(f"📜 Rule: {round_info.get('description', 'No description')}")

    if round_info.get("pool"):
        if st.button("🎲 Roll Champions"):
            result = roll_champions(st.session_state.players, round_info["pool"])
            if result:
                for p, champ in zip(st.session_state.players, result):
                    st.write(f"**{p}**: {champ}")
                    # Convert champion name to ID
                    champ_id = champion_dict[champ]
                    st.image(f"assets/icons/{champ_id}.png", width=50)
            else:
                st.warning("Not enough champions in pool!")
    else:
        st.info("Choose your own champions for this round!")

    # Controls
    col1, col2 = st.columns(2)
    if col1.button("✅ Win (Next Round)"):
        if st.session_state.round_number % 5 == 0:
            st.session_state.checkpoint = st.session_state.round_number
        st.session_state.round_number += 1

    if col2.button("❌ Loss (Back to Checkpoint)"):
        st.session_state.round_number = st.session_state.checkpoint + 1 if st.session_state.checkpoint > 0 else 1
