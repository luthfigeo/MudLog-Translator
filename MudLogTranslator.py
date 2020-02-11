"""
Created on Mon Feb 10 03:29:54 2020
@author: Luthfi (lsaif.github.com)
"""
from flask import Flask, render_template, request, jsonify
import csv
import re

with open('litho_dict.csv', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)
    litholist = dict(reader)
  
def translate(desc,transdict):
     words = desc.split(' ')
     trans = [transdict.get(x.lower(),x) for x in words]
     translation = (' '.join(trans))
     words = re.split('(\W)', translation)
     trans = [transdict.get(x.lower(),x) for x in words]
     translation = (''.join(trans))
     translation = translation.replace('.',',')
     return translation
 
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('../index.html')

@app.route('/', methods=['GET','POST'])
def mudlog_translator():
    
    if request.method == "POST":
        lithodesc = request.form.get('lithology_description')
        print (translate(lithodesc,litholist))
        result = (translate(lithodesc,litholist))
    return render_template('../index.html', result = result)

sample = "Sstone.bn Lt-gry.vf-gr.sbrnd.Fr-cmt.M-srt.ltl-Mtrx.hd. w ltl Fe min mtrx a.a"

if __name__ == "__main__":
    app.run(debug=True)