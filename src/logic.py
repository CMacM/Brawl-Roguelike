import random

def roll_champions(players, round_pool):
    """
    Roll champions for players based on the round pool.
    If the round pool is empty or has fewer champions than players, return None.
    """
    if not round_pool or len(round_pool) < len(players):
        return None
    return random.sample(round_pool, len(players))

