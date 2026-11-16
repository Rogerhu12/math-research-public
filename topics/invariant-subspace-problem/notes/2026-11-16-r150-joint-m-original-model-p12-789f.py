#!/usr/bin/env python3
"""Read the frozen exact original17 model and reduce its coefficients modulo31^12.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
No regenerated equations, altered parameter, or higher-precision zero padding.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os
from pathlib import Path
P12=787662783788549761
EXACT_BYTES=65159
EXACT_SHA="44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"
RAW_BYTES=158741
RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
LOWER_BYTES=22824
LOWER_SHA="2785c53d015d05db4550e1978c05db7d42009cfa8942e915541599a76d3701cc"
def sha(b):return hashlib.sha256(b).hexdigest()
def check(ok,text):
 if not ok:raise ValueError(text)
def atomic(path,b):
 path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_name(path.name+".tmp");tmp.write_bytes(b);os.replace(tmp,path)
def product(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def generate(exact_path,lower_path,out):
 packed=exact_path.read_bytes()
 check(len(packed)==EXACT_BYTES and sha(packed)==EXACT_SHA,"exact original primitive gzip identity")
 raw=gzip.decompress(packed)
 check(len(raw)==RAW_BYTES and sha(raw)==RAW_SHA,"exact original primitive payload identity")
 data=json.loads(raw)
 check(data["format"]=="r150-original-primitive-integer-equations-v1","original model format")
 equations=[[[int(x) for x in p] for p in row] for row in data["equations"]]
 check(len(equations)==17 and all(len(row)==77 for row in equations),"all17 original polynomial rows")
 units=[int(data["denominator"])]+list(map(int,data["contents"]))
 check(len(units)==18 and all(x%31 for x in units),"all original primitive row31-units")
 fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
 h0=product(product(product(product([0,0,0,1],[-2,1]),product(fp,fp)),product(fm,fm)),e8)
 check(list(map(int,data["h0"]))==h0 and len(h0)==25 and h0[-1]==3125,"same original h0 polynomial")
 rows=[];flat=[]
 for e in range(11):
  row=equations[e];values=[]
  for k in range(66):
   p=row[k+11];check(not any(p[1:]),"original N quadratic parameter degree")
   values.append(p[0] if p else 0)
  for v in range(11):
   check(not any(row[v][11:]),"original N linear parameter degree")
   values.extend(row[v][d] if d<len(row[v]) else 0 for d in range(11))
  rows.append(values);flat.extend(values)
 for e in range(11,17):
  row=equations[e];check(not any(x for p in row[:11] for x in p),"original Gamma has no linear terms")
  values=[]
  for k in range(66):
   p=row[k+11];check(not any(p[6:]),"original Gamma parameter degree")
   values.extend(p[d] if d<len(p) else 0 for d in range(6))
  rows.append(values);flat.extend(values)
 check(len(flat)==4433,"all4433 original coefficients")
 lower_raw=lower_path.read_bytes()
 check(len(lower_raw)==LOWER_BYTES and sha(lower_raw)==LOWER_SHA,"same paid original mod31^3 model")
 lower=lower_raw.decode("ascii").split()
 check(len(lower)==4478 and [x%29791 for x in units+flat]==list(map(int,lower[1:-26])),
       "all18 scales and4433 coefficients agree with paid mod31^3 model")
 lines=["R150_ORIGINAL_EQUATIONS_P12_V1 31 "+str(P12)+" 17 4433",
        " ".join(str(x%P12) for x in units)]
 lines.extend(" ".join(str(x%P12) for x in row) for row in rows)
 output=("\n".join(lines)+"\n").encode("ascii")
 atomic(out,output)
 result={"status":"completed","format":"r150-joint-m-original-p12-model-v1","prime":31,"modulus":P12,
  "exactCompressedBytes":len(packed),"exactCompressedSHA256":sha(packed),"exactPayloadSHA256":sha(raw),
  "lowerModelSHA256":sha(lower_raw),"all4433OriginalEquationResiduesVerified":True,
  "all18OriginalRowScaleResiduesVerified":True,"sameOriginalH0Verified":True,
  "newEquationsRegenerated":False,"originalParameterUnchanged":True,
  "modelBytes":len(output),"modelSHA256":sha(output)}
 atomic(Path(str(out)+".json"),(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode("ascii"))
 return result
def main():
 p=argparse.ArgumentParser()
 for name in ("exact-gzip","lower-model","out"):p.add_argument("--"+name,type=Path,required=True)
 a=p.parse_args();print(json.dumps(generate(a.exact_gzip,a.lower_model,a.out)),flush=True)
if __name__=="__main__":main()

