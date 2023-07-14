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
    html_content = markdown.markdown(
        markdown_content,
        extensions=['markdown.extensions.extra']
    )

# Parse headings and generate HTML
html_content = html_content.replace('<h1>', '<h1 class="heading">')
html_content = html_content.replace('<h2>', '<h2 class="heading">')
html_content = html_content.replace('<h3>', '<h3 class="heading">')
html_content = html_content.replace('<h4>', '<h4 class="heading">')
html_content = html_content.replace('<h5>', '<h5 class="heading">')
html_content = html_content.replace('<h6>', '<h6 class="heading">')

# Write the HTML content to the output file
with open(output_file, 'w') as f:
    f.write(html_content)

# Print nothing and exit with status 0 (success)
sys.exit(0)
In this updated version, I've added the markdown.extensions.extra extension to the markdown.markdown() function call. This extension enables additional Markdown syntax, including support for headers.

After converting the Markdown content to HTML, the script replaces the opening <h1> to <h6> tags with their respective versions but adds a class="heading" attribute. This allows for styling the headings with CSS if desired.

Save the updated script to markdown2html.py, and use it as mentioned before to convert the Markdown file to HTML, now with support for parsing headings.
