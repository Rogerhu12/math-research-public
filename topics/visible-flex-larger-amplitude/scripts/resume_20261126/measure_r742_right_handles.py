#!/usr/bin/env python3
"""Measure both physical handle repairs with the original unprojected R742 six jets."""
import argparse
from dataclasses import asdict
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import numpy as np
import r742_right_physical_handle as candidate
import measure_r742_tilted_shoulders as earlier


def measure(d,level,raw):
    n,m,order=level
    c=np.array([.58,0,.58*np.tan(d.gamma)])
    stages={};count=0
    for name,ss in earlier.rings(d,n):
        row={}
        for s in ss:
            a=earlier.angles(s,name,d,m,order)
            if name=="B":
                rr=float(candidate.r.base.rolled_radii(candidate.r.base.A_LENGTH,order)[0])
                knots=np.arccos(np.array([.70,.85,.90,.93,1.00])/rr)
                a=np.unique(np.r_[a,knots,2*np.pi-knots])
            j=candidate.shoulder_jet(s,a,d,False,order=order)
            f=candidate.r.costs(j,c)
            K=np.maximum(np.abs(f["k1"]),np.abs(f["k2"]))
            support=f["support"]
            if not np.all(np.isfinite(K)) or not np.all(np.isfinite(support)):
                raise ValueError("nonfinite on complete declared field")
            y=f["E"]-f["mixed"]**2/f["G"]
            vel=j[:,1]-j[:,2]*(f["mixed"]/f["G"])[:,None]
            z=np.sum(vel*j[:,5],axis=1)/f["G"]
            earlier.extremum(row,"K",K,a,s)
            earlier.extremum(row,"support",support,a,s,True)
            earlier.extremum(row,"area",f["area"],a,s,True)
            for sector,take in (("left",np.cos(a)<-.7),("right",np.cos(a)>.7),
                                ("middle",np.abs(np.cos(a))<=.7)):
                earlier.extremum(row,"K_"+sector,K[take],a[take],s)
            for field,col in (("Eperp",y),("V_dot_section_curvature",z)):
                hi,lo=int(np.argmax(col)),int(np.argmin(col))
                value=float(col[hi]-col[lo])
                if field not in row or value>row[field][0]:
                    row[field]=[value,float(s),float(a[hi]),float(a[lo])]
            raw.write(np.column_stack((np.full(len(a),s),a,j.reshape(len(a),18),K,
                      support,f["area"],y,z)).astype("<f8",copy=False).tobytes())
            count+=len(a)
        stages[name]=row
    return {"levels":level,"samples":count,"charts":stages}


if __name__=="__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--work",required=True,type=Path)
    cli.add_argument("--summary",required=True,type=Path)
    args=cli.parse_args()
    candidate.r.base._public();args.work.mkdir(parents=True,exist_ok=True)
    out={};raw=args.work/"right-original-two-jets.f64le"
    with raw.open("wb") as f:
        for k,d in candidate.DESIGNS.items():
            data=[measure(d,l,f) for l in earlier.LEVELS]
            out[k]={"parameters":asdict(d),"resolutions":data}
            print(k,{s:(p["K"][0],p["support"][0]) for s,p in data[-1]["charts"].items()},flush=True)
    h=sha256()
    with raw.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    e=os.environ
    rec={"schema":"R742-right-physical-handle-complete-cost-v1","repository":e["GITHUB_REPOSITORY"],
        "run":e["GITHUB_RUN_ID"],"attempt":e["GITHUB_RUN_ATTEMPT"],"rules_read_commit":e["R742_RULES_COMMIT"],
        "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
        "trigger_commit":e["GITHUB_SHA"],"source_files":{p:earlier.blob(Path(__file__).parent/p) for p in
          ("r740_rolled_disk_seed.py","r742_tilted_disk_two_jets.py","measure_r742_tilted_shoulders.py",
           "r742_right_physical_handle.py",Path(__file__).name)},"whole_raw":{"bytes":raw.stat().st_size,
           "sha256":h.hexdigest(),"uploaded":False},"design_order":list(candidate.DESIGNS),"results":out,
        "bounds_scope":"Both physical handles including all sections and 3 original complete levels, true six jets and first/second forms. Entries are [working extremum, physical s, material theta] with two angles for invariant spreads. Numeric finite samples do not certify continuous bounds."}
    args.summary.write_text(json.dumps(rec,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
