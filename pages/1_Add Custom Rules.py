import streamlit as st
import pickle
from time import sleep

# Load champion dict (name → image filename)
champion_dict = pickle.load(open("assets/champions.pickle", "rb"))
champion_names = list(champion_dict.keys())

st.page_link("Home.py", label="Back to Home", icon="🏠")

st.title("🛠️ Create Custom Rule")

# Form inputs
rule_description = st.text_area("Rule Name", key="custom_rule_desc")

selected = set()

# Pool selection UI inside an expander
with st.expander("🧙 Select Champions for this Pool"):
    cols = st.columns(6)
    for i, champ in enumerate(sorted(champion_names)):
        champ_id = champion_dict[champ]
        col = cols[i % len(cols)]
        with col:
            st.image(f"assets/champ_icons/{champ_id}.png", width=60)
            if st.checkbox("", key=f"champ_{champ}"):
                selected.add(champ)

cols = st.columns(3)
with cols[0]:
    # Save custom rule
    if st.button("💾 Save Rule"):
        if not rule_description or not selected:
            st.warning("Please complete all fields and select at least one champion.")
        else:
            if "custom_rules" not in st.session_state:
                st.session_state.custom_rules = {}
            st.session_state.custom_rules[rule_description] = {
                "description": rule_description,
                "pool": list(selected)
            }
            st.success(f"Custom rule '{rule_description}' saved!")
            sleep(1)  # Delay to show success message

            # Clear inputs safely
            if "custom_rule_desc" in st.session_state:
                del st.session_state["custom_rule_desc"]
            for champ in champion_names:
                key = f"champ_{champ}"
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

with cols[2]:
    # Clear custom rules
    if st.button("🗑️ Clear Custom Rules"):
        st.session_state.round_selections = {}
        st.session_state.round_schedule = []
        st.session_state.checkpoint_rounds = []
        st.session_state.has_rolled = False
        st.session_state.round_number = 1
        st.session_state.checkpoint = 0
        if "custom_rules" in st.session_state:
            del st.session_state["custom_rules"]
            st.success("All custom rules cleared!")
        else:
            st.warning("No custom rules to clear.")
            sleep(1)
        st.rerun()
    st.markdown("This will reset the game and clear all selections, so be careful!")