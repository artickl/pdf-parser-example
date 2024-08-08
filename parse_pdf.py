#!/usr/bin/python3

import pymupdf #pip install pymupdf
import json

doc = pymupdf.open("out.pdf") 
jpage = json.loads(doc[0].get_text("json"))

print(json.dumps(jpage, indent=4))

#./parse_pdf.py | jq | less
#./parse_pdf.py | jq '.blocks[10].lines[0].spans[0].text'
## "6,864,026 articles in English"