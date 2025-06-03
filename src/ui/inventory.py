import streamlit as st
import random
from src.data import loot_dict

def show_inventory(override=False):

    #for testing purposes
    if override:
        st.session_state.inventory = list(loot_dict.keys())

    st.subheader("🧰 Inventory")
    inventory = st.session_state.get("inventory", [])

    if not inventory:
        st.info("No loot items yet!")
        return

    if not st.session_state.disable_items:
        for idx, item in enumerate(inventory):

            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.image(item["icon"], width=100)

            with col2:
                st.markdown(f"<span style=\"color:orange\">**{item["display_name"]}**</span>: {item["description"]}", unsafe_allow_html=True)
                st.markdown(f"*\"{item["flavour"]}\"*")

            with col3:
                if item["policy"] == "pre_roll":
                    button = st.button(f"Use", key=f"use_item_{idx}", disabled=st.session_state.has_rolled)
                elif item["policy"] == "post_roll":
                    button = st.button(f"Use", key=f"use_item_{idx}", disabled=not st.session_state.has_rolled)
                else:
                    button = st.button(f"Use", key=f"use_item_{idx}")

                if button:
                    handle_item_use(item, idx)

def handle_item_use(item, index):
    item = item["name"] if isinstance(item, dict) else item
    if item == "reroll":
        #st.session_state.has_rolled = False
        st.session_state.has_rolled = False
        st.success("🔁 Champions will be re-rolled!")
    elif item == "round_skip":
        st.session_state.round_number += 1
        st.success("⏩ Round skipped!")
    elif item == "champ_pick":
        st.session_state.force_champ_pick = True
        st.success("🎯 Players will pick their champions!")
    elif item == "team_pick":
        st.session_state.force_team_pick = True
        st.success("👥 Team vote mode activated!")
    elif item == "round_swapper":
        st.session_state.activate_round_swap = True
        st.success("🔄 Swap a round in the schedule!")
    elif item == "gambletronic":
        gamble = random.choice(["boost", "penalty"])
        if gamble == "boost":
            st.session_state.round_number += 2
            st.balloons()
            st.success("🎰 Gambletronic boost! Skipped two rounds!")
        else:
            st.session_state.round_number = max(1, st.session_state.round_number - 2)
            st.error("💥 Gambletronic penalty! Back two rounds.")
    elif item == "setbackatron":
        st.session_state.setback_override = True
        st.info("⏳ If you lose, you'll only go back one round.")

    # Remove used item
    del st.session_state.inventory[index]
    st.rerun()
