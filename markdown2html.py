#!/usr/bin/python3

import sys
import os
import markdown

# Check the number of arguments
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

# Extract the input and output file names
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.exists(input_file):
    print("Missing", input_file, file=sys.stderr)
    sys.exit(1)

# Convert the Markdown file to HTML
with open(input_file, 'r') as f:
    markdown_content = f.read()
    html_content = markdown.markdown(markdown_content)

# Write the HTML content to the output file
with open(output_file, 'w') as f:
    f.write(html_content)

# Print nothing and exit with status 0 (success)
sys.exit(0)
