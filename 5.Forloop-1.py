import random

# Number of rolls
num_rolls = 20

# Counters
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0

previous_roll = 0

# Roll the die multiple times
for i in range(num_rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    # Count 6s and 1s
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1

    # Check for two 6s in a row
    if roll == 6 and previous_roll == 6:
        count_two_6s_in_a_row += 1

    # Update previous roll
    previous_roll = roll

# Output statistics
print("\nStatistics:")
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print(f"Number of times two 6s were rolled in a row: {count_two_6s_in_a_row}")
