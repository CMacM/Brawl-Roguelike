import streamlit as st
import random

def show_inventory(override=False):
    st.subheader("🎒 Inventory")
    inventory = st.session_state.get("inventory", [])

    # Give all items if override is True
    # for testing purposes
    if override:
        inventory = [
            "reroll", "round_skip", "champ_pick", "team_pick",
            "round_swapper", "gambletronic", "setbackatron"
        ]
        st.session_state.inventory = inventory

    if not inventory:
        st.info("No loot items yet!")
        return

    for idx, item in enumerate(inventory):
        display_name = item["display_name"]
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{display_name}**")
        with col2:
            if st.button(f"Use", key=f"use_item_{idx}"):
                handle_item_use(item, idx)

def loot_display_name(item_key):
    from src.data import loot_dict
    return loot_dict.get(item_key, {}).get("display_name", item_key)

def handle_item_use(item, index):
    item = item["name"] if isinstance(item, dict) else item
    if item == "reroll":
        #st.session_state.has_rolled = False
        st.success("🔁 Champions will be re-rolled!")
    elif item == "round_skip":
        st.session_state.round_number += 1
        st.success("⏩ Round skipped!")
        st.rerun()  # Refresh to update round number
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
