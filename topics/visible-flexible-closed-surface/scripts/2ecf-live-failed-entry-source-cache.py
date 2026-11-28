#!/usr/bin/env python3
"""Inspect only the source cache and named actual outputs after a failed research entry."""
import argparse,json,hashlib
from pathlib import Path
def main():
 a=argparse.ArgumentParser()
 a.add_argument('--scripts',type=Path,required=True)
 a.add_argument('--work',type=Path,required=True)
 a.add_argument('--out',type=Path,required=True)
 z=a.parse_args()
 names=['2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py','2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py','2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py','2ecf-r262-cut-same-metric-banded-direct-newton.py','2ecf-r262-cut-frozen-native-and-true-material-position.py','2ecf-r299-actual-thick-arms-and-tapered-central-belt-v3.py','2ecf-adjacent-low-ports-0350-physical-belt.py','2ecf-r262-true-three-arcs-cut-directed-position-kernel.py','2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py']
 rows=[]
 for name in names:
  q=z.scripts/name
  rows.append(dict(name=name,exists=q.is_file(),sha256=hashlib.sha256(q.read_bytes()).hexdigest() if q.is_file() else None))
 states=['adjacent-low/fixed-h1.npz','adjacent-low/h1-physical-inlet.json','adjacent-low/h1-physical-inlet.npz','adjacent-two-moment/fixed-h1.npz','adjacent-two-moment/h1-physical-inlet.npz','adjacent-two-moment-060/fixed-h1.npz','adjacent-two-moment-060/h1-physical-inlet.npz']
 result=dict(schema='actual-source-cache-after-failed-entry-v1',sources=rows,missingSources=[q['name'] for q in rows if not q['exists']],outputs={n:(z.work/n).is_file() for n in states},scope='Filesystem metadata only; no successful scientific calculation repeated.')
 z.out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result),flush=True)
if __name__=='__main__':main()
