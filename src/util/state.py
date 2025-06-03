import streamlit as st

def init_session_state():
    defaults = {
        "players": [],
        "round_number": 1,
        "checkpoint": 0,
        "round_schedule": [],
        "checkpoint_rounds": [],
        "has_rolled": False,
        "round_selections": {},
        "inventory": [],
        "num_rounds": 5,
        "loot_slider": 0.5,
        "modifier_slider": 0.25,
        "pre_selected_rounds": [],
        "force_champ_pick": False,
        "force_team_pick": False,
        "activate_round_swap": False,
        "setback_override": False,
        "team_pick": None,
        "champ_picks": None,
        "activate_round_swap": False,
        "disable_items": False,
        "psychic_mode": False,
        "psychic_prediction": None,
        "alchemy_mode": False,
        "ran_callback": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val
            print(f"Initialized session state: {key} = {val}")
