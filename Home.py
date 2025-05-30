import streamlit as st
import pickle
import random
import math
import time
from src.assets import fetch_champion_assets, play_roll_sound
from src.data import round_pools
from logic.roll_champions import roll_champions

st.set_page_config(page_title="Brawlatron 3000", layout="centered")

# Run fetch_champions on startup to ensure up to date
@st.cache_resource(show_spinner="Fetching champion icons...")
def init_champions():
    fetch_champion_assets()
init_champions()

# Load champion dict
champion_dict = pickle.load(open("assets/champions.pickle", "rb"))

# Define loot pool globally near top or with roll_champions
loot_options = [
    "🔁 Re-roll", "⏩ Round Skip", "🎯 Champ Pick", "👥 Team Pick",
    "🔄 Round Swapper", "🎰 Gambletronic", "⏳ Setbackatron"
]

# Extract round pools and options
available_rounds = list(round_pools.keys())
max_rounds = len(available_rounds)

# Merge any custom rules into the round_pools list
custom_rules = st.session_state.get("custom_rules", {})
custom_rules_cleaned = {}
for i, key in enumerate(custom_rules.keys()):
    custom_rules_cleaned[max_rounds + i + 1] = {
        "description": key,
        "pool": custom_rules[key]["pool"]
    }
combined_round_pools = {**round_pools, **custom_rules_cleaned}

# Update available rounds and options
available_rounds = list(combined_round_pools.keys())
round_options = {k: v["description"] for k, v in combined_round_pools.items()}
max_rounds = len(available_rounds)

# Session state
if "players" not in st.session_state:
    st.session_state.players = []
if "round_number" not in st.session_state:
    st.session_state.round_number = 1
if "checkpoint" not in st.session_state:
    st.session_state.checkpoint = 0
if "round_schedule" not in st.session_state:
    st.session_state.round_schedule = []
if "checkpoint_rounds" not in st.session_state:
    st.session_state.checkpoint_rounds = [5,10,15,20]  # Default checkpoints
if "has_rolled" not in st.session_state:
    st.session_state.has_rolled = False
if "round_selections" not in st.session_state:
    st.session_state.round_selections = {}
if "inventory" not in st.session_state:
    st.session_state.inventory = []

# Round selection phase
if not st.session_state.round_schedule:
    # Title of page
    st.title("Brawlatron 3000 - The Brawl League Game")
    st.markdown("Welcome to Brawlatron 3000! 🎉")
    st.markdown(
        "This is a game where you and your friends can play a series of rounds with unique rules. "
        "Each round has its own set of champions to choose from, and you can customize the rules to fit your playstyle. "
        "Let's get started!"
    )

    st.subheader("🎲 Choose Your Rounds")

    # Number of rounds input
    max_rounds = len(available_rounds)
    default = st.session_state.num_rounds if "num_rounds" in st.session_state else 5
    num_rounds = st.number_input(
        "How many rounds?", 
        min_value=1,
        max_value=max_rounds,
        value=default,
        step=1,
        key="num_rounds"
    )

    # Pre-selected rounds
    if num_rounds > len(available_rounds):
        st.warning("Not enough unique rules to fill all rounds!")
        st.stop()

    st.session_state.pre_selected_rounds = random.sample(available_rounds, k=max_rounds)

    # Round rule selection interface
    manual_config = []
    cols = st.columns(2)

     # Right column: randomize + checkpoints
    with cols[1]:
        if st.button("🎰 Randomize All"):
            st.session_state.round_selections = {}
            st.session_state.pre_selected_rounds = random.sample(available_rounds, k=max_rounds)
            st.rerun()

        checkpoint_options = list(range(1, num_rounds + 1))

        # Filter out invalid checkpoint values once
        if "checkpoint_rounds" in st.session_state:
            st.session_state.checkpoint_rounds = [
                cp for cp in st.session_state.checkpoint_rounds if cp in checkpoint_options
            ]

        # Streamlit handles updates
        st.multiselect(
            "📍 Select checkpoint rounds",
            options=checkpoint_options,
            default=st.session_state.get("checkpoint_rounds", []),
            key="checkpoint_selector",
        )

        st.markdown("Don't see the rule you want?")
        st.page_link("pages/1_Add Custom Rules.py", label="Create Custom Rule", icon="🛠️")

        # Add vertical space
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🗑️ Clear Configuration"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.session_state.num_rounds = 5
            st.session_state.checkpoint_rounds = []
            st.rerun()
        
        if st.button("📖 View Custom Rules"):
            # Print custom rules in a text area outside the colums
            if "custom_rules" in st.session_state and st.session_state.custom_rules:
                for value in st.session_state.custom_rules.values():
                    st.markdown(f"### {value['description']}")
                    st.markdown("**Champions:** " + ", ".join(value["pool"]))
            else:
                st.markdown("No custom rules defined yet. Create some on the custom rules page!")

    # Left column: round rule pickers
    with cols[0]:
        for i in range(num_rounds):
            is_checkpoint = (i + 1) in st.session_state.checkpoint_rounds
            label = f"Round {i + 1}"
            if is_checkpoint:
                label += " 🚩 Checkpoint"

            default_rule = (
                st.session_state.pre_selected_rounds[i]
                if i < len(st.session_state.pre_selected_rounds)
                else available_rounds[0]
            )

            # Get current selection from session state or use default
            current_selection = st.session_state.round_selections.get(i, default_rule)

            # Render selectbox with current selection as default
            rule = st.selectbox(
                label,
                options=available_rounds,
                format_func=lambda k: round_options[k],
                index=available_rounds.index(current_selection),
                key=f"round_select_{i}"
            )

            # Store in session state
            st.session_state.round_selections[i] = rule
            manual_config.append(rule)

        if st.button("🚀 Start Game"):
            st.session_state.checkpoint_rounds = st.session_state.get("checkpoint_selector", [])
            st.session_state.round_schedule = [
                st.session_state.round_selections[i] for i in range(num_rounds)
            ]
            st.session_state.round_number = 1
            st.session_state.checkpoint = 0
            st.rerun()

