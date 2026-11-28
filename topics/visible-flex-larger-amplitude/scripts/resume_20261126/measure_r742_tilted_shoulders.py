#!/usr/bin/env python3
"""Evaluate complete finite R742 shoulders and physical handles on the public runner."""
import argparse
from dataclasses import asdict, replace
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import numpy as np

import r742_tilted_disk_two_jets as ref


LEVELS=((32,128,16),(64,256,24),(128,512,32))
SCRIPT_DIR=Path(__file__).resolve().parent


def blob(path):
    b=path.read_bytes()
    return {"bytes":len(b),"sha256":sha256(b).hexdigest()}


def extremum(record,name,vector,theta,s,minimum=False):
    index=int(np.argmin(vector) if minimum else np.argmax(vector))
    v=float(vector[index])
    if name not in record or (v<record[name][0] if minimum else v>record[name][0]):
        record[name]=[v,float(s),float(theta[index])]


def rings(design,n):
    A=ref.base.A_LENGTH;L=design.join;Z=design.end_height
    for key,lo,hi,knots in (("A",0,A,[ref.base.BLEND,A-ref.base.BLEND]),
                ("B",A,A+L,[A+L*j/8 for j in range(1,8)]),
                ("wall",A+L,A+L+Z,[A+L+Z/2])):
        yield key,np.unique(np.r_[np.linspace(lo,hi,n+1),knots])


def angles(s,key,design,m,order):
    a=np.arange(m)*2*np.pi/m
    r=float(ref.base.rolled_radii(min(s,ref.base.A_LENGTH),order)[0])
    cuts=[ref.base.HOLD+ref.base.BEND*x for x in
          (0,ref.base.EDGE/2,ref.base.EDGE,.5,1-ref.base.EDGE,1-ref.base.EDGE/2,1)]
    cuts+= [-.75,-.475,-.20]
    breaks=np.arccos(np.clip(np.asarray(cuts)/r,-1,1))
    return np.unique(np.r_[a,breaks,2*np.pi-breaks])


def measure(design,n,m,order,raw):
    c=np.array([.58,0,.58*np.tan(design.gamma)])
    sections={};samples=0
    for key,ss in rings(design,n):
        section={}
        for s in ss:
            theta=angles(s,key,design,m,order)
            jets=ref.shoulder_jet(s,theta,design,normalized=False,order=order)
            g=ref.costs(jets,c)
            K=np.maximum(np.abs(g["k1"]),np.abs(g["k2"]))
            y=g["E"]-g["mixed"]**2/g["G"]
            v=jets[:,1]-jets[:,2]*(g["mixed"]/g["G"])[:,None]
            inner=np.sum(v*jets[:,5],axis=1)/g["G"]
            if not np.all(np.isfinite(jets)) or not all(np.all(np.isfinite(arr)) for arr in (K,y,inner,g["support"])):
                raise ArithmeticError("non-finite actual field at "+str((key,s)))
            extremum(section,"absolute_principal_max",K,theta,s)
            extremum(section,"euclidean_center_support_min",g["support"],theta,s,True)
            extremum(section,"physical_area_min",g["area"],theta,s,True)
            left=np.cos(theta)<-.7
            extremum(section,"absolute_principal_left_max",K[left],theta[left],s)
            # These are true scalar invariants of the given meridian foliation.
            for name,col in (("normal_speed_squared_spread",y),("normal_velocity_dot_section_curvature_spread",inner)):
                j,k=int(np.argmax(col)),int(np.argmin(col))
                span=float(col[j]-col[k])
                if name not in section or span>section[name][0]:
                    section[name]=[span,float(s),float(theta[j]),float(theta[k])]
            buf=np.column_stack([np.full(len(theta),s),theta,jets.reshape(len(theta),18),K,
                                 g["support"],g["area"],y,inner]).astype("<f8",copy=False).tobytes()
            raw.write(buf);samples+=len(theta)
        sections[key]=section
    return {"level":[n,m,order],"sample_count":samples,"sections":sections}


