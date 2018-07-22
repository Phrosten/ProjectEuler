#! /usr/bin/python3

# This program takes a markdown file that was exported from the org file and
# further formats it to make the most of Github flavored markdown.
# I could probably do this in emacs, but I can't justify the amount of time,
# since my use of literate programming is minimal.

# Assumptions:
# The markdown file will contain two code blocks that are indented by 4 spaces.
# The first one is the code, the second one is the result.

import sys
import os

path = sys.argv[1]
lang = sys.argv[2]

with open(path, "r") as f:
    content = ""
    code = True
    block = False

    for line in f.readlines():
        if line.startswith("    "):
            if not block:
                if code:
                    content += "``` " + lang + "\n"
                else:
                    content += "## Result\n\n"
                    content += line
                block = True
            if code:
                content += line[4:]
        else:
            if block:
                content += "```\n"
                code = False
                block = False
            content += line

with open(os.path.dirname(path) + "/result.md", "w") as f:
    f.writelines(content)
