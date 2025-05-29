import streamlit as st
import pickle

# Load champion dict (name → image filename)
champion_dict = pickle.load(open("assets/champions.pickle", "rb"))
champion_names = list(champion_dict.keys())

st.title("🛠️ Create Custom Rule")

# Form inputs
rule_name = st.text_input("Rule Name", key="custom_rule_name")
rule_description = st.text_area("Rule Description", key="custom_rule_desc")

selected = set()

# Pool selection UI inside an expander
with st.expander("🧙 Select Champions for this Pool"):
    cols = st.columns(6)
    for i, champ in enumerate(sorted(champion_names)):
        champ_id = champion_dict[champ]
        col = cols[i % len(cols)]
        with col:
            st.image(f"assets/icons/{champ_id}.png", width=60)
            if st.checkbox("", key=f"champ_{champ}"):
                selected.add(champ)

# Save custom rule
if st.button("💾 Save Rule"):
    if not rule_name or not rule_description or not selected:
        st.warning("Please complete all fields and select at least one champion.")
    else:
        if "custom_rules" not in st.session_state:
            st.session_state.custom_rules = {}
        st.session_state.custom_rules[rule_name] = {
            "description": rule_description,
            "pool": list(selected)
        }
        st.success(f"Custom rule '{rule_name}' saved!")

        # Clear inputs safely
        if "custom_rule_name" in st.session_state:
            del st.session_state["custom_rule_name"]
        if "custom_rule_desc" in st.session_state:
            del st.session_state["custom_rule_desc"]
        for champ in champion_names:
            key = f"champ_{champ}"
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()


