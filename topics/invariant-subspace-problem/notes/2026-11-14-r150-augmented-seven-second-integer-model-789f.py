#!/usr/bin/env python3
"""Reduce the already saved exact primitive integer equations modulo31^5."""
from __future__ import annotations
import argparse,gzip,hashlib,json
from pathlib import Path
EXACT_GZIP_SHA="44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"
EXACT_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
P5=28629151
def sha(b):return hashlib.sha256(b).hexdigest()
def product(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def generate(exact_path,lower_path,out):
    compressed=exact_path.read_bytes()
    if sha(compressed)!=EXACT_GZIP_SHA:raise ValueError("frozen exact integer gzip")
    raw=gzip.decompress(compressed)
    if sha(raw)!=EXACT_SHA:raise ValueError("frozen exact primitive integer equations")
    data=json.loads(raw)
    if data["format"]!="r150-original-primitive-integer-equations-v1":raise ValueError("exact original model format")
    equations=[[[int(x) for x in p] for p in row] for row in data["equations"]]
    if len(equations)!=17 or any(len(row)!=77 for row in equations):raise ValueError("all original17 equation terms")
    contents=list(map(int,data["contents"]));denominator=int(data["denominator"])
    if len(contents)!=17 or any(x%31==0 for x in [denominator]+contents):raise ValueError("original fixed row-scale units")
    fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
    h0=product(product(product(product([0,0,0,1],[-2,1]),product(fp,fp)),product(fm,fm)),e8)
    if list(map(int,data["h0"]))!=h0 or len(h0)!=25 or h0[-1]!=3125:raise ValueError("same exact integer h0")
    lines=["R150_ORIGINAL_P2H0_MOD28629151_V1"," ".join(str(x%P5) for x in [denominator]+contents)]
    checks=0
    for e in range(11):
        row=equations[e];values=[]
        for k in range(66):
            poly=row[k+11]
            if any(poly[1:]):raise ValueError("N quadratic parameter dependence")
            values.append(poly[0] if poly else 0);checks+=1
        for v in range(11):
            if any(row[v][11:]):raise ValueError("N linear degree exceeds10")
            for d in range(11):values.append(row[v][d] if d<len(row[v]) else 0);checks+=1
        lines.append(" ".join(str(x%P5) for x in values))
    for e in range(11,17):
        row=equations[e]
        if any(x for poly in row[:11] for x in poly):raise ValueError("Gamma linear part changed")
        values=[]
        for k in range(66):
            poly=row[k+11]
            if any(poly[6:]):raise ValueError("Gamma quadratic parameter degree exceeds5")
            for d in range(6):values.append(poly[d] if d<len(poly) else 0);checks+=1
        lines.append(" ".join(str(x%P5) for x in values))
    lines.append(" ".join(str(961*x%P5) for x in h0)+" 0")
    text="\n".join(lines)+"\n";tokens=text.split();lower=lower_path.read_text().split()
    if checks!=4433 or len(tokens)!=4478 or len(lower)!=4478 or lower[0]!="R150_ORIGINAL_PH0_MOD923521_V1":
        raise ValueError("same exact4433 coefficient schema")
    if [int(x)%923521 for x in tokens[1:-26]]!=list(map(int,lower[1:-26])) or [int(x)//31 for x in tokens[-26:]]!=list(map(int,lower[-26:])) or any(int(x)%961 for x in tokens[-26:]):
        raise ValueError("all equation/scaling residues modulo31^4 and target divided by31 must match the completed actual model")
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text)
    result={"format":"r150-same-original-integer-model-mod31five-v1","status":"completed","prime":31,"modulus":P5,
        "target":"31^2*h0","all4433OriginalEquationResiduesVerified":True,"all18OriginalRowScaleResiduesVerified":True,
        "lowerMod31FourEquationModelAndDividedTargetVerified":True,"exactIntegerJSONSHA256":EXACT_SHA,
        "lowerModelSHA256":sha(lower_path.read_bytes()),"modelSHA256":sha(text.encode()),"modelBytes":len(text),
        "exactOriginalModelRegenerated":False,"onlyExactSavedIntegerReductionPerformed":True}
    Path(str(out)+".json").write_text(json.dumps(result,indent=2)+"\n")
    return result
def main():
    p=argparse.ArgumentParser()
    for name in ("exact-gzip","lower-model","out"):p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args();print(json.dumps(generate(a.exact_gzip,a.lower_model,a.out)),flush=True)
if __name__=="__main__":main()
