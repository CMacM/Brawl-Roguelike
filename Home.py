import streamlit as st
import pickle
import random
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

# Extract round pools and options
available_rounds = list(round_pools.keys())

# Merge any custom rules into the round_pools list
custom_rules = st.session_state.get("custom_rules", {})
combined_round_pools = {**round_pools, **custom_rules}
available_rounds = list(combined_round_pools.keys())
round_options = {k: v["description"] for k, v in combined_round_pools.items()}

# Session state
if "players" not in st.session_state:
    st.session_state.players = []
if "round_number" not in st.session_state:
    st.session_state.round_number = 1
if "checkpoint" not in st.session_state:
    st.session_state.checkpoint = 0
if "round_schedule" not in st.session_state:
    st.session_state.round_schedule = []
if "pre_selected_rounds" not in st.session_state:
    st.session_state.pre_selected_rounds = []
if "checkpoint_rounds" not in st.session_state:
    st.session_state.checkpoint_rounds = []

# Title of page
st.title("🏆 Brawl Rogue")

# Round selection phase
if not st.session_state.round_schedule:
    st.subheader("🎲 Choose Your Rounds")

    num_rounds = st.number_input("How many rounds?", min_value=1, max_value=20, value=10)

    if num_rounds > len(available_rounds):
        st.warning("Not enough unique rules to fill all rounds!")
        st.stop()

    # Round rule selection interface
    manual_config = []
    cols = st.columns(2)

    # Left column: round rule pickers
    with cols[0]:
        for i in range(num_rounds):
            # Use saved selection if it exists; fallback to first option
            default = (
                st.session_state.pre_selected_rounds[i]
                if i < len(st.session_state.pre_selected_rounds)
                else available_rounds[0]
            )
            rule = st.selectbox(
                f"Round {i + 1}",
                options=available_rounds,
                format_func=lambda k: round_options[k],
                index=available_rounds.index(default),
                key=f"round_select_{i}"
            )
            manual_config.append(rule)

    # Right column: randomize + checkpoints
    with cols[1]:
        if st.button("🎰 Randomize All"):
            st.session_state.pre_selected_rounds = random.sample(available_rounds, k=num_rounds)
            st.rerun()

        st.session_state.checkpoint_rounds = st.multiselect(
            "📍 Select checkpoint rounds",
            options=list(range(1, num_rounds + 1)),
            default=[5, 10] if num_rounds >= 10 else [num_rounds],
        )

        st.markdown("Don't see the rule you want?")
        st.markdown("Add your own on the custom rules page!")

    if st.button("🚀 Start Game"):
        st.session_state.round_schedule = manual_config
        st.session_state.round_number = 1
        st.session_state.checkpoint = 0
        st.rerun()
else:
    # Player entry
    with st.expander("🎮 Add Players"):
        num_players = st.number_input("Number of players", min_value=2, max_value=10, step=1)
        for i in range(num_players):
            name = st.text_input(f"Player {i+1} name", key=f"player_{i}")
            if name and name not in st.session_state.players:
                st.session_state.players.append(name)
        if len(st.session_state.players) == num_players:
            st.success("All players entered!")

    # Main game logic
    if len(st.session_state.players) >= 2 and st.session_state.round_schedule:
        round_index = st.session_state.round_number - 1
        if round_index < len(st.session_state.round_schedule):
            rule_id = st.session_state.round_schedule[round_index]
            round_info = combined_round_pools.get(rule_id, {})
            description = round_info.get("description", "No description")
            pool = round_info.get("pool", [])

            st.subheader(f"🔄 Round {st.session_state.round_number}")
            st.caption(f"📜 Rule: {description}")

            if st.session_state.round_number in st.session_state.checkpoint_rounds:
                st.markdown("📍 **Checkpoint Round!** Win here to save progress.")

            if pool:
                if st.button("🎲 Roll Champions"):
                    result = roll_champions(st.session_state.players, pool)
                    if result:
                        for p, champ in zip(st.session_state.players, result):
                            st.write(f"**{p}**: {champ}")
                            champ_id = champion_dict.get(champ, champ)
                            st.image(f"assets/icons/{champ_id}.png", width=50)
                    else:
                        st.warning("Not enough champions in pool!")
            else:
                st.info("Choose your own champions for this round!")

            # Controls
            col1, col2 = st.columns(2)
            if col1.button("✅ Win (Next Round)"):
                if st.session_state.round_number in st.session_state.checkpoint_rounds:
                    st.session_state.checkpoint = st.session_state.round_number
                st.session_state.round_number += 1
                st.rerun()

            if col2.button("❌ Loss (Back to Checkpoint)"):
                st.session_state.round_number = (
                    st.session_state.checkpoint + 1 if st.session_state.checkpoint > 0 else 1
                )
                st.rerun()

    # Always show restart button
    st.markdown("---")
    if st.button("🔁 Restart Game"):
        st.session_state.round_schedule = []
        st.session_state.round_number = 1
        st.session_state.checkpoint = 0
        st.session_state.players = []
        st.session_state.pre_selected_rounds = []
        st.rerun()


