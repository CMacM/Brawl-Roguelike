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
        "pre_selected_rounds": [],
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val
