import streamlit as st
import pickle
import random
import math
import time

from src.assets import fetch_champion_assets
from src.util.state import init_session_state
from src.data import round_pools, round_modifiers

st.set_page_config(page_title="Brawlatron 3000", layout="centered")

init_session_state()

# Run fetch_champions on startup to ensure up to date
@st.cache_resource(show_spinner="Fetching champion icons...")
def init_champions():
    fetch_champion_assets()
init_champions()

# Load champion dict
champion_dict = pickle.load(open("assets/champions.pickle", "rb"))

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
st.session_state.round_pools = combined_round_pools

# Update available rounds and options
available_rounds = list(combined_round_pools.keys())
round_options = {k: v["description"] for k, v in combined_round_pools.items()}
max_rounds = len(available_rounds)

# Title of page
_, col2, _ = st.columns([1, 3, 1])
with col2:
    st.image("assets/brawlatron3000_crop.png", width=600)
st.markdown("Welcome to Brawlatron 3000!")
st.markdown(
    "Originally built by a rogue faction of summoners, Brawlatron 3000 was meant to simulate epic battles across time and dimensions. " \
    "But somewhere deep in the code, something went wrong. " \
    "A fragment of sentience — stitched from old match data, champion echoes, and raw chaos — took hold. " \
    "Now the simulator is alive, unstable, and hungry for conflict. Every run is different. Every rule is bent. Every round could be your last. " \
    "Do you have what it takes to outsmart the Brawlatron and emerge victorious? "
)

# Number of rounds input
max_rounds = len(available_rounds)
num_rounds = st.number_input(
    "How many rounds?", 
    min_value=1,
    max_value=max_rounds,
    step=1,
    key="num_rounds"
)

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

# Pre-selected rounds
if num_rounds > len(available_rounds):
    st.warning("Not enough unique rules to fill all rounds!")
    st.stop()

if len(st.session_state.pre_selected_rounds) == 0:
    st.session_state.pre_selected_rounds = random.sample(available_rounds, k=max_rounds)

# check there are no duplicates
if len(set(st.session_state.pre_selected_rounds)) < max_rounds:
    st.warning("Duplicate rules detected in pre-selected rounds! Please refresh to try again.")
    st.stop()

st.slider(
    "🎲 Loot Chance",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    key="loot_slider",
    on_change=lambda: setattr(st.session_state, "loot_chance", st.session_state.loot_slider)
)

st.slider(
    "💥 Round Modifier Chance",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    key="modifier_slider",
    on_change=lambda: setattr(st.session_state, "modifier_chance", st.session_state.modifier_slider)
)

if "loot_chance" not in st.session_state:
    st.session_state.loot_chance = 0.5  # Default loot chance
if "modifier_chance" not in st.session_state:
    st.session_state.modifier_chance = 0.25  # Default modifier chance

cols1, cols2 = st.columns(2)
with cols1:
    if st.button("🚀 Start Fixed-Round Game"):
        st.session_state.checkpoint_rounds = st.session_state.get("checkpoint_selector", [])
        st.session_state.round_schedule = [
            st.session_state.round_selections[i] for i in range(num_rounds)
        ]
        st.session_state.round_number = 1
        st.session_state.checkpoint = 0
        st.session_state.randomized = False

        st.switch_page("pages/2_Game.py")
    st.markdown("(*Play with fixed rules for each round.*)")

with cols2:
    if st.button("🎰 Start Randomized Game"):
        st.session_state.checkpoint_rounds = st.session_state.get("checkpoint_selector", [])
        st.session_state.round_schedule = random.sample(
            st.session_state.pre_selected_rounds, k=num_rounds
        )
        st.session_state.round_number = 1
        st.session_state.checkpoint = 0
        st.session_state.randomized = True

        st.switch_page("pages/2_Game.py")
    st.markdown("(*Play with randomly selected rules each round.*)")

st.text("Want to play with specific rules for each round? You can manually configure the rounds below.")
with st.expander("🔧 Configure Rounds", expanded=False):

    # Round rule selection interface
    manual_config = []
    cols = st.columns(2)

        # Right column: randomize + checkpoints
    with cols[1]:
        if st.button("🎰 Randomize All"):
            st.session_state.round_selections = {}
            st.session_state.pre_selected_rounds = random.sample(available_rounds, k=max_rounds)
            st.rerun()

        st.markdown("Don't see the rule you want?")
        st.page_link("pages/1_Add Custom Rules.py", label="Create Custom Rule", icon="🛠️")

        # Add vertical space
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🗑️ Clear Configuration"):
            for key in st.session_state.keys():
                del st.session_state[key]
            # st.session_state.num_rounds = 5
            # st.session_state.checkpoint_rounds = []
            # st.session_state.loot_slider = 0.5
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
            is_checkpoint = (i + 1) in st.session_state.checkpoint_selector
            label = f"Round {i + 1}"
            if is_checkpoint:
                label += " 🚩 Checkpoint"

            # Get current selection from session state or use default
            current_selection = st.session_state.round_selections.get(i, st.session_state.pre_selected_rounds[i])

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

with st.expander("📜 View Modifiers", expanded=True):    
    for key, value in round_modifiers.items():
        st.markdown(f"{value["flavour"]}: ✨ **{value["description"]}**", unsafe_allow_html=True)
        #st.markdown("---")