#!/usr/bin/env python3

import pdfkit #apt-get install wkhtmltopdf
pdfkit.from_url('https://en.wikipedia.org/wiki/Main_Page', 'out.pdf')