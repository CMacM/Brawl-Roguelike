import streamlit as st
import random
import time
import pickle

from src.assets import play_roll_sound
from src.data import loot_dict, round_modifiers
from src.logic.roll_champions import roll_champions
from src.ui.animations import animate_champion_roll, animate_loot_roll
from src.ui.inventory import show_inventory

# Load champion dict
champion_dict = pickle.load(open("assets/champions.pickle", "rb"))

num_rounds = len(st.session_state.round_schedule)
combined_round_pools = st.session_state.round_pools

if st.button("🔁 Restart Game"):
    st.session_state.round_schedule = []
    st.session_state.round_number = 1
    st.session_state.checkpoint = 0
    st.session_state.has_rolled = False
    st.session_state.has_rolled = False
    st.session_state.num_rounds = num_rounds
    st.session_state.loot_slider = st.session_state.loot_chance
    st.session_state.modifier_slider = st.session_state.modifier_chance
    st.session_state.checkpoint_rounds = st.session_state.checkpoint_rounds
    st.session_state.inventory = []
    st.switch_page("Home.py")

# Title of page
st.title("Brawlatron 3000")
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
        with st.expander("🧙 Champion Pool"):
            if pool:
                cols = st.columns(6)
                for i, champ in enumerate(sorted(pool)):
                    champ_id = champion_dict.get(champ, champ)
                    col = cols[i % len(cols)]
                    with col:
                        st.image(f"assets/icons/{champ_id}.png", width=60)
                        st.markdown(f"**{champ}**")
            else:
                st.info("No champions available for this round.")

        # Determine if bonus effects should be activated
        if "active_modifier" in st.session_state:
            modifier = st.session_state.active_modifier
            modifier = round_modifiers.get(modifier, {})

            # Run modifier callback
            if modifier["callback"] is not None and st.session_state.ran_callback is False:
                modifier["callback"]()
                st.session_state.ran_callback = True

            st.markdown(f"✨ **Bonus Modifier Activated!** {modifier['description']}")
            st.markdown(modifier['flavour'], unsafe_allow_html=True)

        if st.session_state.alchemy_mode:
            st.markdown("🧪 **Alchemy Mode Active!** Choose an item to transmute to Chrono-tether Core.")
            # Show alchemy options
            swap_item = st.selectbox(
                "Select an item to transmute:",
                options=st.session_state.inventory,
                format_func=lambda item: item["display_name"] if isinstance(item, dict) else item,
                key="alchemy_swap_select"
            )
            if st.button("Transmute to Chrono-tether Core"):
                if swap_item:
                    if isinstance(swap_item, dict):
                        st.session_state.inventory.remove(swap_item)
                        st.session_state.inventory.append(loot_dict["setbackatron"])
                        st.session_state.alchemy_mode = False
                        st.rerun()
                
        # Swap mode UI
        if st.session_state.activate_round_swap:
            st.session_state.has_rolled = True
            current_index = st.session_state.round_number - 1
            swap_options = list(enumerate(st.session_state.round_schedule))
            swap_index = st.selectbox(
                "Choose a round to swap with this one:",
                options=[i for i, _ in swap_options if i != current_index],
                format_func=lambda i: f"Round {i + 1}: {combined_round_pools[st.session_state.round_schedule[i]]['description']}",
                key="round_swap_select"
            )
            if st.button("Confirm Round Swap"):
                # Perform swap
                schedule = st.session_state.round_schedule
                schedule[current_index], schedule[swap_index] = schedule[swap_index], schedule[current_index]
                st.session_state.round_schedule = schedule
                st.session_state.activate_round_swap = False
                st.session_state.has_rolled = False
                st.success(f"✅ Swapped with Round {swap_index + 1}")
                time.sleep(1)  # Delay to show success message
                st.rerun()

        #st.session_state.checkpoint_rounds = [5,10,15,20] #remove (just a hack)
        if st.session_state.round_number in st.session_state.checkpoint_rounds:
            st.markdown("📍 **Checkpoint Round!** Win here to save progress.")

        if st.session_state.force_team_pick:
            # Disable rolling and allow team selection
            st.session_state.has_rolled = True
            st.markdown("👥 **Team Vote Mode Activated!** Players will choose a champion to secure")
            selected = st.selectbox(
                "Choose the champion the team wants to include:",
                options=pool,
                key="team_pick_selection"
            )

            if st.button("Confirm Team Pick"):
                if selected:
                    st.session_state.team_pick = selected
                    st.session_state.force_team_pick = False
                    st.session_state.has_rolled = False
                    st.success(f"✅ {selected} locked in for this round!")
                    time.sleep(1)  # Delay to show success message
                    st.rerun()
                else:
                    st.warning("Please choose a champion first.")
        
        elif st.session_state.force_champ_pick:
            st.session_state.has_rolled = True
            # Disable rolling and allow champion selection
            st.markdown("🎯 **Champ Pick Mode Activated!** Players will choose their champions")
            player_placeholders = []
            for player in st.session_state.players:
                selected = st.selectbox(
                    f"{player}, choose your champion:",
                    options=pool,
                    key=f"champ_pick_{player}"
                )
                player_placeholders.append(selected)
            
            allow_confirm = (len(set(player_placeholders)) == len(st.session_state.players))
            if not allow_confirm:
                st.warning("Players cannot select the same champion.")

            if st.button("Confirm Champion Picks", disabled= not allow_confirm):
                st.session_state.champ_picks = player_placeholders
                st.session_state.force_champ_pick = False
                st.session_state.has_rolled = False
                st.success("✅ Champions locked in for this round!")
                time.sleep(1)  # Delay to show success message
                st.rerun()

        elif st.session_state.psychic_mode:
            predicted_champ = st.selectbox(
                "🔮 Predict a champion for this round:",
                options=pool,
                key="psychic_selection"
            )
            if st.button("Confirm Prediction"):
                if predicted_champ in pool:
                    st.session_state.psychic_prediction = predicted_champ
                    st.success(f"✅ Psychic prediction set to: {predicted_champ}")
                    time.sleep(1)  # Delay to show success message
                    st.session_state.psychic_mode = False
                    del st.session_state.active_modifier  # Clear any active modifier
                    st.rerun()

        elif pool:
            # Champion selection phase
            if st.button(
                "🎲 Roll Champions", 
                disabled=st.session_state.has_rolled, 
                on_click=lambda: setattr(st.session_state, 'has_rolled', True)
            ):
                # Roll champions for this round
                result = roll_champions(st.session_state.players, pool)
                play_roll_sound()
                st.session_state.roll_results = result  # Store results in session state

                # Animate champion roll slot-machine style
                animate_champion_roll(
                    st.session_state.players, pool, champion_dict
                )

                # If team pick was confirmed, replace a random player's champion with the team pick
                if st.session_state.team_pick is not None:
                    random_player_index = random.randint(0, len(st.session_state.players) - 1)
                    result[random_player_index] = st.session_state.team_pick
                    st.session_state.team_pick = None  # Reset after use

                # If force champ pick was active, use those selections
                if st.session_state.champ_picks is not None:
                    result = st.session_state.champ_picks
                    st.session_state.champ_picks = None  # Reset after use

                # If psychic prediction was made, check if it matches
                if st.session_state.psychic_prediction is not None:
                    if st.session_state.psychic_prediction in result:
                        st.success(f"🔮 Psychic prediction succeeded! Advance a round")
                    else:
                        st.warning("🔮 Psychic prediction did not match any champion this round.")
                    st.session_state.psychic_prediction = None
        else:
            # Rule allows manual selection
            st.info("Choose your own champions for this round!")
            st.session_state.has_rolled = True


