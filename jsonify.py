#!/usr/bin/python

import sys
import json
import re

def find_slide_title(html):
    with open(html, "r") as fh:
        for line in fh:
            title_search = re.match('^# (.*)', line)
            if(title_search):
                return title_search.group(1) 

file_data = []
for html in sys.argv[1:]:
    title = find_slide_title(html)
    file_data.append({
        'link': html,
        'title': title
    })

print json.dumps({
    "lessons": file_data
})

