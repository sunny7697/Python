# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:31:52 2019

@author: SUNNY THAKUR
"""

import re

print((lambda p : len(p)>=6 and len(p)<=12 and " " not in p and any(c in "0123456789" for c in p) and any(c in "@#$" for c in p) and (not (re.search("[^A-Za-z0-9@$#]",p) for c in p)))(input()))