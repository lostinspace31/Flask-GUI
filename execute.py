import sys
import os

if len(sys.argv) != 3:
    print("Usage: python execute.py <string1> <string2>")
    sys.exit(1)

string1 = sys.argv[1]
string2 = sys.argv[2]

# Define the directory and file path
directory = 'your_directory'  # Replace 'your_directory' with the desired directory path
file_path = os.path.join(directory, 'content.txt')

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Write strings to the file
with open(file_path, 'w') as file:
    file.write(f"{string1}\n{string2}")

print(f"Strings written to {file_path}")
