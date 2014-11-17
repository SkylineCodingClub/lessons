#!/usr/bin/python

import sys
import json
import re

prefix = "sklinecodingclub.github.io/lessons/"

def find_slide_title(html):
    with open(html, "r") as fh:
        for line in fh:
            title_search = re.match('^# (.*)', line)
            if(title_search):
                return title_search.group(1) 

lesson_string = "<!-- Lesson list -->\n"
for html in sys.argv[1:]:
    title = find_slide_title(html)
    lesson_string += "[{0}]({1}{2})  \n".format(title, prefix, html)
lesson_string += "<!-- End lesson list -->"

readme_data = ""
with open("README.md", "r") as fh:
    readme_data = fh.read()
    readme_data = re.sub(r'<!-- Lesson list -->.*<!-- End lesson list -->', 
                         lesson_string, readme_data, flags=re.DOTALL)
fh.close();

with open("README.md", "w") as fh:
    fh.write(readme_data)
fh.close();
