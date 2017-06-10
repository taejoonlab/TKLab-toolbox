#!/usr/bin/env python3
import os

tax2filename = dict()
for filename in os.listdir('.'):
    tmp_tax_id = filename.split('.')[0]
    if not tmp_tax_id in tax2filename:
        tax2filename[tmp_tax_id] = filename
    elif len(tax2filename[tmp_tax_id]) > len(filename):
        tax2filename[tmp_tax_id] = filename

for tmp_tax_id, tmp_filename in tax2filename.items():
    print("mv %s .."%tmp_filename)
