#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)
# The actual conversion logic would go here
# For this example, we'll simply print the input and output filenames

print(f"Input file: {input_file}")
print(f"Output file: {output_file}")

sys.exit(0)
