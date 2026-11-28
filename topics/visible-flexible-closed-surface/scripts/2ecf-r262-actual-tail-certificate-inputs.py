#!/usr/bin/env python3
"""Prepare actual regenerated R262 continuous tail inputs in temporary storage."""
import argparse,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser()
for name in ("scripts","work","out"):
    p.add_argument("--"+name,type=Path,required=True)
a=p.parse_args()
a.out.parent.mkdir(parents=True,exist_ok=True)
F=a.work/"h2-c2-m48-g12-04r1"
O=a.out.parent
common=["--scripts",str(a.scripts),"--data",str(a.work/"m12-prefix-data.npz.gz")]
field=common+["--grid",str(F/"grid.json"),"--field",str(F/"result.json.field.npz"),"--result",str(F/"result.json")]
def run(name,args):
    subprocess.run([sys.executable,str(a.scripts/name),*map(str,args)],check=True)
run("6a65-m12-entire-half-continuous-correction-bounds.py",field+["--out",str(O/"correction.json")])
run("6a65-m12-original-common-cut-prefix-source-bounds.py",common+["--tail-report",str(F/"exact-tail-queries.json"),"--tail-cache",str(F/"exact-tail-queries.json.npz"),"--out",str(O/"source.json")])
spec=importlib.util.spec_from_file_location("original_recovery",a.scripts/"2ecf-r262-four-field-reconstruction.py")
r=importlib.util.module_from_spec(spec)
sys.modules["original_recovery"]=r
spec.loader.exec_module(r)
r.fetch_blob("24aefcd94bbedb908a345d2a46ac1422b57706ab",1724765,"28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9",O/"m12-primitive.json")
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
out=dict(fieldSHA256=sha(F/"result.json.field.npz"),correctionSHA256=sha(O/"correction.json"),sourceSHA256=sha(O/"source.json"),primitiveSHA256=sha(O/"m12-primitive.json"),scope="Actual regenerated field and exact original source bounds; not a transferred old whole-geometry certificate")
with a.out.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
