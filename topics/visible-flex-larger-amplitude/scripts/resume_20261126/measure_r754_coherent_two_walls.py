#!/usr/bin/env python3
"""Public complete R754 two-wall/rigid-left scan on their common actual initial metric."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import numpy as np
import r754_coherent_mirror_bowed_walls_two_jets as m
import r754_translate_complete_cap_bridge as bridge
import r742_tilted_disk_two_jets as tilt


LEVELS=((48,12,16,8),(96,24,24,16),(192,48,32,32))
PHASES=(0.,.15,.30,.45,.60,.75,.90)
COLUMNS=("regular_points","invalid_points","largest_relative_metric","absolute_principal",
         "least_chart_area","largest_tangent_condition","max_point_motion")


def costs(j,j0):
    j=j.reshape(-1,6,3)
    j0=j0.reshape(-1,6,3)
    f=np.swapaxes(j[:,1:3],1,2)
    f0=np.swapaxes(j0[:,1:3],1,2)
    finite=np.all(np.isfinite(j),axis=(1,2))&np.all(np.isfinite(j0),axis=(1,2))
    bad=int(np.count_nonzero(~finite));j,j0,f,f0=(a[finite] for a in (j,j0,f,f0))
    if not len(j):
        return [0,bad,None,None,None,None,None]
    _,s,v=np.linalg.svd(f,full_matrices=False)
    _,s0,v0=np.linalg.svd(f0,full_matrices=False)
    ok=(s[:,1]>1e-14*s[:,0])&(s0[:,1]>1e-14*s0[:,0])
    bad+=int(np.count_nonzero(~ok))
    j,j0,f,s,v,s0,v0=(a[ok] for a in (j,j0,f,s,v,s0,v0))
    if not len(j):
        return [0,bad,None,None,None,None,None]
    inv=np.swapaxes(v0,1,2)/s0[:,None,:]
    relative=f@inv
    gg=np.swapaxes(relative,1,2)@relative-np.eye(2)
    normal=np.cross(j[:,1],j[:,2]);area=np.linalg.norm(normal,axis=1)
    ii=np.einsum("ni,nki->nk",normal/area[:,None],j[:,3:])
    second=ii[:,[0,1,1,2]].reshape(-1,2,2)
    curvature=(v@second@np.swapaxes(v,1,2))/(s[:,:,None]*s[:,None,:])
    return [len(j),bad,float(np.max(np.abs(np.linalg.eigvalsh(gg)))),
            float(np.max(np.abs(np.linalg.eigvalsh(curvature)))),
            float(np.min(area)),float(np.max(s[:,0]/s[:,1])),
            float(np.max(np.linalg.norm(j[:,0]-j0[:,0],axis=1)))]


def grids(count,trans,order):
    lh,m0,m1,rtop,xl,xr,ux,uz,start,stop,core,half=m.constants(order)
    anchors=np.r_[0.,m.LEFT_LENGTH/2,m.LEFT_LENGTH/2+start,m.LEFT_LENGTH/2+stop,
                  m.LEFT_LENGTH/2+core,half,m.flat_material_s([-.65,-.50,0.,.08],order=order),
                  [m.grip_s(a,order) for a,_,_ in m.MARKS]]
    s=np.unique(np.r_[np.arange(count)*2*half/count,anchors,2*half-anchors])
    cap=np.unique(np.r_[np.linspace(1/trans,1,trans),.15,.35,.40,.70,1-m.CAP_JOIN,1-.002])
    vv=np.unique(np.r_[np.linspace(-1.,1.,trans+1),[y for _,y,_ in m.MARKS]])
    near=np.linspace(0,m.CAP_JOIN,trans+1)
    halfcore=.15*m.CORE
    angles=np.arange(trans)*2*np.pi/trans
    r=np.linspace(0,halfcore,4)
    aa,rr=np.meshgrid(angles,r,indexing="ij")
    corexy=(m.section_center(order)+rr*np.cos(aa)*.999999,rr*np.sin(aa)*.999999)
    out={"cylinder":np.meshgrid(s,vv,indexing="ij")}
    for side in ("+","-"):
        out["end"+side]=np.meshgrid(s,np.unique(np.r_[np.linspace(0,m.END_L,trans+1),m.END_E,m.END_L-m.END_E]),indexing="ij")
        out["cap"+side]=np.meshgrid(s,cap,indexing="ij")
        out["cap-normal"+side]=np.meshgrid(s,near,indexing="ij")
        out["cap-cartesian"+side]=corexy
    return out


class Raw:
    def __init__(self,path):
        self.fp=path.open("wb");self.h=sha256();self.n=0

    def add(self,arr):
        blob=np.asarray(arr,dtype="<f8").tobytes()
        self.fp.write(blob);self.h.update(blob);self.n+=len(blob)


def registered(s,v,ph,order,steps,rigid,raw):
    # Only x > 0 (or outside the two-wall protected strip), and .15<=rho<1,
    # can incur a numerical inverse error. Keep the address of every failed label.
    shape=s.shape
    out=np.full((s.size,6,3),np.nan)
    failures=[]
    x,y=s.ravel(),v.ravel()
    def batch(ids):
        try:
            q=bridge.chart_jet("cap+",x[ids],y[ids],ph,order,steps,rigid_left=rigid)
        except (ArithmeticError,ValueError,np.linalg.LinAlgError,FloatingPointError) as exc:
            if len(ids)>1:
                mid=len(ids)//2
                batch(ids[:mid]);batch(ids[mid:])
            else:
                failures.append([int(ids[0]),type(exc).__name__,str(exc)])
        else:
            out[ids]=q
    for a in range(0,s.size,512):
        batch(np.arange(a,min(a+512,s.size)))
    raw.add(out)
    data=json.dumps(failures,separators=(",",":"),ensure_ascii=True).encode()
    ledger_length=len(data).to_bytes(8,'little')
    for part in (ledger_length,data):
        raw.fp.write(part);raw.h.update(part);raw.n+=len(part)
    return out.reshape(shape+(6,3)),[len(failures),sha256(data).hexdigest(),failures[:1]]


def shortcut(ph,order,rigid):
    *_,core,half=m.constants(order)
    ll=m.LEFT_LENGTH/2
    pt=lambda s:m.chart_jet("cylinder",s,1.,ph,order,rotate=False,rigid_left=rigid)[0]
    p0=lambda s:m.chart_jet("cylinder",s,1.,0.,order,rotate=False,rigid_left=rigid)[0]
    p,db=m.terminal(order)
    # Explicit original oblique path on the left wall; quadrature is piecewise
    # with splits at both meridian ramps and at the wall angle clock ramp.
    nodes,weights=np.polynomial.legendre.leggauss(order)
    breaks=np.unique(np.r_[0.,m.END_E,m.END_L-m.END_E,m.END_L,
                           m.CLOCK_EDGE*m.LEFT_LENGTH*m.END_L/.25])
    length=0.
    for lo,hi in zip(breaks[:-1],breaks[1:]):
        v=lo+(hi-lo)*(nodes+1)/2
        j=m.chart_jet("end+",ll-.25*v/m.END_L,v,0.,order,rotate=False,rigid_left=rigid)
        length+=(hi-lo)/2*np.dot(weights,np.linalg.norm(j[:,2]-.25/m.END_L*j[:,1],axis=-1))
    t=m.chart_jet("end+",ll-.25,m.END_L,0.,order,rotate=False,rigid_left=rigid)[0]
    return {"left_cut_chord":float(np.linalg.norm(pt(ll)-pt(2*half-ll))),
            "left_initial_explicit_path":float(2*(length+t[2])),
            "equator_chord":float(np.linalg.norm(pt(0.)-pt(half))),
            "equator_initial_explicit_path":float(np.linalg.norm(p0(0.)-p0(half))+2*(m.END_L-db))}


def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument("--raw",type=Path,required=True);a.add_argument("--report",type=Path,required=True)
    args=a.parse_args()
    m.old.disk._public()
    raw=Raw(args.raw)
    rows=[]
    for count,trans,order,steps in LEVELS:
        gr=grids(count,trans,order)
        for rigid in (False,True):
            bas={k:m.chart_jet(k,s,v,0.,order,rigid_left=rigid) for k,(s,v) in gr.items()}
            # The regular upper and lower caps have equal planar geometry with
            # opposite y. Time-refined registration is measured separately on
            # both full caps on matching grids covering their entire domains.
            capgr=grids(max(12,count//4),max(4,trans//3),order)["cap+"]
            reg0=m.chart_jet("cap+",*capgr,0.,order,rigid_left=rigid)
            lower0=reg0.copy();lower0[...,1]*=-1.
            for ph in PHASES:
                row={"level":[count,trans,order,steps],"rigid_left":rigid,"phase":ph,
                     "charts":{},"shortcut":shortcut(ph,order,rigid)}
                for k,(s,v) in gr.items():
                    j=m.chart_jet(k,s,v,ph,order,rigid_left=rigid)
                    raw.add(j);row["charts"][k]=costs(j,bas[k])
                reg,failed=registered(*capgr,ph,order,steps,rigid,raw)
                row["transport_failure_count_ledger_sha_first"]=failed
                row["registered_cap+"]=costs(reg,reg0)
                lower=reg.copy();lower[...,1]*=-1.
                raw.add(lower);row["registered_cap-"]=costs(lower,lower0)
                row["charts"]=[row["charts"][name] for name in gr]
                row["shortcut"]=list(row["shortcut"].values())
                rows.append(row)
                print("finished",count,rigid,ph,failed[:1],flush=True)
    raw.fp.close()
    files=(__file__,m.__file__,bridge.__file__,m.old.__file__,m.old.disk.__file__,tilt.__file__)
    rep={"schema":"R754-actual-coherent-closed-full-two-variant-v1","run":os.environ["GITHUB_RUN_ID"],
         "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"trigger_commit":os.environ["GITHUB_SHA"],
         "rules_read_commit":os.environ["R754_RULES_COMMIT"],
         "source_commit":os.environ["R754_SOURCE_COMMIT"],
         "sources":{Path(f).name:[len(Path(f).read_bytes()),sha256(Path(f).read_bytes()).hexdigest()] for f in files},
         "columns":COLUMNS,"chart_order":list(gr),
         "shortcut_order":["left_cut_chord","left_initial_explicit_path","equator_chord","equator_initial_explicit_path"],
         "rows":rows,"whole_raw":{"bytes":raw.n,"sha256":raw.h.hexdigest(),"uploaded":False},
         "scope":"Two original R754 fields, three full grids, seven phases, nine complete charts, both cap transports and both named initial paths. Plane-cap lower transport is the exact y reflection, including all derivatives. Values are finite diagnostics, with any failed inverses reported."}
    args.report.write_text(json.dumps(rep,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
    print("R754 complete report bytes",args.report.stat().st_size,flush=True)


if __name__=="__main__":
    main()
