import argparse
from tabulate import tabulate

# Read the --name argument passed from the command line[cite: 38]
parser = argparse.ArgumentParser(description="A greeting tool with a table using tabulate.")
parser.add_argument("--name", default="World", help="The user's name")
args = parser.parse_args()

# Print a customized greeting[cite: 38]
print(f"Welcome to open source, {args.name}!\n")

# Data to display in the table[cite: 39]
rows = [
    ["Python", "Runs your code", "PSF-2.0"],
    ["Git", "Remembers every version", "GPL-2.0"],
    ["tabulate", "Makes text tables", "MIT"]
]

# Define column headers for the table[cite: 39]
headers = ["Tool", "What it does", "License"]

# Print the table in a grid format to the screen[cite: 39]
print(tabulate(rows, headers=headers, tablefmt="grid"))