else:
    num_rounds = len(st.session_state.round_schedule)

    if st.button("🔁 Restart Game"):
        st.session_state.round_schedule = []
        st.session_state.round_number = 1
        st.session_state.checkpoint = 0
        st.session_state.has_rolled = False
        st.session_state.num_rounds = num_rounds
        st.session_state.checkpoint_rounds = st.session_state.checkpoint_rounds
        st.session_state.inventory = []
        st.rerun()

    # Title of page
    st.title("Brawlatron 3000 - The Brawl League Game")
    st.markdown("Welcome to Brawlatron 3000! 🎉")
    st.markdown(
        "This is a game where you and your friends can play a series of rounds with unique rules. "
        "Each round has its own set of champions to choose from, and you can customize the rules to fit your playstyle. "
        "Let's get started!"
    )

    # Player entry
    with st.expander("🎮 Add Players"):
        max_players = 6
        num_players = st.number_input("Number of players", min_value=2, max_value=max_players, step=1)
        # Prevent adding more than `num_players` unique entries
        new_players = []
        for i in range(num_players):
            name = st.text_input(f"Player {i+1} name", key=f"player_{i}")
            if name:
                new_players.append(name)

        # Remove duplicates and limit total
        unique_players = list(dict.fromkeys(new_players))  # dedupe, preserve order
        if len(unique_players) > max_players:
            st.warning(f"Maximum {max_players} players allowed.")
        else:
            st.session_state.players = unique_players
            if len(unique_players) == num_players:
                st.success("All players entered!")

    # Main game logic
    if len(st.session_state.players) >= 2 and st.session_state.round_schedule:
        round_index = st.session_state.round_number - 1
        if round_index < len(st.session_state.round_schedule):
            rule_id = st.session_state.round_schedule[round_index]
            round_info = combined_round_pools.get(rule_id, {})
            description = round_info.get("description", "No description")
            pool = round_info.get("pool", [])

            st.header(f"⚔️ Round {st.session_state.round_number}")
            st.subheader(f"📜 Rule: {description}")

            #st.session_state.checkpoint_rounds = [5,10,15,20] #remove (just a hack)
            if st.session_state.round_number in st.session_state.checkpoint_rounds:
                st.markdown("📍 **Checkpoint Round!** Win here to save progress.")

            if pool:
                if st.button("🎲 Roll Champions"):
                    result = roll_champions(st.session_state.players, pool)
                    play_roll_sound()

                    columns = st.columns(3)
                    grouped = [[], [], []]
                    for idx, player in enumerate(st.session_state.players):
                        grouped[idx % 3].append((idx, player))

                    # Create placeholders once with name + image slots
                    player_placeholders = [None] * len(st.session_state.players)
                    for col_idx, group in enumerate(grouped):
                        with columns[col_idx]:
                            for idx, player in group:
                                st.markdown(f"**{player}**", unsafe_allow_html=True)
                                player_placeholders[idx] = st.empty()

                    # Animated rolling
                    for t in range(15):
                        delay = 0.03 + (t / 15) * 0.2
                        for idx, player in enumerate(st.session_state.players):
                            champ = random.choice(pool)
                            champ_id = champion_dict.get(champ, champ)
                            player_placeholders[idx].image(f"assets/icons/{champ_id}.png", width=100)
                        time.sleep(delay)

                    # Final result
                    for idx, (player, champ) in enumerate(zip(st.session_state.players, result)):
                        champ_id = champion_dict.get(champ, champ)
                        player_placeholders[idx].image(f"assets/icons/{champ_id}.png", width=100)

                    st.session_state.has_rolled = True
            else:
                st.info("Choose your own champions for this round!")
                st.session_state.has_rolled = True

    if st.session_state.has_rolled:
        col1, col2 = st.columns(2)
        if col1.button("🏆 Win (Next Round)"):
            if st.session_state.round_number in st.session_state.checkpoint_rounds:
                st.session_state.checkpoint = st.session_state.round_number
            st.session_state.round_number += 1
            st.session_state.has_rolled = False

            # LOOT DROP (Animated)
            got_loot = random.uniform(0, 1) < 0.1  # 10% chance to get loot
            if got_loot:
                st.markdown("🎁 **Loot Incoming!**")
                time.sleep(2)
                loot_placeholder = st.empty()

                # Animate spin
                for t in range(15):
                    delay = 0.03 + (t / 15) * 0.2
                    loot_spin = random.choice(loot_options)
                    loot_placeholder.markdown(f"### 🎲 {loot_spin}")
                    time.sleep(delay)

                # Final loot
                new_loot = random.choice(loot_options)
                loot_placeholder.markdown(f"## 🎉 **You got: {new_loot}!**")
                time.sleep(2)

                # Add to inventory
                st.session_state.inventory.append(new_loot)
            else:
                st.info("😞 No loot this time.")
                time.sleep(2)
            st.rerun()

        if col2.button("💀 Loss (Back to Checkpoint)"):
            st.session_state.round_number = (
                st.session_state.checkpoint + 1 if st.session_state.checkpoint > 0 else 1
            )
            st.session_state.has_rolled = False
            st.rerun()

    st.markdown("---")
    st.markdown("### 💰 Inventory")
    if st.session_state.inventory:
        st.markdown("You are carrying:")
        for i, item in enumerate(st.session_state.inventory):
            st.markdown(f"- {item}")
    else:
        st.markdown("_Inventory is empty_")


