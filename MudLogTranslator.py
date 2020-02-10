# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 03:29:54 2020

@author: Luthfi (lsaif.github.com)
"""
import csv

with open('litho_dict.csv', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)
    litholist = dict(reader)
  
def translate(desc,transdict):
    words = desc.split()
    trans = [transdict.get(w.lower(),w) for w in words]
    translation = (' '.join(trans))
    return translation

lithodesc = "Cgl lt gy sbang"
print (translate(lithodesc,litholist))