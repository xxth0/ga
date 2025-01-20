import random

file_path = r"C:\Users\WINDOWS\Documents\ga\usr.txt"

with open(file_path, 'r') as file:
    entries = file.readlines()

winner = random.choice(entries).strip()

# Print the winner
print(f"{winner}")
