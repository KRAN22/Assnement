# Problem
# --------
# 1. lcno = "LCNO-KAR-05-2004-0001

# validations

# LCNO - remains the same


import re

def regEx(ln):
    res = re.search(r'LCNO-(KAR|KER|TND|APN|TEL|MAH|GOA)-([0-6][1-9]|[0-7][0-3])-([2-9][0-9]{3})-(?!0000)[0-9]{4}', ln)
    if res:
        print(res.group(0))
        print("Match found")
    else:
        print("Match not found")

regEx("LCNO-KAR-05-2004-0010")
