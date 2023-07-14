#!/usr/bin/python3
import sys
import os
import re

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Define a regular expression pattern for matching headings
heading_pattern = r'^(#+)\s*(.*)$'

# Read the content of the input file
with open(input_file, 'r') as f:
    markdown_content = f.readlines()

# Convert markdown headings to HTML headings
html_content = []
for line in markdown_content:
    match = re.match(heading_pattern, line)
    if match:
        level = len(match.group(1))
        heading_text = match.group(2).strip()
        html_heading = f"<h{level}>{heading_text}</h{level}>"
        html_content.append(html_heading)
    else:
        html_content.append(line)

# Write the HTML content to the output file
with open(output_file, 'w') as f:
    f.writelines(html_content)

sys.exit(0)
