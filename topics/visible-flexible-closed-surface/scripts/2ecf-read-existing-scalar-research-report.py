#!/usr/bin/env python3
"""Read a completed small scalar report without repeating its computation."""
import argparse, hashlib, json
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("--input",type=Path,required=True)
p.add_argument("--out",type=Path,required=True)
a=p.parse_args()
raw=a.input.read_bytes()
data=json.loads(raw)
if not isinstance(data,dict): raise ValueError("Expected an existing scalar research object")
data["existingReportSHA256"]=hashlib.sha256(raw).hexdigest()
data["existingReportBytes"]=len(raw)
data["observationOnlyNoRecalculation"]=True
with a.out.open("x") as f:
    json.dump(data,f,indent=2)
    f.write("\n")
