import random

# The list of dates provided
dates = [
    "March 2", "March 3", "March 4", "March 5", "March 6",
    "March 9", "March 10", "March 11", "March 12", "March 13",
    "March 16", "March 17", "March 18", "March 24", "March 25",
    "March 26", "March 27", "March 30", "March 31", "April 1",
    "April 2", "April 3", "April 6", "April 7", "April 8"
]

seeds = [0, 1, 2, 3, 4]

for seed in seeds:
    # Work on a copy to keep the original list intact for each iteration
    shuffled_dates = dates.copy()

    # Initialize the random number generator with the specific seed
    random.seed(seed)

    # Perform the in-place shuffle
    random.shuffle(shuffled_dates)

    print(f"--- Seed {seed} ---")
    print(shuffled_dates)
    print("\n")