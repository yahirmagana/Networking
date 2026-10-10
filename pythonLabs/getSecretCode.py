#!/usr/bin/python
import sys
import os
import re

html_content = os.popen('curl -s https://faridfarahmand.net/firstpage.html').read()

for line in html_content.splitlines():
    if 'secret code' in line.lower():
        clean_line = re.sub(r'<[^>]+>', '', line)
        
        if ':' in clean_line:
            secret_value = clean_line.split(':', 1)[1].strip()
            print(secret_value)
        break