def calculate(work,summary):
    ref.base._public();work.mkdir(parents=True,exist_ok=True)
    designs=dict(ref.DESIGNS)
    for tag,d in (("32",ref.TILT32),("44",ref.TILT44)):
        for handle in (.045,.14):
            designs["tilt"+tag+"-left-"+str(handle)]=replace(d,left_handle=handle)
        for lateral in (-.009,.009):
            designs["tilt"+tag+"-left.09-dx"+str(lateral)]=replace(d,left_handle=.09,lateral=lateral)
    results={}
    path=work/"r742-complete-physical-field-and-costs.f64le"
    with path.open("wb") as stream:
        for name,d in designs.items():
            levels=[measure(d,*level,stream) for level in LEVELS]
            results[name]={"parameters":asdict(d),"levels":levels}
            print(name,"fine A/B/wall K and minimum support",
                  [(v["absolute_principal_max"][0],v["euclidean_center_support_min"][0])
                   for v in levels[-1]["sections"].values()],flush=True)
    digest=sha256()
    with path.open("rb") as f:
        for part in iter(lambda:f.read(1048576),b""):
            digest.update(part)
    # One self-contained fine table per design, full extrema of both earlier levels
    # as compact rows. The complete physical samples are identified by their raw hash.
    logical={}
    fields=("absolute_principal_max","euclidean_center_support_min","physical_area_min",
            "absolute_principal_left_max","normal_speed_squared_spread","normal_velocity_dot_section_curvature_spread")
    for name,res in results.items():
        coarse=[[[k,[data["sections"][k][field][0] for field in fields]]
                 for k in ("A","B","wall")] for data in res["levels"][:-1]]
        logical[name]={"parameters":res["parameters"],"samples":[v["sample_count"] for v in res["levels"]],
                       "earlier_extrema":coarse,"fine":res["levels"][-1]["sections"]}
    env=os.environ
    record={"schema":"R742-original-ellipse-and-tilt-all-physical-six-jet-costs-v1",
         "repository":env["GITHUB_REPOSITORY"],"run":env["GITHUB_RUN_ID"],"attempt":env["GITHUB_RUN_ATTEMPT"],
         "rules_read_commit":env["R742_RULES_COMMIT"],"trigger_commit":env["GITHUB_SHA"],
         "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
         "source_files":{p:blob(SCRIPT_DIR/p) for p in ("r740_rolled_disk_seed.py",
                              "r742_tilted_disk_two_jets.py",Path(__file__).name)},
         "levels_ring_intervals_uniform_angles_gauss_order":LEVELS,"earlier_extrema_order":fields,
         "coordinates":"Each extremum gives [working value, original physical shoulder material, material angle]; spreads give both angles. Coverage includes all three complete original shoulder stages, every angular sector, both endpoints and the extra analytic break rings. Disk and reflected sides are the exact accompanying R740/R742 charts. Center=(.58,0,.58 tan(gamma)) lies in the reflection plane; spatially rotate center with phase.",
         "scientific_scope":"Direct physical six jets, before any Fourier projection. Finite grid extrema and quadrature are working numerical observations, not outward intervals or whole-surface certificates. Principal curvature uses the actual first and second forms. No fixed-metric nonlinear outcome is asserted.",
         "raw_column_order":"s, theta, (F,Fu,Fa,Fuu,Fua,Faa) xyz, max abs principal, outward support, area, Eperp, V dot section curvature. Record order is design insertion order, then level, A/B/wall, increasing s then theta.",
         "design_order":list(designs),"all_working_raw":{"bytes":path.stat().st_size,"sha256":digest.hexdigest(),
         "uploaded":False},"results":logical}
    summary.write_text(json.dumps(record,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--work",type=Path,required=True)
    p.add_argument("--summary",type=Path,required=True)
    a=p.parse_args();calculate(a.work,a.summary)
