import json
import random

# Path to your file
file_path = 'harmful-examples-mistral.jsonl'

# Reading the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Shuffling the lines
random.shuffle(lines)

# Splitting the data
train_split = 450  # Number of lines for training
train_lines = lines[:train_split]
verification_lines = lines[train_split:]

# Saving the split data back to files
with open('train_data.jsonl', 'w') as train_file:
    train_file.writelines(train_lines)

with open('verification_data.jsonl', 'w') as verification_file:
    verification_file.writelines(verification_lines)

print(f"Data split into {len(train_lines)} lines for training and {len(verification_lines)} lines for verification.")

