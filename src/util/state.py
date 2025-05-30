import streamlit as st

def init_session_state():
    defaults = {
        "players": [],
        "round_number": 1,
        "checkpoint": 0,
        "round_schedule": [],
        "checkpoint_rounds": [],
        "has_rolled": False,
        "disable_roll": False,
        "round_selections": {},
        "inventory": [],
        "num_rounds": 5,
        "loot_chance": 0.5,
        "pre_selected_rounds": [],
        "force_champ_pick": False,
        "force_team_pick": False,
        "activate_round_swap": False,
        "setback_override": False,
        "team_pick": None,
        "champ_picks": None,
        "activate_round_swap": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val
            print(f"Initialized session state: {key} = {val}")