# After rolling show options to win or lose
if st.session_state.has_rolled:
    players = st.session_state.players
    columns = st.columns(3)
    grouped = [[] for _ in range(3)]
    for idx, player in enumerate(players):
        grouped[idx % 3].append((idx, player))
    player_placeholders = [None] * len(players)
    for col_idx, group in enumerate(grouped):
        with columns[col_idx]:
            for idx, player in group:
                st.markdown(f"**{player}**", unsafe_allow_html=True)
                player_placeholders[idx] = st.empty()

    # Display roll results
    for idx, (player, champ) in enumerate(zip(st.session_state.players, st.session_state.roll_results)):
        champ_id = champion_dict.get(champ, champ)
        player_placeholders[idx].image(f"assets/icons/{champ_id}.png", width=100)

    col1, col2 = st.columns(2)
    if col1.button("🏆 Win (Next Round)"):
        # Increment round number and reset has_rolled
        if st.session_state.round_number in st.session_state.checkpoint_rounds:
            st.session_state.checkpoint = st.session_state.round_number
        st.session_state.round_number += 1
        st.session_state.has_rolled = False
        st.session_state.has_rolled = False

        # Chance to get loot
        got_loot = random.uniform(0, 1) < st.session_state.loot_chance
        if got_loot:
            # Animate loot roll
            new_loot = animate_loot_roll(loot_dict)
            # Add to inventory if space
            if len(st.session_state.inventory) < 3:
                st.success(f"🎉 You got: {new_loot['display_name']}!")
                time.sleep(1)
                st.session_state.inventory.append(new_loot)
            else:
                st.warning("Inventory full!")
        else:
            st.info("😞 No loot this time.")
            time.sleep(1)

        st.session_state.disable_items = False  # Reset item usage state
        st.session_state.alchemy_mode = False  # Reset alchemy mode
        st.session_state.psychic_mode = False  # Reset psychic mode
        st.session_state.ran_callback = False  # Reset modifier callback state

        # Roll for bonus modifier next round
        activate_modifier = random.uniform(0, 1) <= st.session_state.modifier_chance
        if activate_modifier:
            modifier = random.choice(list(round_modifiers.keys()))
            st.session_state.active_modifier = modifier
        elif "active_modifier" in st.session_state:
            del st.session_state.active_modifier

        st.rerun()

    if col2.button("💀 Loss (Back to Checkpoint)"):
        if st.session_state.randomized:
            # re-draw the round schedule
            st.session_state.round_schedule = random.sample(
                st.session_state.round_schedule, len(st.session_state.round_schedule)
            )

        if st.session_state.get("setback_override", False):
            st.session_state.round_number = max(1, st.session_state.round_number - 1)
            st.session_state.setback_override = False
        else:
            st.session_state.round_number = (
                st.session_state.checkpoint + 1 if st.session_state.checkpoint > 0 else 1
            )
            # Lose inventory items
            st.session_state.inventory = []

        st.session_state.has_rolled = False
        st.session_state.has_rolled = False
        st.session_state.disable_items = False
        st.session_state.alchemy_mode = False
        st.session_state.psychic_mode = False
        st.session_state.ran_callback = False

        # Roll for bonus modifier next round
        activate_modifier = random.uniform(0, 1) <= st.session_state.modifier_chance
        if activate_modifier:
            modifier = random.choice(list(round_modifiers.keys()))
            st.session_state.active_modifier = modifier
        elif "active_modifier" in st.session_state:
            del st.session_state.active_modifier  # Clear any active modifier

        st.rerun()

st.markdown("---")
show_inventory(override=False)